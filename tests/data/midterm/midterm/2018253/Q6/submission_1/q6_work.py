import pickle

def read_stations(f):
    list1 = []
    for line in f:
        list1.append(line)
    list1.remove("=EastWestLine (EW)=\n")
    list1.remove("\n")
    list1.remove("=NorthSouthLine=\n")
    list1.remove("=EastWestLine (CG)=\n")
    list1.remove("Tanah Merah, Expo, Changi Airport\n")
    list1.remove("\n")
    list2 = []
    list3 = []
    listcg.append(
    list2.append(list1[0])
    list3.append(list1[1])
    list2str = ''
    list3str = ''
    listcg = ''
    for i in list2:
        list2str += i
    for i in list3:
        list3str += i
    list2str = list2str.split(', ')
    list3str = list3str.split(', ')
    list2str[-1] = 'Tuas Link'
    mydict = {'NorthSouthLine': list3str}
    mydict['EastWestLine (EW)'] = list2str

def get_stationline(mrt):
    newdict = {}
    for i in mrt['NorthSouthLine']:
        if i == 'Jurong East' or i == 'City Hall' or i == 'Raffles Place':
            newdict[i] = ['EastWestLine (EW)', 'NorthSouthLine']
        else:
            newdict[i] = ['NorthSouthLine']
    for i in mrt['EastWestLine (EW)']:
        if i == 'Tanah Merah':
            newdict[i] = ['EastWestLine (EW)', 'EastWestLine (CG)']
        elif i != 'Jurong East' and i != 'City Hall' and i != 'Raffles Place':
            newdict[i] = ['EastWestLine (EW)']
          
    for i in mrt['EastWestLine (CG)']:
        if i != 'Tanah Merah':
            newdict[i] = ['EastWestLine (CG)']
    return newdict
                    
def get_interchange(stationline):
    newdict1 = {}
    for i in stationline:
        if 
    for i in range(0, len(stationline)):
        if len(stationline[i]) > 1:
            newdict1 +=  
  
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