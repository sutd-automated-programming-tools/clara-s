PSEUDOCODE

open the text file provided

file=open("mrt_line_short.txt","r")

iterate through the file with while loop. If the line is equal to the name of the station line,
create a dictionary with the key being the name of the line, and assign its value to the an empty list

while True:
    line=line.readline()
    
    if len(line)==0:
        break

next, after creating a dictionary with the keys as the names of the stations, equate innerlist as the empty list assigned to its key

dct={namea:[], nameb:[], namec:[]


for key in dct.keys():
    innerlist=dct[key]
    if line==key is False:
        innerlist.append(line)
        
    else:
        continue
    
the final output should be the dictionary created with the correct keys and values

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