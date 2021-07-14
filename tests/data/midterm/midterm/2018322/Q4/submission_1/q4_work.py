def determinant(M):
    for i in M:
        for j in i:
            if len [i] != len[j]:
                    
                if len[i] == 2:
                    determinant = M[0][0]*M[1][1] - M[0][1]-M[1][0]
                    return (int(determinant))

                if len [i] == 3:
                    determinant = M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
                    return (int(determinant))    
                
            else:
                return None
           
