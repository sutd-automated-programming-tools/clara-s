import pickle

def read_stations(f):
    dic = {}
    for line in f:
        if line[0] == '=':
            key = line.replace('=','').strip()
        elif line != '\n':
            line = list(line.strip().split(','))
            line2 = list(x.strip() for x in line)
            print(line2)
            dic[key] = line2
    return dic

def get_stationline(mrt):
    abc = list(mrt.items())
    dic = {}
    #print(abc)
    for a in abc:
        for b in a[1]:
            if b not in dic:
                dic[b] = [a[0]]
            #else:
                #lst = dic[b].append(a[0])
                #print(dic[b])
                #print(a[0])
                #print(lst)
                #dic[b] = lst
    print(dic)
    return dic

def get_interchange(stationline):
    dic = {}
    for keys in  stationline:
        if len(stationline[keys]) != 1:
            dic[keys] = stationline[keys]
    return dic

def find_path(f,start,end):
    maindic = read_stations(f)
    linedic = get_stationline(maindic)
    intdic = get_interchange(linedic)
    # if both mrt are on the same line, find get the index of the station in read_station(f)
    # if both mrt are not on the same line, find a station in line 1 that have a interchange of both sations 
    for key in line:
        if start in linedic[key]:
            a = line
        if end in linedic
  
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