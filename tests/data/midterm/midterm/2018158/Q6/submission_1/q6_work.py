import pickle

def read_stations(f):
    dic = {}
    for line in f:
        lst = line.strip().split(",")
        if len(lst) < 2:            #lst of line name
            curr_colourline = lst[0]
        if len(lst) > 1:            #it is a lst of stations)
            dic[curr_colourline] = lst    #pairs my lst which is of all stations to the current colour line eg. ew
    return dic

def get_stationline(mrt):
    new_dict = {}
    for key in mrt.keys():    #will return me all the key one by one
        lst = mrt[key]
        for stations in lst:
            new_dict[stations] = key
    return new_dict

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