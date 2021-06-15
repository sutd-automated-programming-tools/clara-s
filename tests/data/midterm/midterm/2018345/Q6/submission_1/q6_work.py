import pickle

def read_stations(f):
    
    dic={"EastWestLine (EW)":[],"NorthSouthLine":[]}
    
    for aline in islice(f,2,3):
        values=aline.split()
        dic["EastWestLine (EW)"]+=values
    for aline in islice(f,5,6):
        values=aline.split()
        dic["EastWestLine (CG)"]+=values
        
    for aline in islice(f,8,9):
        values=aline.split()
        dic["NorthSouthLine"]+=values
    return dic
    

def get_stationline(mrt):
    mrt=read_stations(f)
    dicc={}
    for i in mrt:
        for item in i:
            dicc[i[item]=[i]
    return dicc

def get_interchange(stationline):
    stationline = get_stationline(mrt)
    new_dic={}
    for i in stationline:
        if len(stationline[i])>1:
                 new_dic[i]=stationline[i]
        else:
            new_dic[i]=0
    return new_dic


  
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
    f=
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass