import pickle

def read_stations(f):
    d = {}
    ls = []
    ls2 = []
    lines = f.readlines()
    print(lines)
    for j in range(len(lines)):
        lines[j] = lines[j].strip('\n')
    for j in lines:
        if j == '':
            continue
        else:
            ls.append(j)
    for j in range(len(ls)):
        ls[j] = ls[j].strip('=')
    for j in ls:
        ls2.append(j.split(','))
    for j in ls2:
        pass

def get_stationline(mrt):
    pass

def get_interchange(stationline):
    pass


  
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