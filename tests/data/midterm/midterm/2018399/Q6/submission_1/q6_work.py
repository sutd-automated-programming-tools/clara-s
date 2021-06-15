import pickle

def read_stations(f):
    output = {}
    File_list = []
    data_list = []
    for line in f:
        File_list.append(line.split())
    pass


def get_stationline(mrt):
    output = {}
    for key,lst in mrt.items():
        for i in lst:
            if i not in output:
                output[i] = [key]
            else:
                output[i] += [key]
    return output

def get_interchange(stationline):
    output = {}
    for key, lst in line:
        for i in lst:
            if i == stationline and len(lst) < 1:
                output[key] = lst
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
    pass