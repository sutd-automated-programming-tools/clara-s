import pickle

def read_stations(f):
    read_dict={}
    new_list = []
    EastWestLine_EW_list = []
    for i in f:
#        print (i)
        message = i.strip().split()
#        print (message)
        new_list.append(message)
#    print (new_list)
    EastWestLine_CG = False
    NorthSouthLine = False
    
    for j in new_list[1:]:
        if j[0] == "=EastWestLine":
            EastWestLine_EW = True
            NorthSouthLine = False
            EastWestLine_CG = False
            
            
        if EastWestLine_CG == False and NorthSouthLine == False:
            temp_list = []
            for k in j:
                temp_list.append(j)
            EastWestLine_EW_list.append(temp_list)
        
        if j[0] == "=NorthSouthLine=":
            EastWestLine_EW = False
            EastWestLine_CG = False
            
        if EastWestLine_EG == False and NorthSouthLine == False:
            temp_list = []
        
        
        read_dict["EastWestLine (EW)"] = EastWestLine_EW_list

def get_stationline(mrt):
    new_dict={}
    for i in mrt:
        for j in mrt.keys():
            new_dict[mrt[j]] = i 
    return new_dict

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