import pickle

def read_stations(f):
    lines = f.readlines()
    maindict ={}
    stations1 = []
    stations2 = []
    stations3 = []
    for line in lines:
        #remove white spaces from line
        formatted = line.strip()
        mrtline1 = False
        mrtline2 = False
        mrtline3 = False
        if formatted == "=EastWestLine (EW)=":
            formatted_line = formatted.strip('=')
            mrtline1 = True
            mrtline2 = False
            mrtline3 = False
        elif formatted == "=EastWestLine (CG)=":
            formatted_line = formatted.strip('=')
            mrtline1 = False
            mrtline2 = True
            mrtline3 = False
        elif formatted == "=NorthSouthLine=":
            formatted_line = formatted.strip('=')
            mrtline1 = False
            mrtline2 = False
            mrtline3 = True
        else:    
            if mrtline1:
                stops = formatted_line.split(',')
				   # Convert to string
                station1 = [str(x) for x in stops]
                #stations1.append(station1)
            elif mrtline2:
                stops = formatted_line.split(',')
				   # Convert to string
                station2 = [str(x) for x in stops]
                stations2.append(station2)
            elif mrtline3:
                stops = formatted_line.split(',')
				   # Convert to string
                station3 = [str(x) for x in stops]
                stations3.append(station3)
    maindict['EastWestLine (EW)'] = stations1
    #maindict = {'EastWestLine (EW)': stations1, 'EastWestLine (CG)': stations2, 'NorthSouthLine':stations3}
    return maindict

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