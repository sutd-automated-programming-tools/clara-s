import pickle

def read_stations(f):
    dic = {}
    f.readline()
    line = f.readline()
    lstemp = line.strip().split(',')
    lstempnew = [item.strip() for item in lstemp]
    dic['EastWestLine (EW)'] = lstempnew
    
    for x in range(2):
        f.readline()
    line = f.readline()
    lstemp3 = line.strip().split(',')
    lstemp3new = [item.strip() for item in lstemp3]
    dic['EastWestLine (CG)'] = lstemp3new
    
    for x in range(2):
        f.readline()
    line = f.readline()
    lstemp2 = line.strip().replace(' ', '').split(',')
    lstemp2new = [item.strip() for item in lstemp2]
    dic['NorthSouthLine'] = lstemp2new
    
    return dic
    
    return dic

def get_stationline(mrt):
    dic = {}
    for key, value in mrt.items():
        for item in value:
            dic[item] = [key]
            
    cg = ['Tanah Merah']
    eww = ['Raffles Place', 'City Hall', 'Jurong East']
    
    com = cg +eww
    
    for key, value in dic.items():
        if key in cg:
            dic.key = ['EastWestLine (EW)', 'EastWestLine (CG)']
        elif key in eww:
            dic.key = ['EastWestLine (EW)', 'NorthSouthLine']
    return dic


  
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