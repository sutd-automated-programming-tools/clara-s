import pickle

def read_stations(f):
    mrtMapped=dict()
    fulllist=[]
    for line in f:
        lineandstations=fulllist.append(list(x.strip() for x in line.split(",")))
        #line=lineandstations.pop(0)    
        #m#rtMapped[line]=lineandstations
        #print( lineandstations)
    
    
    mrtMapped[fulllist[0][0].strip("=")]=fulllist[1]
    mrtMapped[fulllist[3][0].strip("=")]=fulllist[4]
    mrtMapped[fulllist[6][0].strip("=")]=fulllist[7]
    #print(fulllist[6][0].strip("="))
    return(mrtMapped)

    pass

def get_stationline(mrt):
    stationdict=dict()
    for i in mrt:
        v=list(mrt.values())
    #print(v[2])
    q=(list(mrt.keys()))
    m=0
    while m <(len(q)):
        n=0
        linelist=[]
        while n <len(v[m]):
            stationdict[v[m][n]]=(q[m])
            n+=1
        m+=1
    print(stationdict)
    
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