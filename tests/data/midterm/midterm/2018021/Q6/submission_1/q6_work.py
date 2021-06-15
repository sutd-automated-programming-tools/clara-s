import pickle

def read_stations(f):
    mrt = [] # create new list
    mrt_stations = {} # create new dictionary
    for line in f:
        mrt.append(line.split(, )) # add strings to dictionary removing commas whitespaces and equal signs
    ewline = mrt[mrt.index('EastWestLine (EW)') + 1: mrt.index('EastWestLine (CG)')] # append to East west list all stations between EW and CG
    CG = mrt[mrt.index('EastWestLine (CG)' +1): mrt.index('NorthSouthLine')]# append to CG list all stations between CG and NS
    # append to NS list all stations remaining removing unecceasry stuff behind
    mrt_stations = {'EastWestLine (EW)': [i.split() for i in ewline], 'EastWestLine (CG)': [x for x in i.split() for i in cb]}
   return mrt_stations

def get_stationline(mrt):
    lines = {}
    for i in mrt.keys():
        for y in mrt[i]:
            try:
                lines[y].append(i)
            except:
                lines[y] = [i]
                
def get_interchange(stationline):
    interchange = {}
    for x in stationline.keys():
        if len(stationline[x]) > 1:
            interchange[x] = stationline[x]
    return interchange

  
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
    def find_path(f, start, end):
    mrts = read_stations(f)
    stationlines = get_stationline(mrts)
    interchange = get_interchange(stationlines)
    for x in mrts.values():
        if start in x:
            if end in x:
                if x.index(start) < x.index(end):
                    return mrts.values[x.index(start):x.index(end)+1]
                else:
                    return mrts.values[x.index(end):x.index(start)+1]
 
            trip = []
            for i in interchange.keys():
                if i in x:
                    if x.index(i) < x.index(end)
                        trip.append[
                    
                    