import pickle

def get_stationline(mrt):
    B={}
    A=mrt
    for key in A:
        for i in range(len(A[key])):
            if A[key][i] in B:
                B[A[key][i]]=[B[A[key][i]], key]
            else:
                B[A[key][i]]=key
    return B

mrt=read_stations(f)
ans=get_stationline(mrt)     
print(mrt)   

def get_interchange(stationline):
    C={}
    for key in stationline:
        if type(stationline[key]) is list:
            C[key]=stationonine[key]
    return C


  
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