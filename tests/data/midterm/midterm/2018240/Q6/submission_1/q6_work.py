import pickle

def read_stations(f):
    dict={}
    linesname=['=EastWestLine (EW)=','=EastWestLine (CG)=', '=NorthSouthLine=']
    for line in f:
        x=line.strip().split(', ')
        for i in x:     
            if i in linesname:
                lst=[]
                dict[i]=lst
            elif i not in linesname:
                lst.append(i)
    return dict

def get_stationline(mrt):
    mrt=read_stations(f)
    dict={}
    for key in mrt:
        if key=='NorthSouthLine':
            for value in mrt[key]:
                dict[value]="NorthSouthLine"
        if key=='EastWestLine (EW)':
            for value in mrt[key]:
                dict[value]="EastWestLine (EW)"
        if key=='EastWestLine (CG)':
            for value in mrt[key]:
                dict[value]="EastWestLine (CG)"
                
    return dict

def get_interchange(stationline):
    dict={}
    stationline=get_stationline(mrt)
    for key in stationline:
        lst=stationline[key]
        if len(lst)>1:
            dict[key]=lst
    
    return dict

def find_path(f,start,end):
    for key in f:
        if start in f[key]:
            position1=f[key].index(start)
            position2=f[key].index(end)
            lst=f[key][position1:position2]
    return lst

  
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