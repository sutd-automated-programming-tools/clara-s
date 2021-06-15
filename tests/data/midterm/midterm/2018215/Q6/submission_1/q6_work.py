import pickle

def read_stations(f):
    dic = {}
    for line in f:
        line = line.strip()
        if line == "":
            continue
        elif line[0] == '=':
            title = line.strip('=')
        else:
            stations = line.split(',')
            dic[title] = stations
    return dic

def get_stationline(mrt):
    final = {}
    for k, v in mrt.items():
        for i in v:
            i = i.strip(" ")
            if i in final.keys():
                j = final.pop(i)
                j.append(k)
                final[i] = j
            else:
                final[i] = [k]
    return final

def get_interchange(stationline):
    final = {}
    new_dic = stationline.copy()
    print(new_dic)
    for k, v in stationline.items():
        if len(v) > 1:
            j = new_dic.pop(k)
            final[k] = j
    return final

  
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
    final = []
    mrt_d = read_stations(f)
    #lines = get_stationline(mrt)
    #interchange = get_interchange(stationline)
    for k, v in mrt_d.items():
        if start in v or end in v:
            a = v.index[start]
            b = v.index[end]
            for i in range(a, b):
                final.append(i)
    return final