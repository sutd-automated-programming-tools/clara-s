import pickle

def read_stations(f):
    lst=f.readlines()
    ans={}
    for i in lst:
        if "=" in i:
            name=i.strip("=")
            ans[name]=[]
        else:
            l=i.strip().split(",")
            for j in l:
                ans[name].append(j)
    return ans
    pass

def get_stationline(mrt):
    ans={}
    lines=mrt.keys()
    lst=[]
    stations=mrt.values()
    for i in stations:
        for j in i:
            lst.append(j)
    for k in lst:
        key=ans.keys()
        for h in lines:
            if k in mrt[h]:
                if k in key:
                    ans[k].append(h)
                else:
                    ans[k]=[h]
    return ans
    pass

def get_interchange(stationline):
    key=stationline.keys()
    for i in stationline.values():
        
        if len(i)==1:
            for j in key:
                if stationline[j]==i:
                    stationline.pop(j)
    return stationline
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