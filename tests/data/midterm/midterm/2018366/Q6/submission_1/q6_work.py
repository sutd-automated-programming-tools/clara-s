import pickle

def read_stations(f):
    sublist=[]
    output = dict()
    for line in (f):
        if line == '=EastWestLine (EW)=\n':
            continue
        elif line == '=EastWestLine (CG)=\n':
            output['EastWestLine (EW)'] = sublist1
            sublist = []
            continue
        elif line == '=NorthSouthLine=\n':
            output['EastWestLine (CG)'] = sublist1
            sublist = []
            continue
        elif line == 'END':
            break
        else:
            sublist1=sublist
            sublist = line.strip('\n')
            sublist = sublist.split(', ')
            
    output['NorthSouthLine'] = sublist
    return output

def get_stationline(mrt):
    dic=dict()
    for i in mrt:
        for x in mrt[i]:
            dic[x]=''
    for i in mrt:
        for x in mrt[i]:
            dic[x]+=i
    return dic

def get_interchange(stationline):
    dic=dict()
    for i in stationline:
        for x in stationline[i]:
            if len(stationline[i])>1:
                dic[i]=stationline[i]
            
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