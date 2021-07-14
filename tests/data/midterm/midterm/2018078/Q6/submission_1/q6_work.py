import pickle

def read_stations(f):
    ret_dict = {}
    
    while True:
        lines = f.readline()
        if lines == '':
            break
        
        lines = lines.split(',')
        lines = [i.strip() for i in lines]
        lines[-1] = lines[-1].strip()
        print(lines[-1])
        ret_dict[lines[0]] = lines[1:]
    print(ret_dict)
    return ret_dict        

    
f = open('mrt_lines_short.txt' ,'r')
    
'''turning the text into a dict and the list with the 
def get_stationline(mrt):
    
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