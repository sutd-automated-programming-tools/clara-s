import pickle

def read_stations(f):
    d={'EastWestLine(EW)':valuesa,'EastWestLine (CG)': valuesc, "NorthSouthLine": valuesb }
    valuesa= read_stationsa(f)
    valuesb=read_stationsb(f)
    valuesc=read_stationc(f)


def read_stationsa(f):
    f=open('mrt_lines_short.txt','r')
    
    lines=f.readlines()[1:4]
    for line in lines:
        valuesa=line.split(",")
        print(valuesa) 
#         values=values.strip 
#         a.append(values)
#     f=open('mrt_lines_short.txt','r')
    
#     lines=f.readlines()[8:11]
#     b=[]
#     for line in lines:
#         valuesb=line.split(",")
#         print(valuesb)
# #         b.append(values)
    
    return valuesa


def read_stationsb(f):
    f=open('mrt_lines_short.txt','r')
    lines=f.readlines()[9:11]
    print(lines)
  
    for line in lines:
        valuesb=line.split(",")
        print(valuesb)
        
    return valuesb 


def read_stationsc(f):
    f=open('mrt_lines_short.txt','r')
    lines=f.readlines()[6:6]
    print(lines)
   
    for line in lines:
        valuesc=line.split(",")
        
        
    return valuesc


def get_stationline(mrt): 
    d={}
    for line,stations in mrt.items(): # gives the list of stations in each line and also the line 
        for s in stations: 
            d[s]= [line] 
    return d 
            


def get_interchange(stationline):
    dnew={}
    for station, line in get_station(mrt): 
        if len(line)>1: 
            dnew[station]=line
    return dnew 


  
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