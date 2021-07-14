import pickle

def read_stations(f):
    output = dict()
    for line in (f):
        s= ' '
        ls = list(line.strip)
        if ls[0] == '=':
            ls.pop(len(ls)-1)
            ls.pop(0)
            s = ''
            for i in range(len(ls)):
                s+=ls[i]
            
        else:
            sublist = line.strip('\n')
            sublist = sublist.split(' ')
            sublist = [float(i) for i in sublist]
            ls.append(sublist)
            
    return output

def get_stationline(mrt):
    output ={}
    for k,v in mrt.items:
        for i in range(len(v)):
            if v[i] not in output:
                output[v[i]] = [k]
            else:
                output[v[i]] += [k]
    return output

def get_interchange(stationline):
    output = {}
    for k,v in stationline.items:
        if len(v) > 1:
            output[k] = v
    return output

def find_path(f,start,end):
    output = []
    odic = read_stations(f)
    startlines = odic[start]
    endlines = odic[end]
    for line in startlines:
        if line in endlines:
            allstations = odic[line]
            si = allstations.index(start)
            ei = allstations.index(end)
            if si<ei:
                output = allstations[si:ei+1]
            else:
                output = allstations[ei:si+1]
                output.reverse()
        else:
            interchange = get_interchange(startlines)
            for eline in endlines:
                for k,v in interchange.items:
                    if eline in v:
                        thechange = k
                        transfer1s = odic[line]
                        transfer2s = odic[eline]
                        si = transfer1s.index(start)
                        ti = transfer1s.index(thechange)
                        t2i = transfer2s.index(thechange)
                        ei = transfer2s.index(end)
                        if si<ti:
                             output1 = transfer1s[si:ti+1]
                        else:
                            output1 = transfer1s[ti:si+1]
                            output1.reverse()
                        if t2i<ei:
                            output2 = transfer2s[t2i+1:ei+1]
                        else:
                            output2 = transfer2s[ei:t2i]
                            output2.reverse()                        
                        output = output1 + output2
                    else:
                        output = None
    return output

  
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