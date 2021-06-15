def read_stations(f):
    line_name = 'o'
    ew = []
    cg = []
    ns = []
    for line in f:
        line=line.strip()
        if line == '=EastWestLine (EW)=':
            line_name = 'ew'
        elif line == '=EastWestLine (CG)=':
            line_name = 'cg'
        elif line == '=NorthSouthLine=':
            line_name = 'ns'
        elif line_name != 'o':
            if line_name == 'ew':
                line = line.split(', ')
                if line!=['']:
                    ew =line
                #print(line)
            elif line_name == 'cg':
                line= line.split(', ')
                if line!=['']:
                    cg= line
            elif line_name == 'ns':
                line= line.split(', ')
                ns=line
    stations = {'EastWestLine (EW)': ew, 'EastWestLine (CG)': cg, 'NorthSouthLine': ns}
    return stations

f = open('mrt_lines_short.txt', 'r')
print(read_stations(f))