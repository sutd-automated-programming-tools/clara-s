import pickle

def read_stations(f):
    infile = open('mrt_lines_short.txt','r')
    outfile =open('mrtdictionary.txt','w')
    dictionary = {}
    lista = []
    dictionary['EastWestLine (EW)'] = 'a']
    dictionary['EastWestLine (CG)'] = 'b']
    dictionary['NorthSouthLine (NS)'] = 'c']
    
    aline = infile.readline()
       
aline = infile.readline()

    infile.close()
    outfile.close()
    
                
"""
basically here i am opening the file, creating a dictionary, and by spliting up lines 2,5,8 from the original text file,
i then enter them into each of the 3 values i have created in the new dictionary. then the dictionary will be placed into the outfile
"""

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


''' here with parts ABC done, I should have
from a) a list of all stations together
b) list where each station is a key and the value is a list of all possible lines
    and if interchange, then all the lines calling at this interchange
c)this is the same as b), but only interchange.
so for d, what i want to do is to create a function
first calling b, because b is all the stations having its own key,
then using c to call for hte lines