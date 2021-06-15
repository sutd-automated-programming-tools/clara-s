import pickle

def read_stations(f):
    my_dict = {}
    b = f.readlines()
    j = 2
    my_list = []
    while j<=6:
        c = b[j].split(',')
        for i in c:
            my_list.append(i)
        my_dict[b[0].strip('=')] = my_list
        j += 1
    d = b[10].split(',')
    another_list = []
    for i in b:
        another_list.append(i)
    my_dict[b[8].strip('=')] = another_list
    k = 14
    lst = []
    while k<=18:
        c = b[j].split(',')
        for i in c:
            lst.append(i)
        my_dict[b[12].strip('=')] = lst
        k+=1
    return my_dict

def get_stationline(mrt):
    another_dict = {}
    for i in mrt:
        for j in mrt[i]:
            if j in another_dict:
                another_dict[j].append(i)
            else:
                my_list = []
                my_list.append(i)
                another_dict[j] = my_list
    return another_dict

def get_interchange(stationline):
    bb = {}
    for k in stationline:
        if len(stationline[k]) > 1:
            bb[k] = stationline[k]
        else:
            continue 
    return bb


  
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
        mrt = read_station(f)
    cc = get_station(mrt)
    if len(cc[start]) > len(cc[end]):
        for i in cc[end]:
            if i in cc[start]:
                mah_list = []
                a = mrt[cc[start]]
                b = mrt[cc[end]]
                c = a.index(start)
                d = b.index(end)
                while c<=d:
                        mah_list.append(read_station(f)[cc[start]][c])
                        c+=1
                return mah_list 
            else:
                dd = get_interchage(cc)
                for interchange in dd:
                    if i in dd[interchange]:
                        station_to_change_at = interchange 
                        continue 
    elif len(cc[start]) <len(cc[end]):
        for i in cc[start]:
            if i in cc[end]:
                mah_list = []
                a = mrt[cc[start]]
                b = mrt[cc[end]]
                c = a.index(start)
                d = b.index(end)
                while c<=d:
                    mah_list.append(read_station(f)[cc[start]][c])
                    c+=1
                return mah_list 
    elif len(cc[start]) == len(cc[end]):
        if cc[start] == cc[end]:
            mah_list = []
            a = read_station(f)[cc[start]]
            b = read_station(f)[cc[end]]
            c = a.index(start)
            d = b.index(end)
            while c<=d:
                mah_list.append(read_station(f)[cc[start]][c])
                c+=1
                return mah_list 
        
        