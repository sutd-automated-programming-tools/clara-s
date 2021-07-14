import pickle

def read_stations(f):
    all_lines = f.readlines()
    stn_dict = {}
    los_less_ew = [each_line.strip('=EastWestLine (EW)=') for each_line in all_lines]
    los_less_ew_cg = [each_line.strip('=EastWestLine (CG)=') for each_line in los_less_ew]
    los_less_nsl = [each_line.strip('=NorthSouthLine=') for each_line in los_less_ew_cg]
    los_less_nlc = [each_line.strip('\n') for each_line in los_less_nsl]
    lol_cool = [each_line.split(', ') for each_line in los_less_nlc]
    ew_list = []
    for i in range(33):
        ew_list.append(lol_cool[i])
    stn_dict['EastWestLine (EW)'] = ew_list 
    ew_cg_list = []
    for i in range(33, 36):
        ew_cg_list.append(lol_cool[i])
    stn_dict['EastWestLine (CG)'] = ew_cg_list
    nsl_list = []
    for i in range(36, 64):
        nsl_list.append(lol_cool[i])
    stn_dict['NorthSouthLine'] = nsl_list
    return stn_dict
    
    pass

def get_stationline(mrt):
    new_dict = {}
    for 
    values_lst = mrt.values()
    for value in value_lst:
        new_dict.setdefault(value) # creates new keys for all stations in value_lst, all values set to 0
        if value in mrt.get('EastWestLine (EW)') and value in mrt.get('EastWestLine (CG)'): # checks if station is in EW and CG
            new_dict.[value] = ['EastWestLine (EW)', 'EastWestLine (CG)']
        elif value in mrt.get('EastWestLine (EW)') and value in mrt.get('NorthSouthLine'):
            new_dict.[value] = ['EastWestLine (EW)', 'NorthSouthLine']
        elif value in mrt.get('EastWestLine (EW)'):
            new_dict.[value] = ['EastWestLine (EW)']
        elif value in mrt.get('EastWestLine (CG)'):
            new_dict.[value] = ['EastWestLine (CG)']
        elif value in mrt.get('NorthSouthLine'):
            new_dict.[value] = ['NorthSouthLine']
    return new_dict
    pass

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