import pickle

#f = open("mrt_lines_short.txt", "r")

g = open("mrt_lines_short.txt", "r")
f = g.readlines()
def read_stations(f):
    dickydict = {}
    service = ''
#    lines = f.readlines
    for line in f:
        formattedLine = line.strip()
        if "Line" in formattedLine:
            service = formattedLine.strip('=')
            dickydict[service] = []
        elif "Line" not in service:
            station = formattedLine.split(' ')
            dickydict[service].append(station)
    return dickydict
#UGH why doesnt this work

print(read_stations(f))



def get_stationline(mrt):
    newdict = {}
    for value in mrt:
        newdict[value] = mrt[value]
    return newdict
        

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