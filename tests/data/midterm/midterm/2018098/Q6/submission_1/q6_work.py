import pickle

def read_stations(f):
    mrt_line = []
    station_list = []
    ans = {}
    count = 0
    for i in f:
#        print (i.strip().split(', '))
        if i[0][0] == '=':
            mrt_line.append(i.replace('=', '').strip())
        if count == 1 or count == 4 or count == 7:
            station_list.append(i.strip().split(', '))
        count += 1
#    print (station_list)
    for i in range(len(mrt_line)):
        ans[mrt_line[i]] = station_list[i]
        
    return ans

def get_stationline(mrt):
    ans = {}
    for line, station in mrt.items():
#        print ([line])
        for i in station:
            ans[i] = [line]
    count = {}
    for newstation, newline in ans.items():
        if newstation in count:
            count[newstation] += 1
        if newstation not in count:
            count[newstation] = 1
        
    return ans

def get_interchange(stationline):
    ans = {}
    count = {}

    for newstation, newline in ans.items():
        if newstation in count:
            count[newstation] += 1
        if newstation not in count:
            count[newstation] = 1
    
    interchange = []
    for station, counts in count.items():
        if count > 1:
            interchange.append(station)
    return ans


  
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