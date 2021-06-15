import pickle

def read_stations(f):
    aline_list = []
    ans = {}
    for aline in f:
        aline = aline.strip().strip("=")
        aline_list.append(aline)
    for a in range(0, len(aline_list), 3):
        mrt_list = aline_list[a+1].split(", ")
        ans[aline_list[a]] = mrt_list
    return ans
        
#qn6b
def get_stationline(mrt):
    ans = {}
    for key, value in mrt.items():
        for station in value:
            if station not in ans:
                ans[station] = []
            ans[station].append(key)
    return ans

#qn6c
def get_interchange(stationline):
    ans = {}
    for key, value in stationline.items():
        if len(value) > 1:
            ans[key] = value
    return ans


  
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
    ans = []
    #check if stations on same line
    same_station = False
    mrt = read_stations(f)
    for key, value in mrt.items():
        if start in value:
            start_line = key
            
            if end in value:
                same_station = True
        if end in value:
            end_line = key

    #find interchange for 2 lines
    if start_line != end_line:
        stationline = get_stationline(mrt)
        interchange_dict = get_interchange(stationline)
        interchange_station = None
        
        for key,value in interchange_dict.items():
            if start_line in value and end_line in value:
                interchange_station = key
        if interchange_station == None:
            return None
#    mrt[start_line]
    if start_line == end_line:
        start_index = mrt[start_line].index(start)
        end_index = mrt[start_line].index(end)
        for a in range(start_index, end_index+1):
            flip = 1
            ans.append(mrt[start_line][a])
        for a in range(end_index, start_index+1):
            flip = 2
            ans.append(mrt[start_line][a])
        if flip == 2:
            ans = ans[::-1]
            return ans
    else:
        start_index = mrt[start_line].index(start)
        end_index = mrt[end_line].index(end)
        interchange_startline = mrt[start_line].index(interchange_station)
        interchange_endline = mrt[end_line].index(interchange_station)