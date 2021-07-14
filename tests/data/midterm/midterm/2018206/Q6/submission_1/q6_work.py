import pickle
import copy


def read_stations(f):
    x = {"EastWestLine (EW)":0, 'NorthSouthLine' : 0, "EastWestLine (CG)":0 }
    lst = []
    c = 1
    
    for i in f:
        if "Pasir Ris" in i:
            y = copy.deepcopy(i) 
            lst.append(i)
        if "Bukit Batok" in i:
            y = copy.deepcopy(i)
            lst.append(i)
        if "Expo" in i:
            y = copy.deepcopy(i)
            lst.append(i)
    for j in lst:

        if "\n" in j:
            j.replace('\n', '')
        j.split(',')
        j.strip()
        if "Pasir Ris" in j:
            x["EastWestLine (EW)"] = j
        if "Bukit Batok" in j:
            x["NorthSouthLine"] = j
        if "Expo" in j:
            x["EastWestLine (CG)"] = j
    
            
    return x




def get_stationline(mrt):
    x = {}
    

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