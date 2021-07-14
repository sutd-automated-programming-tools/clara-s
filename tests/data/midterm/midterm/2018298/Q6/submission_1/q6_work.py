import pickle

def read_stations(f):
    
    Dict = {}
    Header = ''
    MRTLines = []
    
    while True:
        lines = f.readline()
        if lines == '':
            break 
    
        lines = lines.split()
    
        if lines[0].lstrip():
            Header = lines[0].strip()
            MRTLines = []
            
        elif lines[0].isalpha():
            lines = tuple(i for i in lines)
            MRTLines.append(lines)
            Dict[Header] = MRTLines
        
    return Dict 


def get_stationline(mrt):
    pass

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