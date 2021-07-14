import pickle

def read_stations(f):    
    i = 0
    final_dictionary = {"EastWestLine(EW)":[],"EastWestLine(CG)":[],"NorthSouthLine":[]}
    for line in f:
        a_line = line.strip().split(",")
        i += 1 
        if i == 2:
            x = list(a_line)
            for element in x:
                    final_dictionary["EastWestLine(EW)"].append(element)
        if i == 4:
            for element in x:
                final_dictionary["EastWestLine(CG)"].append(element)
        if i == 6:
            for element in x:
                final_dictionary["NorthSouthLine"].append(element)
    return final_dictionary


def get_stations(mrt):
    new_dict = {}
    for keys in mrt: #asses the mrt lines 
        for places in keys:
            new_dict[places] = keys
    return new_dict

print(get_stations(read_stations(f)))

def get_interchange(stationline):
    interchange = {'Tanah Merah':["EastWestLine (EW)","EastWestLine (CG)"],"City Hall":["EastWestLine (EW)","NorthSouthLine"],"Raffles Place":["EastWestLine (EW)","NorthSouthLine"],"Jurong East":["EastWestLine (EW)","NorthSouthLine"]}
    return interchange



  
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