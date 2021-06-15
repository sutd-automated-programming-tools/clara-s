import pickle

def read_stations(f):
    outputDict={}
    x = f.read()
    splitx = x.split('\n')
    #splitx.remove('')
    for i in range(len(splitx)):
        if splitx[i][0]=='=':
            outputDict[splitx[i][1:-1]]=splitx[i+1]
    """
    convert file into one string
    split string into lists with '\n'
    as long as the first character of each element is '=', that would be a name of a line. take the [1:-1] of the line name (as dictionary element name), and the next element (as dictionary element value)
    finally, take the values of all dictionary element and split with ','.
    
    """

def get_stationline(mrt):
    outputDict = {}
    for lines in mrt:
        for stations in mrt[lines]:
            if (stations in outputDict):
                outputDict[stations].append(lines)
            else:
                outputDict[stations]=[lines]
    return outputDict

def get_interchange(stationline):
    outputDict = {}
    for stations in stationline:
        if len(stationline[stations])>1:
            outputDict[stations] = stationline[stations]
    return outputDict


  
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
    """
    Check if start and end belong in the same list within a dictionary element. If so, return this path by taking index(start) and index(end) and append all elements in betweeen into a list for output
    
    if not, 
    """
    pass