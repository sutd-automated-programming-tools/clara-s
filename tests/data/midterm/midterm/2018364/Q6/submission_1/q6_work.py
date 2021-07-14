import pickle

def read_stations(f):
    ls = list(f)
    #print (ls)
    temp = []
    temp2 = []
    for i in ls:
        if '=' not in i:
            temp = i.split(',')
            temp2.append(temp)
    #print(temp)
    #print('\n')
    #print (temp2)
    ans= {}
    ans[ls[0]]= temp2[0]
    ans[ls[2]]= temp2[2]
    ans[ls[4]]= temp2[4]
    #print('\n')
    #print (ans)
    return(ans)

def get_stationline(mrt):
    ans = {}
    for i in mrt:
        #print (i)
        #print (len(mrt[i]))
        for j in mrt[i]:
            #print (j)
            a = []
            a.append(i)
            ans[j] = a
            
    return (ans)
            
        #ls = list(i.keys())
        #print (ls)

def get_interchange(stationline):
    
    ans = {}
    
    for i in stationline:
        if len(stationline[i])> 1:
            ans[i] = stationline[i]
    return (ans)
        


  
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