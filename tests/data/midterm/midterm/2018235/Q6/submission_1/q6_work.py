import pickle

def read_stations(f):
    dic = {}
    lin = f.readlines()
    for line in lin:
        lines = line.strip('\n')
        if lines[0]== '=':
            if lines[1] == 'E':
                if lines[14] == 'E':
                    key = 'EastWestLine (EW)'
                    
                
                elif lines[14] == 'C':
                    key = 'EastWestLine (CG)'
                    
                elif lines[1] == 'N':
                    key = 'NorthSouthLine'
        
        elif lines[0] != ' ':
            count += lines.count(',')+1
            
        elif line[0] == ' ':
            dic[key] = count
            
    return dic

def get_stationline(mrt):
    x = list(mrt)
    diction = {}
    y = []
    for i in mrt:
        y.append(mrt[i])
        
    list1 = y[0]
    list2 = y[1]
    list3 = y[2]
    
    for j in range(3):
        g = x[j]
        for k in range(len(y[j]):
            diction[str(y[j][k])] = str(x[j])
                       
    return diction
    
        
        

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