import pickle

def read_stations(f):
    op = {}
    ls = []
    a = f.readlines()
    for l in a:
        if l[0] == '=':
            op[l.strip('=\n')] = ls
#            ls=[]
            continue
        elif l[0] == '-':
            op[l[0]] = ls
#            ls = []
            continue
        lol = l
        lol = lol.strip('\n')
#        lol = lol.replace(',', '')
        lol = lol.split(',')
        for i in lol:
            ls.append(i.strip())
        for i in ls:
            if i == '':
                ls.remove(i)
        ls = []
    return op




def get_stationline(mrt):
    op = {}
    
    for line in mrt:
        for stat in mrt[line]:
            op.setdefault(stat,[line])
            if line not in op[stat]:
                op[stat].append(line)
            
    return op

def get_interchange(stationline):
    op = {}
    for i in stationline:
        if len(stationline[i]) > 1:
            op.setdefault(i, stationline[i])
    return op


  
##### Testing get_stationline ###########
with open('stations_short.pickle','rb') as f:
    mrt_d = pickle.load(f)
    print(get_stationline(mrt_d))
#########################################

##### Testing get_interchange ###########
with open('lines_short.pickle','rb') as f:
    lines = pickle.load(f)
    print(get_interchange(lines))
#########################################

###### Testing find_path ################
# You can use these three variables in your find_path
# to get the output of
# mrt_d = read_station()
# lines = get_stationline()
# interchange = get_interchange()
# even if you haven't finished these three functions
#########################################
def find_path(f,start,end):
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass