import pickle



def read_stations(file):
    
    lineName = "";
    lineList = []
    output = {};
    
    for line in file:

        if(line[0] == "="):
            
            if(lineName!=""):
                
                output[lineName] = lineList;
                lineList = [];
                
            
            
            lineName = line.strip().replace("=","");
            
        else:
            
            if(line.strip()!=""):
                
                lineList = line.split(",");
                
                
                #Somehow this is not stripping the line list
                for item in lineList:
                    item = item.strip();
                    
                
    output[lineName] = lineList;
    return output;
           

    
    
    

def get_stationline(mrt):
    
    output = {};
    for line in mrt:
        for station in mrt[line]:
            if(station in output):
                output[station] += [line];
            else:
                output[station] = [line];
            
    return output;
    
    
    

def get_interchange(stationline):
    output = {};
    for station in stationline:
        if len(stationline[station])>1:
            
            output[station] = stationline[station];
            
    return output;




            


  
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
        stationsOnLine = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        linesOnStation = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    
    path = [];
    

    
    for line in stationsOnLine:
        
        if start in stationsOnLine[line] and end in stationsOnLine[line]:
            
            addStation = False;
            for station in stationsOnLine[line]:
                if station == start or station == end:
                    addStation = bool(1-addStation);
                
                if addStation:
                    path += [station];
                    
            return path;
            
        
            
    
    
    
    
    
    


    