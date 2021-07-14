import pickle

def read_stations(f):
    contents = f.read()
    
    contents.strip()

    contents = contents.replace("\n","")
    
    contents = contents.split("=")

    contents = contents[1:]
    

    
    contents = [x.strip() for x in contents]
    
    content_dict = {}

    iterator = 0
    
    while iterator < len(contents) - 1:
        if content_dict.get(contents[iterator]) is None:
            content_dict[contents[iterator]] = []
        content_dict[contents[iterator]] = (contents[iterator + 1].split(", "))
        iterator += 2
    
    
    return content_dict

def get_stationline(mrt):
    
    mrt_dict = mrt
    ans_dict = {} 
    
    
    for key in mrt_dict:
        
        station_list = mrt_dict.get(key)
        station_list = [x.strip() for x in station_list]
        for station in station_list:
            if ans_dict.get(station) is None:
                ans_dict[station] = [key]
            else:
                ans_dict[station].append(key)


                
    return ans_dict

def get_interchange(stationline):
    
    ans_dict = {}
    
    for station in stationline:
        if len(stationline.get(station)) > 1:
            ans_dict[station] = stationline.get(station)
            
    return ans_dict


  
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
    
    
    