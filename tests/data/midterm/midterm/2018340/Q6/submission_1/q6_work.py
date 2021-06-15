import pickle

def read_stations(f):
    output = {'EastWestLine(EW)':[],
              'NorthSouthLine':[],
              'EastWestLine(CG)':[],
              }
    
    for line in f:
        
        line = line.strip()
        data = line.split()
        print(data)
        if len(data) > 1:
            if data[0] == 'Pasir':
                for i in data:
                    output['EastWestLine(EW)'].append(i)
            elif data[0] == 'Tanah':
                for i in data:
                    output['EastWestLine(CG)'].append(i)
            elif data[0] == 'Jurong':
                for i in data:
                    output['NorthSouthLine'].append(i)
        return output

def get_stationline(mrt):
    output = {}
    for i in mrt.values():
        if i in mrt['EastWestLine(EW)']:
            if i not in output:
                output[i] = ['EastWestLine(EW)']
            else:
                output[i].append('EastWestLine(EW)')
                
        elif i in mrt['EastWestLine(CG)']:
             if i not in output:
                output[i] = ['EastWestLine(CG)']
             else:
                output[i].append('EastWestLine(CG)')
            
        elif i in mrt['NorthSouthLine']:
            if i not in output:
                output[i] = ['NorthSouthLine']
            else:
                output[i].append('NorthSouthLine')
            
    return output

def get_interchange(stationline):
    output = {}
    for key in stationline:
        if len(stationline[key]) > 1:
            output[key] = stationline[key]
    return output


  
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
        station = read_stations(f)
    stationline = get_stationline(station)
    interchange  = get_interchange(stationline)
    EW = station['EastWestLine(EW)']
    CG = station['EastWestLine(CG)']
    NS = station['NorthSouthLine']
    
            
    if start not in interchange and end not in interchange:
        if stationline[start] == stationline[end]:
            start_idx = 0
            end_idx = 0
            if stationline[start] == 'EastWestLine(EW)':
                for i in range(len(EW)):
                    if EW[i] == start:
                        start_idx = i
                    if EW[i] == end:
                        end_idx = i
                return stationline[start_idx:end_idx]
            if stationline[start] == 'EastWestLine(CG)':
                for i in range(len(CG)):
                    if CG[i] == start:
                        start_idx = i
                    if CG[i] == end:
                        end_idx = i
                return stationline[start_idx:end_idx]
                        
            if stationline[start] == 'NorthSouthLine':
                for i in range(len(NS)):
                    if NS[i] == start:
                        start_idx = i
                    if NS[i] == end:
                        end_idx = i
                return stationline[start_idx:end_idx]
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass