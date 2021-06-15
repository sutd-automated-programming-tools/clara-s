import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    output = {}
    for i in mrt:
        if i[0] not in output:
            output[i[0]] = {}
        if i[1] not in output:
            output[i[1]] = {}
            
    for i in mrt:
        output[i[0]][i[1]] = 1
        output[i[1]][1[0]] = 1
        
    return output

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





#A
#def read_stations(f):
# create an empty dictionary for output
# read file f line by line using f.readlines()
# separate the file into key and item
#add the key with respect to the item in the output dictionary

#b
#def get_station(mrt):

#create an empty dictionary for output
#for every item in the dictionary, change it to a key:
#for every key in the dictionary change it to an item for that particular key:
#append to output dictionary
#return dictionary



#c
#def get_interchange(stationline)
#create an output dictionary
# for every key with more than 1 item, append to output dictionary

#d
#output = []
#for i between start and end+1
#append all the i to output
#return output