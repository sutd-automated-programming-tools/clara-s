import pickle
f=open('mrt_lines_short.txt','r')
def read_stations(f):
    f.read()
        ls=x.split('\n')
    ls1=[]
    vaue=[]
    dic={}
    for i in ls:
        if len(i)==0:
            pass
        else:
            ls1.append(i.strip('='))

    for i in ls1:
        if i in ['EastWestLine (EW)','EastWestLine (CG)','NorthSouthLine']:
            key=i
            value=[]
        else:
            value.append(i)
            dic[key]=value
    for i in dic:
        dic[i]=dic[i][0].split(', ')
    return dic

def get_stationline(mrt):
    dic={}
    ls=[]         
    for i in mrt:#i=mrt line
        for j in mrt[i]:#mrt stop
            ls.append(i)
            dic[j]=ls
            ls=[]
    for i in dic:
        for j in dic:
            if i==j:
                dic[i]
    return dic

def get_interchange(stationline):
    dic={}
    for i in stationline:
        if len(stationline[i])>1:
            dic[i]=stationline[i]
    return dic  
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