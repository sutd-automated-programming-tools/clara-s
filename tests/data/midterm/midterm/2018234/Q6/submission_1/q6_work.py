import pickle

def read_stations(f):
    dic = {}
    lines = f.readlines() # a list of all the lines inside the file 
    for i in lines: #read line by line 
        i = i.split() #splitting will result in 0,1,.. from 0 1
        small_list = (int(i[0]),int(i[1])) #creatinga new tuple in which the content is 0 1 
       #i is a list of 0 and 1 
        biglist.append(small_list)
    return biglist
result = get_nodes(f)
print (result)

def get_stationline(mrt):
    pass

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