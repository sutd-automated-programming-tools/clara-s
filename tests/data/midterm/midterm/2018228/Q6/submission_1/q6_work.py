import pickle

def read_stations(f):
    mrt = {}
    line = f.readlines()
    print(line)
    print('')
    line_s = [each.strip('\n').strip('=') for each in line]
    print(line_s)
    print('')
    line_ss = [each.split(',') for each in line_s]
    print(line_ss)
    print('')
    output = {}
    output['EastWestLine (EW)'] = line_ss[1]
    output['EastWestLine (CG)'] = line_ss[4]
    output['NorthSouthLine'] = line_ss[7]
    return output

def get_stationline(mrt):
    dic = {}
    for i in mrt.values():
        for stations in i:
            dic[stations] = [x for x in mrt if stations in mrt[x]]
    return dic

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