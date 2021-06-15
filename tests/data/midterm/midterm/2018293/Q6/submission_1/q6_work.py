import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    pass
def get_interchange(stationline):
    dictionary = {}
    for i in stationline :
        values = stationline[i]
        if len(values) > 1:
            dictionary[i] = values
    return dictionary

def get_interchange(stationline):
    pass
def get_stationline(mrt):
    dictionary = {}
    new_list = []
    for i in mrt.values():
        for j in i:
            if j not in dictionary:
                dictionary[j] = {}
            if j in dictionary:
                for k in mrt :
                    if j in mrt[k]:
                        new_list.append(k)
                        dictionary[j]= new_list 
                new_list = []
    return dictionary
def read_stations(f):
    #print(f.readlines)
    mini_list = []
    data = f.readlines()
  #  for  in data :
  #      new_data = i.split()
  #  print(data)    
    dict = {}
    for station in data:
        new_station = station.strip('\n')
        new_station = new_station.strip('=') # rmb to give a name like new_station to the action u performed, otherwise the method won'be updated
        new_station = station.split(",") # rmb to use this to separate them by the , in between instead of just split() bcos split() remove white spaces
       # print(new_station) # once u apply split, it become a list so no need to use mini_list.append
       # print(type(station))
#        print(mini_list)
        #single_station = station.strip()
        dict[new_station[0]] = []
        for location in new_station[1::] :
            dict[new_station[0]].append(location)
    return dict
  
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