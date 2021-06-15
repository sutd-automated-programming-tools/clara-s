import pickle

def read_stations(f):
    d = {}
    file = f.readlines()
    for line in file:
        if line[0] == "=":
            a = line.split("=")   #a = ['', 'linename', '']
            mrtline = a[1]
        else:
            lsofstation = line.split(",")
            lsofstation = [i.strip() for i in lsofstation]
            lsofstation = [i for i in lsofstation if i !=""]
            if d.get(mrtline) == None:
                d[mrtline] = lsofstation
            else:
                d[mrtline] += lsofstation
    return d




def get_stationline(mrt):
    d = {}
    for line, stations in mrt.items():
        for station in stations:
            if station in d.keys():
                d[station] += [line]
            else:
                d[station] = [line]
    return d





def get_interchange(stationline):
    d ={}
    for station, lines in stationline.items():
        if len(lines) > 1:
            d[station] = lines
    return d


  
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
    stationNlines = mrt_d
    stationNitslines = lines
    interchanges = interchange
    for line, stations in mrt_d:  #mrt_d is a dictionary
        if start in stations and end in stations:
            indexofstart = stations.index(start)
            indexofend = stations.index(end)
            return stations[indexofstart:indexofend+1]
        #pseudo code in comments
                #check the lines the start station is in using get_stationline()
                # if it is an interchange to lines n: (n is the other mrt lines that the start station is in) 
                #    if the end station is in lines n:
                #         return list of stations from start to end station in that other mrt line
                #    else:
                #         return None
                #check for the interchanges in the line the start station is in using a for loop through get_interchange() and read_stations()
                #    for all interchanges:
                #        if end station is in the other mrt lines of the interchange:
                #              return list of stations from start to interchange and interchange to endstation
                #        else:
                #              return None
                
    