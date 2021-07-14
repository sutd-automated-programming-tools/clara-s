import pickle
import os
os.getcwd()
f = open('mrt_lines_short.txt','r')

def read_stations(f):
    mrtMapped=dict()
    f = f.readlines()
    for line in f:
        line_stations = list(x.strip() for x in line.split(","))
        line = line_stations.pop(0)
        mrtMapped[line]=line_stations
        
    return mrtMapped
            
          
def get_stationline(mrt):
    lineStationsMapped = dict()
    fileContent = f.readlines()

    for i in range(len(fileContent)):
        line_stations = fileContent[i].strip().split(",")
        line = line_stations.pop(0)
        lineStationsMapped[line] = lines_stations

        return lineStationsMapped

def get_interchange(stationline):
    


  
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