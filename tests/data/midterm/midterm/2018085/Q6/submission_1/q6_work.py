import pickle

def read_stations(f):
    a=""
    output={}
    for line in f:
        if "Line" in line:
            a=line.strip("\n")
            a=a[1:-1]
        else:
            if len(line.strip("\n"))>0:
                line=line.strip("\n")
                line=line.strip()
                x=line.split(',')
                lis=[]
                for j in x:
                    lis.append(j.strip())
                output[a]=lis
    return output

def get_stationline(mrt):
    output={}
    for i in mrt.values():
        for j in i:
            list1=[]
            for k in mrt:
                if j in mrt[k]:
                    list1.append(k)
            if j not in output.keys():
                output[j]=list1
    return output

def get_interchange(stationline):
    output={}
    for i in stationline:
        if len(stationline[i])>1:
            output[i]=stationline[i]
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