import pickle

def read_stations(f):
    lines=f.read()
    a=lines.split('\n')
    dic={}
    for i in a:
        if i=='':
            a.remove('')
    dic2={}
    for i in range(0,len(a)-1,2):
        dic[a[i]]=a[i+1].split(', ')
    for k,v in dic.items():
        dic2[k[1:len(k)-1]]=v
        

    return dic2
def get_stationline(mrt):
    out={}
    for k,v in mrt.items():
        
        for i in v:
            
            n=out.get(i,[])
            n.append(k)
            out[i]=n
            
    return out

def get_interchange(stationline):
    out={}
    for k,v in stationline.items():
        if len(v)>1:
            out[k]=v
    return out


  
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