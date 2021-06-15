import pickle

f = open('mrt_lines_short.txt', 'r')

def read_stations(f):
    d ={}
#    ls = f.read().strip().splitlines()
#    print(ls)
#    lst = []
#    for i in ls:
#        if i.isalpha():
#            lst.append(i)
        
    each_line = f.readlines()
    for element in each_line:
        
        new_str = element.strip('\n')
        #print(new_str)
        elements = new_str.split(', ')
        
        #print(elements)
        d[elements[0]] = list([i for i in elements])
        
    key = ''
    if key in d.keys():
        del d[key]
#    
#    
#        
    return d
print(read_stations(f))

def get_stationline(mrt):
    d = {}
    for k, v in mrt.items():
        d[k] = v
    return d

def get_interchange(stationline):
    d= {}
    for k, v in stationline.items():
        print(v)
        for value in v:
            if len(value) < 1:
                d[k] = v
                continue
    return d



  
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