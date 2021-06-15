import pickle

def read_stations(f):
    counter=0
    dic={}
    for line in f:
        if counter<2:
            counter+=1
        else:
            elements=line.split()
            dic[elements[0]]=float(elements[1])
    return dic
   

def get_stationline(mrt):
    mrt=list(mrt)
             
    dic={}
    for i in range(len(mrt)):
        for j in range(len(mrt[i])):
            dic[mrt[i][j]]=mrt[i]
    return dic
            

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