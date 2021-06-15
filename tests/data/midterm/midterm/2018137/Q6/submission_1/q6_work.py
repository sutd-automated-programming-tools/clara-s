import pickle

def read_stations(f) :
     f = "mrt_lines_short.txt"
     fread = open ( f , "r" )
     freadlines = fread.readlines()
     for x in freadlines :
      fstrip = x.strip('\n')
      fsplit = fstrip
     
     lst_EW = freadlines[1]
     lst_CG = freadlines[4]
     lst_NS = freadlines[]
     
     return {'EastWestLine (EW)' : [lst_EW] , 'EastWestLine (CG)' : [lst_CG] , 'NorthSouthLine' : [lst_NS] }

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