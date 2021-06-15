import pickle

def read_stations(f):
    ls = f.read().strip().split('\n')
    ewl = ls[ls.index('=EastWestLine (EW)='):ls.index('=EastWestLine (CG)=')]
    ewlcg = ls[ls.index('=EastWestLine (CG)='):ls.index('=NorthSouthLine=')]
    nsl = ls[ls.index('=NorthSouthLine='):]
    ewl[0] = ewl[0].replace('=','')
    ewlcg[0] = ewlcg[0].replace('=','')
    nsl[0] = nsl[0].replace('=','')
    ewl = [x.split(',') for x in ewl]
    ewlcg = [x.split(',') for x in ewlcg]
    nsl = [x.split(',') for x in nsl]
    ewl[1] = [x.strip() for x in ewl[1]]
    ewlcg[1] = [x.strip() for x in ewlcg[1]]
    nsl[1] = [x.strip() for x in nsl[1]]
    d = {}
    d[ewl[0][0]] = ewl[1]
    d[ewlcg[0][0]] = ewlcg[1]
    d[nsl[0][0]] = nsl[1]
    return d

def get_stationline(mrt):
    d = {}
    for stns in mrt['EastWestLine (EW)']:
        if stns in mrt['EastWestLine (CG)']:
            d[stns] = ['EastWestLine (EW)','EastWestLine (CG)']
            mrt['EastWestLine (EW)'].remove(stns)
            mrt['EastWestLine (CG)'].remove(stns)

        if stns in mrt['NorthSouthLine']:
            d[stns] = ['EastWestLine (EW)', 'NorthSouthLine']
            mrt['EastWestLine (EW)'].remove(stns)
            mrt['NorthSouthLine'].remove(stns)
    for key in mrt:
        stns = mrt[key]
        for ele in stns:
            d[ele] = [key]
    return d

def get_interchange(station_line):
    d = {}
    for key in station_line:
        if len(station_line[key]) != 1:
            d[key] = station_line[key]
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
    d1 = read_stations(f)
    d2 = get_stationline(d1)
    d3 = get_interchange(d2)
    if d2[start] == d2[end]:
        line = d2[start]
        start_ind = d1[line].index(start)
        end_ind = d1[line].index(end)
        return d1[line][start_ind:end_ind+1]
    else:
        start_line = d2[start]
        end_line = d2[end]
        for key in d3:
            if start_line and end_line in key:
                interchange = key
            else:
                return None
        start_ind = d1[start_line].index(start)
        interchange_ind_1 = d1[start_line].index(interchange)
        interchange_ind_2 = d1[end_line].index(interchange)
        end_ind = d1[end_line].index(end)
        part1 = d1[start_line][start_ind:interchange_ind+1]
        part2 = d1[end_line][interchange_ind:end_ind+1]
        return part1 + part2