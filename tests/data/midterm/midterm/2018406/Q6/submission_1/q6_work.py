import pickle

def read_stations(f):
    fread = open('stations_short.pickle','rb')
     for line in fread:
        word = line.strip()
    return word

def get_stationline(mrt):
    diction = read_stations(f)
    lista = []
    listb = []
    newdict = {}
    for keys in diction:
        listb.append(diction[keys])
        for items in listb:
            if listb.count(items) != 1:
               newdict[items].append[keys]       
        if diction[keys][i] = diction[keys][j]
          lista.append
            

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