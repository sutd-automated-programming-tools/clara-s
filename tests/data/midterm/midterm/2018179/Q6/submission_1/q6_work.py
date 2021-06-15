import pickle

def read_stations(f):
    f = f.readlines()
    f = [i.strip() for i in f]
    #print(f)
    line_lst = []
    station_lst = []
    for i in f:
        if '=' in i:
            x, y, z = i.split('=')
            line_lst.append(y)
        else:
            station_lst.append(i)
    #print(line_lst)
    while '' in station_lst:
        station_lst.remove('')
    
    d = {}
    for k in range(len(line_lst)):
        for m in station_lst[k]:
            stations = station_lst[k].split(', ')
        d[line_lst[k]] = stations
    return d
          

def get_stationline(mrt):
    line_lst = mrt.keys()
    stations_lst = mrt.values()
    
    stat_lst = []
    for i in stations_lst:
        for j in i:
            stat_lst.append(j)
    #print(stat_lst)
    
    d={}
    for key in stat_lst:
        d[key] = []
        for line in line_lst:
            if key in mrt[line]:
                d[key].append(line)
    return d

def get_interchange(stationline):
    d = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            d[station] = stationline[station]
    return d


  
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
    
    line_st = lines[start]
    line_end = lines[end]
    #print(line_st)
    #print(line_end)
    ans = []
    if line_st == line_end:
        all_stat = mrt_d[line_st[0]]
        #print(all_stat)
        index_st = all_stat.index(start)
        index_end = all_stat.index(end)
        #print(index_st)
        #print(index_end)
        if index_st > index_end:
            all_stat = all_stat[::-1]
            index_st = all_stat.index(start)
            index_end = all_stat.index(end)
        #print(all_stat)
        ans = all_stat[index_st: index_end+1]
    return ans
        
        