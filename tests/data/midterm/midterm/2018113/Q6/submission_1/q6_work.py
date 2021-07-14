import pickle

def read_stations(f):
    file = open(f,'r')
    lines = file.readlines()
    dict = {}
    lis = ['=EastWestLine (EW)=', '=EastWestLine (CG)=' ,'=NorthSouthLine=']
    for line in lines:
        if line in lis:
            dict.setdefault(line,[])
            temp = line
            continue
        dict[line].append(line.strip().split(', '))
    return dict

def get_stationline(mrt):
    output = {}
    for x in mrt.keys():
        for i in mrt[x]:
            if i not in output.keys():
                output[i] = []
            output[i].append(x)
    return output

def get_interchange(stationline):
    output = {}
    for key in stationline:
        if len(stationline[key]) > 1:
            output[key] = stationline[key]
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
    mrt_d = read_station()
    lines = get_stationline()
    interchange = get_interchange()
    for key in mrt_d:
        if start in mrt_d[key] and end in mrt_d[key]:
            return mrt_d[key][mrt_d[key].index(start):mrt_d[key].index(end)]
    lis1 = lines[start]
    lis2 = lines[end]
    for i in lis1:
        if i in lis2:
            temp = i
            return 