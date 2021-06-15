import pickle

def read_stations(f):
    matrix1 = []
    my_dict = {}
    for line in f:
        line = line.split(",")
        if line == ["=EastWestLine (EW)="]:
            continue

        if line == ["=EastWestLine (CG)="]:
            my_dict['EastWestLine (EW)']= matrix1
            matrix1 = [] #clears the dictionary to put matrices after OP into matrix
            continue

        if line == ["=NorthSouthLine="]:
                my_dict['EastWestLine (CG)'] = matrix1
                matrix1 = []  # clears the dictionary to put matrices after OP into matrix
                continue

        matrix1.append(line)
    return my_dict

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