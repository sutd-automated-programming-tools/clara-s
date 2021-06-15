#qn6
#PART A
def read_stations(f):
    file=open(f,'r')
    output_dict={'EastWestLine (EW)':0 , 'EastWestLine (CG)':0, 'NorthSouthLine':0}
    lst1=[]
    lst2=[]
    lst3=[]
    raw_data=file.readlines()
    for aline in raw_data[2:7]:
        element1=aline.strip('\n').split(',')
        lst1.append(element1)
    output_dict['EastWestLine (EW)']=lst1
    
    for aline in raw_data[10:11]:
        element2=aline.strip('\n').split(',')
        lst2.append(element2)
    output_dict['EastWestLine (CG)']=lst2
    
    for aline in raw_data[13:]:
        element3=aline.strip('\n').split(',')
        lst3.append(element3)
    output_dict['NorthSouthLine']=lst3
    return output_dict
    
#PART B
def get_station(mrt):
