import pickle
def read_stations(f):
    ans = {}
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if line == '\n':
            continue
        if line[0] == ('='):
            l = line.strip()
            l = l.strip('=')
        else:
            stations = line.split(',')
            for i in range(len(stations)):
                stations[i] = stations[i].strip()
            ans[l] = stations
    return ans
            

def get_stationline(mrt):
    ans = {}
    for line, stations in mrt.items():
        for i in stations:
            ls = []
            if i in mrt['EastWestLine (EW)']:
               ls.append('EastWestLine (EW)') 
            if i in mrt['EastWestLine (CG)']:
               ls.append('EastWestLine (CG)')
            if i in mrt['NorthSouthLine']:
               ls.append('NorthSouthLine')
            ans[i] = ls
    return ans

def get_interchange(stationline):
    ans = {}
    for station, lines in stationline.items():
        if len(lines) > 1:
            ans[station] = lines
    return ans


  
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
    mrt = read_stations(f)
    lines = get_stationline(mrt)
    inter = get_interchange(lines)
    for j in lines[end]:
        if j in lines[start]:
            ans = []
            line = mrt[j]
            for i in range(len(line)):
                if line[i] == start:
                    for k in range(i,len(line)):
                        ans.append(line[k])
                        if line[k] == end:
                            break
                    return ans
                elif line[i] == end:
                    for k in range(i,len(line)):
                        ans.append(line[k])
                        if line[k] == start:
                            break
                    return ans[::-1]
    good = []
    for station, line in inter.items():
        if lines[start][0] in line and lines[end][0] in line:
            good.append(station)
    if len(good) == 0:
            return None
    cnt = 10000

    for i in good:
        ans = []
        line = mrt[lines[start][0]]
        for j in range(len(line)):
            if line[j] == start:
                for k in range(j,len(line)):
                    ans.append(line[k])
                    if line[k] == end:
                        break
            elif line[j] == i:
                for k in range(j,len(line)):
                    ans.append(line[k])
                    if line[k] == start:
                        break
        ans2 = []
        line2 = mrt[lines[end][0]]
        for j in range(len(line2)):
            if line2[j] == i:
                for k in range(j,len(line2)):
                    ans2.append(line2[k])
                    if line2[k] == end:
                        break
            elif line2[j] == end:
                for k in range(j,len(line2)):
                    ans2.append(line[k])
                    if line2[k] == start:
                        break
        if len(ans)+len(ans2) < cnt:
            cnt = len(ans)+len(ans2)
            final = ans+ans2
    
    return final