#!/usr/bin/env python

'''
clara CLI interface
'''

# Python imports
import glob
import json
import os
import pprint
import shutil
import sys
import traceback

from ast import literal_eval

# clara imports
from clara.common import parseargs, debug
from clara.feedback import Feedback, FeedGen
from clara.feedback_repair import RepairFeedback
from clara.feedback_simple import SimpleFeedback
from clara.feedback_python import PythonFeedback
from clara.interpreter import getlanginter
from clara.matching import Matching
from clara.clustering import Clustering
from clara.model import expr_to_dict, dict_to_expr
from clara.parser import getlangparser
from clara.repair import Repair

VERBOSE=0

class Clara(object):

    USAGE = '''
%s COMMAND [OPTIONS*] SOURCE_FILE_1 SOURCE_FILE_2 ...

Commands are:
  help       print this usage message
  model      prints a model of a program
  match      run the matching procedure on two source files
  cluster    run the clustering on a set of files
  repair     run the repair algorithm on two source files
  feedback   generates feedback on multiple specifications

Options are:
  --verbose [0|1]    controls the amount of output information printed
                     (default is 0)
  --lang LANG        language of the source files
                     (default is to guess from the first source file extension)
  --args ARGS        arguments for matching or repair
  --argsfile FILE    file with arguments for matching or repair
  --ins INS          inputs for matching or repair
  --insfile FILE     file with arguments for matching or repair
  --entryfnc FNC     entry function for matching or repair
                     (default is 'main')
  --ignoreio [0|1]   whether to ignore IO in matching or repair
  --ignoreret [0|1]  whether to ignore return value in matching or repair
  --bijective [0|1]  whether to perform bijective matching (default is 1)
  --cleanstrings [0|1]
                     whether to clean (trim) strings when checking correctness
                     in the repair algorithm (default is 0)
  --timeout INT      timeout in seconds (for the repair)
                     (default is 60)
  --suboptimal [0|1] allow sub-optimal repairs (default is 1)
  --poolsize INT     number of (parallel) processes to use for feedback
                     (default is the number of CPUs)
  --feedtype FEED    type of feedback to generate ('repair', 'simple')
                     (default is 'repair')
  --maxfeedcost N    maximum cost of a repair for feedback; if cost is larger
                     than N, an error occurs
                     (default is 0, which means that there is no limit)
  --clusterdir DIR   directory to write/read clustering results
'''

    def __init__(self):
        pass

    def usage(self):
        '''
        Prints usage information (to stderr).
        '''

        print(self.USAGE % (sys.argv[0],), file=sys.stderr)

    def debug(self, msg, *args):
        '''
        Prints debug message if verbose mode on.
        '''
        
        if self.verbose:
            debug(msg, *args)

    def error(self, msg, *args):
        '''
        Prints error message and exits
        '''
        
        if args:
            msg %= args
        print('Error: %s\n' % (msg,), file=sys.stderr)
        sys.exit(1)

    def main(self):

        global VERBOSE

        self.args, self.opts = parseargs(sys.argv[1:])

        if len(self.args) < 1:
            self.usage()
            self.error('Command not specified!')

        self.cmd = self.args[0]
        self.sources = self.args[1:]

        if self.cmd == 'help':
            self.usage()
            return

        self.verbose = int(self.opts.pop('verbose', 0))
        VERBOSE = self.verbose
        
        self.lang = self.opts.pop('lang', None)
        self.timeout = int(self.opts.pop('timeout', 60))
        self.ignoreio = int(self.opts.pop('ignoreio', 0))
        self.ignoreret = int(self.opts.pop('ignoreret', 0))
        self.bijective = int(self.opts.pop('bijective', 1))
        self.cleanstrings = int(self.opts.pop('cleanstrings', 0))
        self.entryfnc = self.opts.pop('entryfnc', 'main')
        self.suboptimal = int(self.opts.pop('suboptimal', 1))
        self.maxfeedcost = int(self.opts.pop('maxfeedcost', 0))
        self.clusterdir = self.opts.pop('clusterdir', 'clusters')

        self.poolsize = self.opts.pop('poolsize', None)
        if self.poolsize is not None:
            self.poolsize = int(self.poolsize)

        self.feedtype = self.opts.pop('feedtype', 'repair')
        if self.feedtype == 'repair':
            self.feedtype = RepairFeedback
        elif self.feedtype == 'simple':
            self.feedtype = SimpleFeedback
        elif self.feedtype == 'python':
            self.feedtype = PythonFeedback
        else:
            self.error("Unknown feedback type: '%s'", self.feedtype)

        self.ins = self.opts.pop('ins', None)
        self.args = self.opts.pop('args', None)
        self.insfile = self.opts.pop('insfile', None)
        self.argsfile = self.opts.pop('argsfile', None)

        if self.ins is not None and self.insfile is not None:
            self.error('Got both inputs and file with inputs: which to use?')
        if self.args is not None and self.argsfile is not None:
            self.error('Got both args and file with args: which to use?')
        
        if self.ins is not None:
            self.ins = literal_eval(self.ins)
        if self.args is not None:
            self.args = literal_eval(self.args)
        if self.insfile is not None:
            with open(self.insfile, 'r') as f:
                self.ins = literal_eval(f.read())
        if self.argsfile is not None:
            with open(self.argsfile, 'r') as f:
                self.args = literal_eval(f.read())

        if self.lang is None:
            self.guess_lang()

        self.parser = getlangparser(self.lang)
        self.inter = getlanginter(self.lang)

        self.process_sources()

        if self.cmd == 'match':
            self.match()

        elif self.cmd == 'cluster':
            self.cluster()

        elif self.cmd == 'model':
            self.model()

        elif self.cmd == 'repair':
            self.repair()

        elif self.cmd == 'feedback':
            self.feedback()

        elif self.cmd == 'eval':
            self.eval()

        else:
            self.usage()
            self.error("Unknown command: '%s'", self.cmd)

    def model(self):

        if len(self.models) != 1:
            self.error('Model requires one program!')

        print(self.models[0].tostring())

    def match(self):

        if len(self.models) < 2:
            self.error('Match requires two programs!')

        elif len(self.models) > 2:
            self.debug('Match requires two programs, ignoring the rest!')

        M = Matching(ignoreio=self.ignoreio, ignoreret=self.ignoreret,
                     verbose=self.verbose, bijective=self.bijective)

        m = M.match_programs(self.models[0], self.models[1], self.inter,
                             ins=self.ins, args=self.args,
                             entryfnc=self.entryfnc)
        if m:
            self.debug('Match: %s', pprint.pformat(m[1]))
            print('Match!')
        else:
            print('No match!')

    def cluster(self):
        if len(self.models) < 1:
            self.error('Clustering requires at least one program!')

        if not os.path.isdir(self.clusterdir):
            self.error("Clustering directory '%s' does not exist!", self.clusterdir)

        M = Matching(ignoreio=self.ignoreio, ignoreret=self.ignoreret,
                     verbose=self.verbose, bijective=self.bijective)
        C = Clustering(M)

        existing = []
        for f in glob.glob(os.path.join(self.clusterdir, "*." + self.lang)):
            model = self.process_source(f)
            existing.append(model)
        print("Found %d existing clusters" % (len(existing)))
                    
        new, mod = C.cluster(self.models, self.inter,
                             ins=self.ins, args=self.args,
                             entryfnc=self.entryfnc, existing=existing)

        print("Done, %d new clusters, %d modified clusters" % (len(new), len(mod)))
        
        # Add new clusters
        for f in new:
            f.new_name = os.path.join(self.clusterdir, f.new_name)
            print("NEW:", f.name, "->", f.new_name)

            # Copy the source file
            if os.path.exists(f.new_name):
                self.error("Filename '%s' already exists!")
            shutil.copyfile(f.name, f.new_name)

            # Dump expressions
            f.name = f.new_name
            self.dump_exprs(f)

        # Write modifications for the modified clusters
        for f in mod:
            print("MOD:", f.name)
            self.dump_exprs(f)

    def eval(self):

        if len(self.models) != 1:
            self.error('Eval requires exactly one program!')

        print(self.models[0])
        print()

        inter = self.inter(entryfnc=self.entryfnc)
        trace = inter.run(self.models[0], args=self.args, ins=self.ins)

        print(trace)

    def repair(self):

        if len(self.models) < 2:
            self.error('Repair requires two programs!')

        elif len(self.models) > 2:
            self.debug('Repair requires two programs, ignoring the rest!')

        R = Repair(timeout=self.timeout, verbose=self.verbose,
                   allowsuboptimal=self.suboptimal,
                   cleanstrings=self.cleanstrings)

        r = R.repair(self.models[0], self.models[1], self.inter,
                     ins=self.ins, args=self.args, ignoreio=self.ignoreio,
                     ignoreret=self.ignoreret, entryfnc=self.entryfnc)
        if r:
            txt = RepairFeedback(self.models[1], self.models[0], r)
            txt.genfeedback()
            print('Repairs:')
            print('\n'.join(['  * %s' % (x,) for x in txt.feedback]))
        else:
            print('No repair!')

    def feedback(self):

        if len(self.models) < 2:
            self.error('Feedback requires at least two programs!')

        F = FeedGen(verbose=self.verbose, timeout=self.timeout,
                    poolsize=self.poolsize, allowsuboptimal=self.suboptimal,
                    feedmod=self.feedtype)

        impl = self.models[-1]
        specs = self.models[:-1]

        feed = F.generate(
            impl, specs, self.inter, ins=self.ins, args=self.args,
            ignoreio=self.ignoreio, ignoreret=self.ignoreret,
            cleanstrings=self.cleanstrings,
            entryfnc=self.entryfnc)

        if feed.status == Feedback.STATUS_REPAIRED:
            if self.maxfeedcost > 0 and feed.cost > self.maxfeedcost:
                self.error('max cost exceeded (%d > %d)',
                           feed.cost, self.maxfeedcost)
            for f in feed.feedback:
                print('*', f)
                
        elif feed.status == Feedback.STATUS_ERROR:
            self.error(feed.error)

        else:
            self.error(feed.statusstr())

    def guess_lang(self):
        '''
        Sets lang options from the first source file extension.
        '''

        if not len(self.sources):
            self.error('Cannot guess the language - no source files!')
            return

        file_parts = self.sources[0].rsplit('.', 1)

        if len(file_parts) < 2:
            self.error('Cannot guess the language - no file extension!')

        self.lang = file_parts[1]
        self.debug('Guessed language: %s', self.lang)

    def dump_exprs(self, model):
        '''
        Dumps additional expressions.
        '''
        
        exprs = []
        for fnc in model.getfncs():
            if not hasattr(fnc, 'repair_exprs'):
                continue
            rex = fnc.repair_exprs

            for loc in rex:
                for var in rex[loc]:
                    exprs.append({
                        "fnc": fnc.name,
                        "loc": loc,
                        "var": var,
                        "expr": expr_to_dict(fnc.getexpr(loc, var)),
                        "src": None,
                    })
                    for expr in set(rex[loc][var]):
                        exprs.append({
                            "fnc": fnc.name,
                            "loc": loc,
                            "var": var,
                            "expr": expr_to_dict(expr),
                            "src": expr.src,
                        })
                        
        ext = '.' + self.lang
        exprs_filename = model.name.replace(ext, '-exprs.json')
        with open(exprs_filename, 'w') as f:
            json.dump(exprs, f, indent=2)

    def extract_exprs(self, model):
        '''
        Loads additional expressions for the specification.
        '''
        ext = '.' + self.lang
        exprs_filename = model.name.replace(ext, '-exprs.json')
        if not os.path.isfile(exprs_filename): return
        with open(exprs_filename, 'r') as f:
            exprs = json.load(f)

        for expr_entry in exprs:
            fname = expr_entry['fnc']
            loc = expr_entry['loc']
            var = expr_entry['var']
            expr = dict_to_expr(expr_entry['expr'])
            expr.src = expr_entry.get('src')

            fnc = model.fncs[fname]

            if not hasattr(fnc, 'repair_exprs'):
                fnc.repair_exprs = {}

            rex = fnc.repair_exprs

            if loc not in rex:
                rex[loc] = {}

            if var not in rex[loc]:
                rex[loc][var] = []

            rex[loc][var].append(expr)

    def process_source(self, src):
        '''
        Reads and parses a single source file `src` and stets model fields.
        '''

        self.debug("Reading and parsing source file '%s'", src)
            
        with open(src, 'r', encoding="utf-8") as f:
            code = f.read()
            
        model = self.parser.parse_code(code)
        model.name = src
        self.extract_exprs(model)

        return model
            
    def process_sources(self):
        '''
        Reads and parses source files (sets models field).
        '''

        self.models = []

        for src in self.sources:
            model = self.process_source(src)
            self.models.append(model)
                

if __name__ == '__main__':
    try:
        clara = Clara()
        clara.main()
        sys.exit(0)
    except Exception as err:
        print('Error occured: %s' % (err,), file=sys.stderr)
        if VERBOSE:
            traceback.print_exc()
        sys.exit(1)
