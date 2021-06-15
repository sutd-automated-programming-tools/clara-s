import pickle

def read_stations(f):
    daten = f.readlines()
    i = 0; ligne = None; arret = None; pendaison = {}
    while i < len(daten):
        if daten[i][0] == '=':
            ligne = daten[i].strip().replace('=','')
        elif daten[i][0] == '\n':
            pass
        else:
            arret = daten[i].replace(', ',',')
            arret = arret.strip().split(',')
            pendaison[ligne] = arret
        i += 1
    return pendaison
        
    
def get_stationline(mrt):
    stn = {}
    for line in list(mrt.keys()):
        fin = len(mrt[line])
        i = 0
        while i < fin:
            try:
                stn[mrt[line][i]] += [line]
            except KeyError:
                stn[mrt[line][i]] = [line]
            i += 1
    return stn

def get_interchange(stationline):
    xcg = {}
    for arret in list(stationline.keys()):
        if len(stationline[arret])> 1:
            try:
                xcg[arret] += stationline[arret]
            except KeyError:
                xcg[arret] = stationline[arret]
    return xcg
        


  
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
    
    D = mrt_d
    S = lines
    line1 = S[start]; line2 = S[end]
    for a in range(len(line1)):
        for b in range(len(line2)):
            if line1[a] == line2[b]:
                si = D[line1].index(start); ei = D[line2].index(end)
                pth = []
                i = si
                for i in range(si,ei):
                    pth.append(D[line1][i])
                return pth