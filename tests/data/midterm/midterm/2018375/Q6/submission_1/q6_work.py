import copy
import pickle

def read_stations(f):
    all_lines = f.readlines()
    new_ls = []
    for i in range(len(all_lines)):
        new_line = all_lines[i].strip("\n")
        spl_line = new_line.split(", ")
        if spl_line == [""]: #dont append "" into the ls
            continue
        new_ls.append(spl_line)
    dct = {}
    for i in range(len(new_ls)):
        for j in range(len(new_ls[i])):
            if new_ls[i][j] in ["=EastWestLine (EW)=","=EastWestLine (CG)=",
                      "=NorthSouthLine="]:
                x = new_ls[i][j].strip("=")
                dct[x]= []
            else:
                dct[x].append(new_ls[i][j])
    return dct


def get_stationline(mrt):
    st_dct = {}
    for key in mrt:
        for values in mrt[key]:
            if values in st_dct: #avoid removing the initial key
                st_dct[values].append(key)
            else:
                st_dct[values] = [key]
    return st_dct

def get_interchange(stationline):
    st_copy = copy.copy(stationline)
    int_dct = {}
    for key in stationline:
        if len(stationline[key]) > 1:
            int_dct[key] = st_copy[key]
    return int_dct


def find_path(f, start, end):
    mrt_line = read_stations(f)
    st_line = get_stationline(mrt_line)
    st_int = get_interchange(st_line)
    first_line = st_line[start]
    last_line = st_line[end]
    if first_line == last_line:
        x = mrt_line[first_line[0]]
        path = []
        if x.index(start) < x.index(end):
            for i in range(x.index(start),x.index(end)+1):
                path.append(x[i])
            return path
        else:
            for i in range(x.index(end),x.index(start) +1):
                path.append(x[i])
            new_path = []
            for i in range(len(path)):
                new_path.append(path[len(path) - i - 1])
            return new_path
    elif start in st_int and end in st_int:
        return None

  
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