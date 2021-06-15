import pickle

def read_stations(f):
    list = []
    output = dict()
    for line in f:
        if line == '=EastWestLine (EW)=\n':
            continue
        elif line == '=EastWestLine (CG)=\n':
            output['EastWestLine (EW)'] = list[0]
            list = []
            continue
        elif line == '=NorthSouthLine=\n':
            output['EastWestLine (CG)'] = list[0]
            list = []
            continue
        elif line == 'Jurong East, Bukit Batok, Bukit Gombak, Choa Chu Kang, Yew Tee, Kranji, Marsiling, Woodlands, Admiralty, Sembawang, Canberra, Yishun, Khatib, Yio Chu Kang, Ang Mo Kio, Bishan, Braddell, Toa Payoh, Novena, Newton, Orchard, Somerset, Dhoby Ghaut, City Hall, Raffles Place, Marina Bay, Marina South Pier':
            sublist = line.strip('\n')
            sublist = sublist.split(', ')
            list.append(sublist)
            output['NorthSouthLine'] = list[0]
            list = []
        else:
            sublist = line.strip('\n')
            sublist = sublist.split(', ')
            list.append(sublist)
    return output

def get_stationline(mrt):
    new_dict = {}
    for k,v in mrt.items():
        for i in v:
            if i not in new_dict:
                new_dict[i] = [k]
            elif i in new_dict:
                new_dict[i].append(k)
    return new_dict

def get_interchange(stationline):
    new_dict = {}
    for k,v in stationline.items():
        if len(v) > 1:
            new_dict[k] = v
    return new_dict


  
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