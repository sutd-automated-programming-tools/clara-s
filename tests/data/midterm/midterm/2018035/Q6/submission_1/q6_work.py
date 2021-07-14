import pickle

def read_stations(f):
    dic = {}
    x = 1
    for line in f:
        #print(line)
        if x == 1 or x == 4 or x == 7:
            a = line[1:(len(line)-2)]
            dic[a] = 0
            x += 1
        elif x == 3 or x == 6:
            x+=1
        elif x == 8: 
            dic[a] = line[0:len(line)].split(", ")
            x+=1
        else: 
            dic[a] = line[0:len(line)-1].split(", ")
            x+=1
    return dic
            

def get_stationline(mrt):
    newdic = {}
    for key in mrt:
        for i in mrt[key]:
            if i in newdic == True:
                newdic[i].append(key)
            else:
                newdic[i] = [key]
    return newdic

def get_interchange(stationline):
    nwdic = {}
    for key in stationline:
        if len(stationline) >= 2:
            nwdic[key]=stationline[key]
    return nwdic


  
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