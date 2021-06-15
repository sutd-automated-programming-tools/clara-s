import pickle

def read_stations(f):
    dic = {}
    line = f.readline()
    x = line.strip('=')
    line = f.readline()
    answer1 = ''
    while line != '\n':
        answer1 += line
        line = f.readline()
    data1 = answer1.strip()
    data1 = data1.split(',')
    for i in range(len(data1)):
        new_data1 = ''
        for j in data1[i]:
            if j != '\n':
                new_data1 = new_data1 + j
        data1[i] = new_data1
    line = f.readline()
   
    y = line.strip('=')
    line = f.readline()
    answer2 = ''
    while line != '\n':
        answer2 += line
        line = f.readline()
    data2 = answer2.strip()
    data2 = data2.split(',')
    for i in range(len(data2)):
        new_data2 = ''
        for j in data2[i]:
            if j != '\n':
                new_data2 = new_data2 + j
        data2[i] = new_data2
    line = f.readline()
    
    z = line.strip('=')
    line = f.readline()
    answer3 = ''
    while line != '\n':
        answer3 += line
        line = f.readline()
    data3 = answer3.strip()
    data3 = data3.split(',')
    for i in range(len(data3)):
        new_data3 = ''
        for j in data3[i]:
            if j != '\n':
                new_data3 = new_data3 + j
        data3[i] = new_data3
    dic[x] = data1
    dic[y] = data2
    dic[z] = data3
    return dic
        
def get_stationline(mrt):
    new_dic = {}
    for keys in mrt:
        for i in range(len(mrt[keys])):
            if mrt[keys][i] not in new_dic:
                new_dic[mrt[keys][i]] = [keys]
            else:
                new_dic[mrt[keys][i]].append(keys)
    return new_dic

def get_interchange(stationline):
    answer = {}
    for keys in stationline:
        if len(stationline[keys]) >= 2:
            answer[keys] = stationline[keys]
    return answer


  
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