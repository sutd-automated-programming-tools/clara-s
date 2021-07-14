
def read_stations(f):
    dic={}
    for line in f:
        #print(line)
        line_1=line.strip()
        print(line_1)
        data=line_1.split()
        print(data)
        

with open("mrt_line_short.txt","r") as f1:
    ans=read_stations(f1)
    
def get_stationline(mrt):
    dic={}
    for key in mrt:
        if key in dic:
            dic[key]+=`
            
def get_interchange(stationline):
    dic={}
    info=f.readlines()
#    print(info)
    dictionary={}
    for i in info:
        i=i.split()
    for key in stationline:
        if len(stationline[key])>1:
            key=i[0]
            value=stationline[key]
            dictionary[key]=value
    return dic

def find_path(f,start,end):
    if path==None
        return None
    if path==exist
        return path
    