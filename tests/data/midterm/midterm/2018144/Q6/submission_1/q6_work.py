import pickle

def read_stations(f):
    line_d={}
    while True:
        cur_line = f.readline()
        if len(cur_line) == 0:
            break
        if "=" in cur_line:
            key = cur_line.strip()
            key = key.strip("=")
            #line_d[key] = []
        elif len(cur_line)>1:
            cur_line = cur_line.strip()
            mylist = cur_line.split(",")
            line_d[key] = mylist
    return line_d

def get_stationline(mrt):
    newdict={}
    for j in mrt.values():
        for i in j:
            newdict[i] = []
            if i in mrt["EastWestLine (EW)"]:
                newdict[i] += ["EastWestLine (EW)"]
            if i in mrt["EastWestLine (CG)"]:
                newdict[i] += ["EastWestLine (CG)"]
            if i in mrt["NorthSouthLine"]:
                newdict[i] += ["NorthSouthLine"]
    return newdict

def get_interchange(stationline):
    interchange = {}
    for key,values in stationline.items():
        #print(values)
        if len(values)>1:
            interchange[key]=values
    return interchange
  
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
    lines = read_stations(f)
    stations = get_stationline(lines)
    interchange = get_interchange(stations)
    for i in lines.keys():
        print(lines[i])
        if (start in lines[i]) and (end in lines[i]):
            #print(i)
            select_ls = lines[i]
            for num,val in enumerate(select_ls):
                if val==start:
                    num1 = num
                elif val==end:
                    num2 = num
                output_ls = select_ls[num1:num2]
                return output_ls