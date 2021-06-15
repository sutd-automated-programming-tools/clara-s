import pickle

def read_stations(f):
    station_dict = {}
    for line in f.readlines():
        if '=' in lines.strip():
            line_station = line.strip('=')
        '''line is all station names'''
        station = line.strip()
        print(station)
f = open('f','r')
read_stations(f)
f.close()
    
def get_stationline(mrt):
    new_dict - {}
    main_lines = ['EastWestLine (EW)', 'EastWestLine (CG)', 'NorthSouthLine']
    for i in range(3):
        station_name = mrt[main_lines[i]]
        for station in station_name:
            if station not in new_dict:
                new_dict[station] = list(main_lines[i])
            else:
                line = new_dict.pop(station)
                line.append(main_lines[i])
                new_dict[station] = line
    return new_dict

def get_interchange(stationline):
    interchange_dict = {}
    lst_all = list(stationline.items())
    for i in range(len(lst_all)):
        if len(lst_all[i][1]) > 1: #theres 2 interchange
            interc = stationline.pop(lst_all[i][0])
            interchange_dict[lst_all[i][0]] = interc
        else:
            pass
    return interchange_dict


  
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
    lst = []
    new_dict = get_stationline(mrt)
    interchange_dict = get_interchange(stationline)
    directory = read_stations(f)
    for stations in new_dict:
        if stations == start:
            line = new_dict[stations] #line for the station
            if len(line)==1:
                for x in directory:
                    if x==line[0]:
                        all_stations = directory[x]
                        #iterate thru stations list
                        ls.append(start)
                        while all_stations[i] != end:
                            ls.append(all_stations[i])
                            i+=1
                        ls.append(end)
            #there is more than one interchange