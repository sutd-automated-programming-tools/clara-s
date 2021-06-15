import pickle

def read_stations(f):
    answer_dict = {}
    for line in f:
        string = line.strip()
    
    
    def create_graph(nodes):
    holding_dict = {}
    for i in nodes:
        if i[0] in holding_dict.keys():
            holding_dict[i[0]][i[1]] =1 #just append to internal dictionary
        else:
            holding_dict[i[0]] = {} #create an empty dictionary inside holding_dict, with the node name as key.
            holding_dict[i[0]][i[1]]=1 #access that dictionary, then assign the friend name as a key with value 1.


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