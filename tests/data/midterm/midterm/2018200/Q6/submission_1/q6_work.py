import pickle

def read_stations(f):
    a = []
    d = {}
    c = []
    for lines in f:
        line = lines.strip()
        #if line[0:1] == '=':
            #d[line.strip('=')] = []
        #print(line)
        a.append(line)
    for i in a:
        if i[0:1] == '=':
            c = []
            d[i.strip('=')] = c
        else:
            c.append(i)
    for keys, values in d.items():
        d[keys] = values[0].split(',')

    for keys2, values2 in d.items():
        for pos, k in enumerate(values2):
            values2[pos] = k.strip()
        d[keys2] = values2
    
        
            
    #print(line)
    return d

def get_stationline(mrt):
    B = []
dic = {}
for keys, values in mrt.items():
    for j in values:
        B.append(j)

for keys2, values2 in mrt.items():
    
    for i in values2:
        
        if keys2 not in dic:
            b = []
            dic[i] = b
            b.append(keys2)
        if keys2 in dic:
            dic[keys2] = val
            b = [val, keys2]
    return dic

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