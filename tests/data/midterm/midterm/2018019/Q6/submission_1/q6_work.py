import pickle

def read_stations(f):
    dict_out = {}
    stn = f.readlines()
    lst = []
    strng = ''
    for i in stn:
        if '=' in i:
            for j in i:
                if j == '=':
                    continue
                else:
                    strng += j
        else:
            lst.append(i.strip())
    lst_2 = strng.split("\n")
    lst.remove('')
    lst.remove('')
    for i in range(3):
        dict_out[lst_2[i]] = [lst[i]]
    return dict_out


def get_stationline(mrt):
    dict_out = {}
    lst2 = []
    for k, v in mrt.items():
        for i in v:
            lst = i.split(',')
        for j in lst:
            if j in lst2:
                dict_out[j] += [k]
            else:
                dict_out[j] = [k]
                lst2.append(j)
    return dict_out

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