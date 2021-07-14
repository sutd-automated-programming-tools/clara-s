import pickle

def read_stations(f):
    for line in f:
        output = dict()
        if line == "=EastWestLine (EW)=":
            continue

        if line == "=EastWestLine (CG)=":
            output["EastWestLine (EW)"] = stations
            stations = []
            continue


        if line == "=NorthSouthLine=":
            output["EastWestLine (CG)"] = stations
            stations = []



        else:
            
            stations = line.strip(',')
            stations = station.split(' ')

        output["NorthSouthLine"] = stations

    return output

ddef get_stationline(mrt):
    output = dict()
    for i in mrt: #for each key,
        station_list = mrt.get(i)
        for j in station_list: #for each station,
            if j not in output: #if station not in output,
                output[j] = i #put it in
            else:
                output[j] += i
    
    return output

def get_interchange(stationline):
    output = dict()
    for i in stationline:
        if len(stationline.get(i)) > 1:
            output[i] = stationline.get(i)
    return output


  
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
    