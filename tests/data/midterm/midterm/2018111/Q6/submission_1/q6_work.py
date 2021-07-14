import pickle

def read_stations(f):
    count=0
    ans=dict()
    for i in f:
        i=i.strip()
        arr=i.split(', ')
        if count==0 or count%3==0:
            key=arr[0][1:-1]
            l=count
        if count==l+1:
            ans[key]=arr
        count+=1
    return ans

def get_stationline(mrt):
    ans=dict()
    for i in mrt:
        for n in mrt[i]:
            if not n in ans:
                ans[n]=[i]
            else:
                ans[n].append(i)
    return ans

def get_interchange(stationline):
    ans=dict()
    for i in stationline:
        if len(stationline[i])>1:
            ans[i]=stationline[i]
    return ans


  
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
    mrt = read_stations(f)
    mark1=None
    mark2=None
    for i in mrt:
        for n in range(len(mrt[i])):
            if mrt[i][n]==start:
                mark1=n
            if mrt[i][n]==end:
                mark2=n
        if not mark1==None and not mark2==None:
            ans=[]
            for z in range(mark1,mark2+1):
                ans.append(mrt[i][z])
            return ans
    return -1