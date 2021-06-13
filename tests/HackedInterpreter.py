# override the interpreter used by clara
# to sub in for math_sqrt
from claraplus.clara.py_interpreter import (
    PyInterpreter, VAR_OUT, VAR_RET, UndefValue
)
from claraplus.clara.interpreter import Program
from claraplus.clara import matching

import traceback
import random
import time
import math


# Program = PyInterpreter.Program


class HackedInterpreter(PyInterpreter):
    def run(self, prog, mem=None, ins=None, args=None, entryfnc=None):
        """
        this check fails, so I've had to remove it
        otherwise, all the code in this method is the same as in clara

        Apparently the reason it fails is because I have two
        clara folders in my UROP project folder, and when claraplus tries
        to import the Program it loads them from my original clara
        folder instead.

        if not isinstance(prog, Program):
            # print(type(prog), Program)
            # <class 'clara.model.Program'>
            # <class 'claraplus.clara.model.Program'>
            raise Exception("Expected Program, for '%s'" % (prog,))
        """

        self.prog = prog

        # Get function
        entryfnc = entryfnc or self.entryfnc
        try:
            fnc = prog.getfnc(entryfnc)
        except KeyError:
            raise RuntimeErr("Unknown function: '%s'" % (entryfnc,))

        # Init memory
        if mem is None:
            mem = dict()

        # Init trace
        self.trace = []

        # Set inputs
        if ins:
            mem[VAR_IN] = list(ins)
        # Set output
        if VAR_OUT not in mem:
            mem[VAR_OUT] = ''
        # Set var
        mem[VAR_RET] = UndefValue()

        # Init all vars to Undef
        for (var, _) in list(fnc.types.items()):
            if var not in mem:
                mem[var] = UndefValue()

        # Set args for the function
        if args:
            if len(args) != len(fnc.params):
                raise RuntimeErr(
                    "Wrong number of args: expected %s, got %s" % (
                        len(fnc.params), len(args)))
            for (var, t), a in zip(fnc.params, args):
                mem[var] = self.convert(a, t)

        self.starttime = time.time()

        res = self.execute(fnc, mem)
        self.prog = None
        return res

    def execute_Op(self, op, mem):
        if op.name in self.UNARY_OPS:
            if len(op.args) != 1 and op.name not in self.BINARY_OPS:
                raise RuntimeError(
                    "Got <>1 args for binary op in '%s'" % (op,))
            if len(op.args) == 1:
                return self.execute_UnaryOp(op.name, op.args[0], mem)

        if op.name in self.BINARY_OPS:
            if len(op.args) != 2:
                raise RuntimeError(
                    "Got <>2 args for binary op in '%s'" % (op,))
            return self.execute_BinaryOp(op.name, op.args[0], op.args[1], mem)

        if op.name == '[]':
            return self.execute_ArrayIndex(op, mem)

        # intercept unary op
        # print(f'OPNAME', type(op), op.name)
        if op.name in ('math_sqrt', 'sqrt'):
            assert len(op.args) == 1
            sub_op = op.args[0]

            # print('SUBOPNAME', op, mem)
            # execute any inner expressions
            # e.g. the 3*x in math.sqrt(3*x)
            # usually the inner expression is just a constant
            sub_op_result = self.execute_Op(sub_op, mem)
            # manually sqrt the result of the inner operation
            result = math.sqrt(sub_op_result)
            return result

        try:
            # meth = self.execute_math_sqrt
            meth = getattr(self, 'execute_%s' % (op.name,))
            return meth(op, mem)
        except Exception as e:
            print(f'OPNAME', type(op), op.name)
            raise e

    def execute_FuncCall(self, f, mem):
        """
        sometimes math.sqrt is treated as a function call
        in clara, rather than an operation
        """
        name = f.args[0].name

        if name == 'sqrt':
            # execute inner expression
            inner = self.execute(f.args[1], mem)
            # manually sqrt the result of the inner operation
            return inner ** 0.5

        else:
            return super().execute_FuncCall(f, mem)
