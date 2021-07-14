def detereminant(matrix):
    for i in matrix:
        for x in i:
            if len(x)!=len(i):
                return None 
            else: