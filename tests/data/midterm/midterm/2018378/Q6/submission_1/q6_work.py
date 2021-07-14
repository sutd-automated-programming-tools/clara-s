import pickle


def read_stations(f):
    data=f
    output={}
    header=None
    for line in data:
        if 'Line' in line:            
            header=line.strip()
            output[header]=[]
        else:
            formatted=line.split(',')
            clean = [item.strip() for item in formatted]
            output[header] += clean
    return output
            
def get_stationline(mrt):
    output={}
    for key,values in list(mrt.items()):
        for station in values:
            if station not in output:
                output[station]=[key]
            elif station in output:
                output[station]+=key
    return output

def get_interchange(stationline):
    output={}
    for key, value in list(stationline.items()):
        if len(value)>1:
            output[key]=value
    return output

  
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