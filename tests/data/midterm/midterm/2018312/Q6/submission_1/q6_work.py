import pickle

def read_stations(f):
    l ={'EastWestLine (EW)':[
Pasir Ris, Tampines, Simei, Tanah Merah, Bedok, Kembangan, Eunos, Paya Lebar, Aljuned, Kallang, Lavender, Bugis, City Hall, Raffles Place, Tanjong Pagar, Outram Park, Tiong Bahru, Redhill, Queenstown, Commonwealth, Buona Vista, Dover, Clementi, Jurong East, Chinese Garden, Lakeside, Boon Lay, Pioneer, Joo Koon, Gul Circle, Tuas Crescent, Tuas West Road, Tuas Link]

'EastWestLine (CG)':[Tanah Merah, Expo, Changi Airport]

'NorthSouthLine':[Jurong East, Bukit Batok, Bukit Gombak, Choa Chu Kang, Yew Tee, Kranji, Marsiling, Woodlands, Admiralty, Sembawang, Canberra, Yishun, Khatib, Yio Chu Kang, Ang Mo Kio, Bishan, Braddell, Toa Payoh, Novena, Newton, Orchard, Somerset, Dhoby Ghaut, City Hall, Raffles Place, Marina Bay, Marina South Pier]}
    d ={}
    for line in f:
        line.strip()

        if line.split()[0]:
            l =[]
            d[line.split()[0]] = l
        else:
            l.append(list(line.split()))
    return l

def get_stationline(mrt):
    return list(mrt)

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