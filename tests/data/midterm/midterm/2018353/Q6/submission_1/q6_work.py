import pickle

def read_stations(f):
    mylist = []
    mydict = {}
    for fil in f:
        line = fil.strip().split(',')
        if '=' not in line:
            mylist.append(line)
        else:
            mydict[line.replace('=','')] = mylist
            mylist = []
    return mydict
def get_stationline(mrt):
    mydict = {}
    mylist = []
    for i in mrt:
        for m in mrt[i]:
            mylist.append(m)
    
    for n in mylist:
        mydict[n] = []
        for x in mrt:
            if n in mrt[x]:
                mydict[n].append(x)
    return mydict

def get_interchange(stationline):
    mydict = {}
    for i in stationline:
        if len(stationline[i])>1:
            mydict[i] = stationline[i]
    return mydict
    


  
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
    mrt_d = read_stations(f)
    lines = get_stationline(mrt_d)
    interchange = get_interchange(lines)
    mylist = []
    for i in mrt_d:
        if (start in mrt_d[i] and end in mrt_d[i]):
            line_to_take = mrt[i]
            for i1 in (0,len(mrt[i])):
                if mrt[i][i1] == start:
                    start_num = i1
                if mrt[i][i1] == end:
                    end_num = i1
            mylist = mrt[i][start_num:end_num+1]
        else:
            startline = lines[start]
            endline = lines[end]
            interstation = 0
            for line1 in startline:
                for line2 in endline:
                    for stations in interchange:
                        if (line1 in interchange[stations] and line2 in interchange[stations]):
                            interstation = stations
            if interstation == 0:
                return None
            else:
                for i in mrt_d:
                    if (start in mrt_d[i] and end in mrt_d[i]):
                        line_to_take = mrt[i]
                for i1 in (0,len(mrt[i])):
                    if mrt[i][i1] == start:
                        start_num = i1
                    if mrt[i][i1] == end:
                        end_num = i1
                mylist.append(mrt[i][start_num:end_num+1])
                lens = []
                for r in mylist:
                    lens.append(len(mylist))
                minilen = min(lens)
                for r1 in mylist:
                    if len(r1) == minilen:
                        mylist = r1
                        break
                return mylist
                    
                
            