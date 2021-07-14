import pickle

def read_stations(f):
    dd={}
    #create a list with line and stations occur in alternative manner
    my_list=f.readlines()
    for item in my_list:
        item.strip()
    length=len(my_list) 
    for i in range(length-1):
        if i%2 == 0:
            dd[ls[i]]=ls[i+1]
    return dd

def get_stationline(mrt):
    dd= read_stations(f)
    new_dd={}
    outlist=[]
    for (line,stations) in dd.items():
        if mrt in stations:
            outlist.append(line)
    new_dd[mrt]=outlist
    return new_dd
    

def get_interchange(stationline):
    oldbee={]
    for (stations,line) in stationline.items():
        if len(line) >2:
            oldbee[stations]=line
    return oldbee
    


  
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