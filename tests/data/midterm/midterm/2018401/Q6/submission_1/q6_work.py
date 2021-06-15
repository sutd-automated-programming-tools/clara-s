import pickle

def read_stations(f):
    lines = f.readlines() #gives a list with each line as an item
    lines_n = [line.strip('\n') for line in lines] #same thing but with \n stripped
    #print(lines_n)
    dictionary = {}
    for i in lines_n:
        if i == '=EastWestLine (EW)=' or i == '=EastWestLine (CG)=' or i == '=NorthSouthLine=':
            i = i.strip('=')
            dictionary[i] = [] #create a list to store values for each key
            a = i 
            #print(dictionary)
# 
        else:
            mylist = i.split(',')
            
            
            #mystation = mylist.remove('\t')
            
            #print(mystation)
            
            for stuff in mylist:
                if stuff != '':
                    dictionary[a].append(stuff)
            
    return dictionary   

def get_stationline(mrt):
    pass

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