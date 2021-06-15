def determinant(matrix):
    x = []
    y = []
    z = []

    no1 = len(x)
    no2 = len(y)
    no3 = len(z)
    
    if no1 != no2 or no1 != no3 or no2 != no3:
        return None
    else:
        determinant = no1[1]*(no2[2]*no3[3] - no2[3]*no3[2]) - no1[2]*(no2[1]*no3[3] - no2[3]*no3[1]) + no1[3]*(no2[1]*no3[2] - no2[2]*no3[1])