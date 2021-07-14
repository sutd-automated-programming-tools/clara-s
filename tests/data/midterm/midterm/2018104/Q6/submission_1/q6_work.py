import pickle

def read_stations(f):
    lines = {}
    for line in f:
        sline = line.rstrip('\n')
        if sline == '':
            continue
        elif sline[0] == '=':
            keyhead = sline.strip('=')
        else:
            lines[keyhead] = sline.split(', ')
    return lines

def get_stationline(mrt):
    station_dict = {}
    for i in mrt:
        station = mrt[i]
        for j in station:
            if j not in station_dict:
                station_dict[j] = [i]
            else:
                station_dict[j].append(i)
    return station_dict

def get_interchange(stationline):
    interchanges = {}
    for i in stationline:
        if len(stationline[i]) != 1:
            interchanges[i] = stationline[i]
    return interchanges


  
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
def find_path(f, start, end):
    # A function to get station distances
    def get_dist(stations, start, end):
        start_index = stations.index(start)
        end_index = stations.index(end)
        return end_index - start_index

    # Subfunction to get station list:
    def get_stnlst(stations, start, end):
        start_index = stations.index(start)
        end_index = stations.index(end)
        lst_stations = stations[start_index:end_index]
        return lst_stations


    def test_lines(line_start, line_end, lines, interchanges):
        if line_start == line_end:
            stations = lines[line_start]
            lst_stations = get_stnlst(stations, start, end)
            return lst_stations
        else:
            sl = lines[line_start]
            el = lines[line_end]
            shortest = 999999
            not_found = True
            for i in interchanges:
                stn = interchanges[i]
                if (line_start in stn) and (line_end in stn):
                    start_int = get_dist(sl, start, stn)
                    end_int = get_dist(el, stn, end)
                    total = start_int + end_int
                    if total < shortest:
                        interchange = i
                    not_found = False
            if not_found:
                return None
            full_list = get_stnlst(sl, start, interchange) + get_stnlst(el, interchange, end)
            return full_list
    # Initialisation and setup of dicts
    lines = read_stations(f)
    stationline = get_stationline(lines)
    interchanges = get_interchange(stationline)
    line_s = stationline[start]
    line_e = stationline[end]
    for sl in line_s:
        for el in line_e:
            lenls = test_lines(sl,el,lines,interchanges)
    if lenls == None:
        return None
    elif len(lenls) > 1:
        lenls.sort()
        return lenls[0]
    else:
        return lenls