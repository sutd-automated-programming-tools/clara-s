def read_station(f):
    f = open(f,'r')
    f = f.readlines()
    lines = {}
    lst=[]
    for fi in f:
        line=fi.strip().split()
        lst.append(line)
    for i in range(0,5,2):
        line_name = lst[i].split('=')
        line_name = line_name[1]
        lines[line_name] = lst[i+1]
    return lines




# In[ ]:


def get_stationline(mrt):
    dic = {}
    for key in mrt:
        for station in mrt[key]:
            if station in dic:
                dic[station].append(key)
            else:
                dic[station] = key
    return dic 
            
            


# In[ ]:


def get_interchange(stationline):
    interchange = {}
    for station in stationline:
        if len(stationline[station])>1:
            interchange[station] = stationline[station]
    return interchange


# In[ ]:


def find_path(f,start,end):
    lines = read_station(f)
    dic = get_stationline(lines)
    interchange = get_interchange(lines)
    
    
    for i in dic[start]:
        for a in dic[end]:
            if i == a:
                path = lines[a]
                path = lines[lines.index(start):lines.index(end)+1]
                return path

