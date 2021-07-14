import pickle

def read_stations(f):
    result={}
    result['EastWestLine (EW)']=[]
    result['EastWestLine (CG)']=[]
    result['NorthSouthLine']=[]
    for i in f:
        if i=='=EastWestLine (EW)=':
            break
    for i in f:
        a=i.strip()
        b=a.split(',')
        result['EastWestLine (EW)'].append(b)
        if i=='=EastWestLine (CG)=':
            break
    for i in f:
        a=i.strip()
        b=a.split(',')
        result['EastWestLine (CG)'].append(b)
        if i=='=NorthSouthLine=':
            break
    for i in f:
        a=i.strip()
        b=a.split(',')
        result['NorthSouthLine'].append(b)
    return result
        
        
    
    
    
        
    

def get_stationline(mrt):
    dict1={}
    for i in mrt:
        for j in i:
            if j not in dict1:
                dict1[j]=[]
            else:
                dict1[j].append(i)
    return dict1
                
  
def get_interchange(stationline):
    dict2={}
    for i in stationline:
        if len(stationline[i])>1:
            dict2[i].append(stationline[i])
    return dict2
    


  
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
    a=read_stations(f)
    dict1=get_stationline(a)
    dict2=get_interchange(dict1)
    num=0
    route=[]
    for i in a:
        if start in a[i]:
            index=a[i].index(start)
            b=i
        if end in a[i]:
            index2=a[i].index(end)
    if end in a[b]:
        return a[b][index:index2+1]
    
        
     
    
    
            