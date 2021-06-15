def read_stations(f):
    NSlist = []
    EWlist = []
    newdata =[]
    EWCG = []
    
    for line in f:
        line = line.strip()
        if line == '=EastWestLine (EW)=':
            check = 1
        elif line == '=EastWestLine (CG)=':
            check = 2
        elif line == '=NorthSouthLine=':
            check = 3
        else:
            data = line.split(', ')
            
            for el in data:
                newel = str(el)
                newdata.append(newel)
                if check == 1: 
                    EWlist.append(newel)
                    
                if check == 3:
                    NSlist.append(newel)
                if check == 2:
                    EWCG.append(newel)
                
    dictionary = {'EastWestLine (EW)':EWlist,'NorthSouthLine':NSlist,'EastWestLine (CG)':EWCG}
    return dictionary 

def get_stationline(mrt):
    mrt = read_stations(f)
    dictionary = {}
    NSL = mrt['NorthSouthLine']
    EWL = mrt['EastWestLine (EW)']
    
    for i in NSL:
        key = NSL[i]
        dictionary[key] = ['NorthSouthLine']
        print(dictionary)
    for I in EWL:
        key = EWL[I]
        dictionary[key] = ['EastWestLine (EW)']
        print(dictionary)
    dictionary['Tanah Merah'] = ['EastWestLine (EW)', 'EastWestLine (CG)']
    dictionary['TExpo'] = ['EastWestLine (EW)', 'EastWestLine (CG)']
    dictionary['Changi Airport'] = ['EastWestLine (EW)', 'EastWestLine (CG)']  
    dictionary['City Hall'] = ['EastWestLine (EW)', 'NorthSouthLine']  
    dictionary['Raffles Place'] = ['EastWestLine (EW)', 'NorthSouthLine'] 
    return dictionary 

def get_interchange(stationline):
    stationline = get_stationline(mrt)
    for i in range(len(stationline)):
        if len(stationline[i]) <= 1:
            stationline.remove(i)
    return stationline 


  
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