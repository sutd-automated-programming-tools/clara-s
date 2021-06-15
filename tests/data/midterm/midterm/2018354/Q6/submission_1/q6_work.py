import pickle

def read_stations(f):
    
    
    list = []
    output = dict()
    for line in (f):
        if line == '=EastWestLine (EW)=\n':
            continue
        elif line == '= EastWestLine (CG)=':
            output['EastWestLine (EW)'] = list
            list = []
            continue
        elif line== '= NorthSouthLine=':
            output['EastWestLine (CG)']= list
            list=[]
            conrinue
        elif line == 'end of text file':
            break
        else:
            sublist = line.strip('\n')
            sublist = sublist.split(' ')
            sublist = [i for i in sublist]
            list.append(sublist)
    #output[''] = list
    return output

def get_stationline(mrt):
    
    dic={}
    for stations in mrt.value():
        


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