import pickle

def read_stations(f):
    ret_d = {}
    c_key = ''
    while True:
        lines = f.readline()
        if lines == '':
            break
        lines = lines.split('=')
        #print(lines)
        
        if lines[0] == '':
            c_key = lines[1]       
        elif len(lines) == 1:
            if lines[0] == '\n':
                pass
            else:
                lines = lines[0].split(',')
                lines = [i.strip() for i in lines]
                ret_d[c_key] = lines
    #print(ret_d)
    return ret_d

def get_stationline(mrt):
    new_d = {}
    for i in mrt.keys():
        for j in mrt[i]:
            if j in new_d:
                val = new_d[j]
                val.append(i)
                new_d[j] = val
            else:
                new_d[j] = [i]
    #print(new_d)
    return new_d

def get_interchange(stationline):
    new_d = {}
    for i in stationline.keys():
        le = len(stationline[i])
        if le > 1:
            new_d[i] = stationline[i]
#    print(new_d)
    return new_d

  
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
    
    mrts = read_stations(f)
    station_line = get_stationline(mrts)
    get_interchange(station_line)
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass