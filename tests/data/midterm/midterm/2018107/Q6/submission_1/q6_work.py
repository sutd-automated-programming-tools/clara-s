import pickle

def read_stations(f):
    dic={}
    dic1={}
    output=[]
    b="=EastWestLine (EW)=\n"
    for line in f:
        if line=="=EastWestLine (EW)=\n" or line =="=EastWestLine (CG)=\n" or line =="=NorthSouthLine=\n":
            ab=b.strip()
            dic[ab.strip("=")]=output
            b=line
            output=[]
        else:
            a=line.strip()
            aa=a.strip("\n")
            c=aa.split(", ")
            output.append((c))
            dic.update({b.strip():output})
    dic.update({b.strip():output})
    EW=dic.get("=EastWestLine (EW)=")[0]
    dic1["EastWestLine (EW)"]=EW
    CG=dic.get("=EastWestLine (CG)=")[0]
    dic1["EastWestLine (CG)"]=CG
    NS=dic.get("=NorthSouthLine=")[0]
    dic1["NorthSouthLine"]=NS
    return dic1

def get_stationline(mrt):
    dic={}
    for entry in mrt:
        a=mrt.get(entry)
        for station in a:
            if station not in dic:
                dic.update({station:[entry]})
            else:
                dic[station] += [entry]
    return dic

def get_interchange(stationline):
    dic ={}
    for entry in stationline:
        if len(stationline.get(entry))>1:
            dic[entry]=stationline[entry]
    return dic


  
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
#    with open('stations_short.pickle','rb') as f:
#        mrt_d = pickle.load(f)
#    with open('lines_short.pickle','rb') as f:
#        lines = pickle.load(f)
 #   with open('interchange_short.pickle','rb') as f:
 #       interchange = pickle.load(f)
    startidx=0
    endidx=0
    mrt_d=read_stations(f)
    lines=get_stationline(mrt_d)
    interchange=get_interchange(lines)
    for entry in lines:
        a=lines.get(entry)
        if start in a and end in a:
            for idx in range(0,len(a)-1):
                if a[idx] == start:
                    startidx=idx
                if a[idx] == end:
                    endix=idx
            if startidx>endix:
                n=-1
            else:
                n=1
            return a[startidx:endidx+1:n]