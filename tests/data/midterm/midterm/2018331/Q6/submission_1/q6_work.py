import pickle

def read_stations(fid):
    stationdict={}
    counter=-1
    for f in fid:
        if f[0] == '=':
#            print(f[0])
            linename=f.strip('=').strip('=\n')
            stationdict[linename]=[]
            counter=linename
        line=f.strip().split(',')
        for i in line:
            i=i.strip()
            stationdict[counter].append(i)
    for key in stationdict:
        del stationdict[key][0]
    
    return stationdict

#print(read_stations(fid1))

#parta=read_stations(fid1)

def get_stationline(dictmrt):
    linelist=[]
    stationlinedict={}
    for key in dictmrt:
        for mrt in dictmrt[key]:
#            print(mrt)
            if mrt not in stationlinedict:
                stationlinedict[mrt]=[]
            stationlinedict[mrt].append(key)
            
    return stationlinedict

#partb=get_stationline(parta)
#print(get_stationline(dictmrtlines))

def get_interchange(partb):
    interdict={}
    for key in partb:
        if len(partb[key])>1:
            interdict[key]=partb[key]
            
    return interdict


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
    parta=read_stations(f)
    partb=get_stationline(parta)
    partc=get_interchange(partb)
    startposkey='idk'
    startposind=1
    endposkey='idkeither'
    startposind=1
    for keys in partb:
        for i in range(len(partb[keys])):
            if partb[keys][i]==start:
                startposkey=keys
                startposind=i
            if partb[keys][i]==end:
                endposkey=keys
                endposind=i
    if endposkey==startposkey:
        return partb[startposkey][startposind:endposind]
    elif endposkey!=startposkey:
        return None