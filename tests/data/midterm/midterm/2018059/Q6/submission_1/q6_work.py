import pickle


f = open("mrt_lines_short.txt","r")   
def read_stations(f):
    dic = {}
    lst = []
    for line in f:
        if line in f == '=EastWestLine (EW)=\n':
            continue
        elif line in f == 'EastWestLine (CG)=\n':
            dic['=EastWestLine (EW)='] = lst
            lst = []
        elif line in f == '=NorthSouthLine=\n':
            dic['EastWestLine (CG)='] = lst
            lst = []
            x = line.strip('\n').split(',')
            lst.append(x)
            dic['=NorthSouthLine='] = lst
        else:
            x = line.strip('\n').split(',')
            lst.append(x)
    return dic

def get_stationline(mrt):
    dic = {}
    for entry in mrt:
        if entry 

def get_interchange(stationline):
    dic = {}
    for entry in stationline:
        if len(stationline[key]) > 1:
            dic[key] = 
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