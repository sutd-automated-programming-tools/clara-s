import pickle

def read_stations(f):
    d = {"EastWestLine (EW)": [], "EastWestLine (CG)": [], "NorthSouthLine": []}
    reading_EW = False
    reading_NS = False
    reading_CG = False

    lines = f.readlines()

    for line in lines:
        formatted = line.strip()
        if formatted == "=EastWestLine (EW)=":
            reading_EW = True
            reading_CG = False
            reading_NS = False
        elif formatted == "=NorthSouthLine=":
            reading_NS = True
            reading_EW = False
            reading_CG = False
        elif formatted == "=EastWestLine (CG)=":
            reading_CG = True
            reading_EW = False
            reading_NS = False

        elif formatted != "\n":
            data = formatted.strip()
            data = data.split(", ")
            for i in data:
                if reading_EW:
                    d["EastWestLine (EW)"].append(i)
                elif reading_NS:
                    d["NorthSouthLine"].append(i)
                elif reading_CG:
                    d["EastWestLine (CG)"].append(i)
    return d

def get_stationline(mrt):
    line = {}
    for k in mrt:
        for i in mrt[k]:
            if i in line:
                line[i].append(k)
            else:
                line[i] = [k]
            
    return line

def get_interchange(stationline):
    output = {}
    for key in stationline:
        if len(stationline[key]) > 1:
            output[key] = stationline[key]
        else:
            pass
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
    
        stations_dict = get_stationline(read_stations(f))
    interchange = get_stationline(stations_dict)
    path = []
    
    #for both stations in one line
    for k in stations_dict.values():
        if start in k and end in k:
            index_start = stations_dict[k].index(start)
            index_end = stations_dict[k].index(end)
            for i in range(index_start, index_end+1):
                path.append(stations_dict[k][i])
                
        
        elif start in k and end not in k:
            firstline = stations_dict[k]
            index_start = stations_dict[k].index(start)
            for i in stations_dict:
                if end in i:
                    endline = stations_dict[i]
                    index_end = stations_dict[i].index(end)
                    for j in interchange:
                        if firstline in j and endline in j:
                            interchangestn.append(j)