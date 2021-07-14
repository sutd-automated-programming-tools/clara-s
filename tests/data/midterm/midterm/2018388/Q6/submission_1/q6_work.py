import pickle

def read_stations(f):
    d = {}
    lst = []
    lst1= []
    lst2 = []
    fullchunk=f.read()
    smallchunk=fullchunk.split('=EastWestLine (CG)=')
    for i in smallchunk[0].split('\n'):
        if i =='=EastWestLine (EW)=' or i =='':
            pass
        else:
            for j in i.split(''):
                lst.append(str(j))
    
    
    smaller = smallchunk[1].split('=NorthSouthLine=')
    for i in smaller[0].split('\n'):
        if i =='=EastWestLine (CG)=' or i =='':
            pass
        else:
            for j in i.split(''):
                lst1.append(str(j))
    for i in smaller[1].split('\n'):
        if i =='=NorthSouthLine=' or i =='':
            pass
        else:
            for j in i.split(''):
                lst2.append(str(j))
                
    d.['EastWestLine (EW)']= lst
    d.['EastWestLine (CG)']= lst1
    d.['NorthSouthLine']= lst2
    return d       

def get_stationline(mrt):
    dic = {}
    lst = list(mrt.items())
    for i[1] in lst:
        for n in i[1]:
            dic.update({i[1][n],i[0]})
    return dic

def get_interchange(stationline):
    dic = {}
    lst = list(stationline.items()) 
    for i in len(lst):
        if len(lst[i][i])>= 2:
            dic.update({lst[i][0],lst[i][1]})
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
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    read_stations(f)
    
    