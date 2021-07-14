import pickle

def read_stations(f):
    lst = []
    output = {}
    text= f.read()
    f.close()
    n1 = text.strip('\n')
    for i in range(len(n1)):
        n2 = n1[i].split()
        name = str(n2[0])
        for m in range(1,len(n2)+1,+1): 
            lst.append(n2[m])
        output.update({name, lst})
    return output

def get_stationline(mrt):
    mrtline={}
    keys=output.values()
    values=output.keys()
    mrtline.update(keys, values)
    return mrtline

def get_interchange(stationline):
    mrtinterchange={}
    if mrtline.values >1:
        
        


  
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