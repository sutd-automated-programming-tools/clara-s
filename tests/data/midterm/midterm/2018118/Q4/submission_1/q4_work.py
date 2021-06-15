def determinant(M):
    #check square
    if len(M)!=len(M[0]):
        return None
    else:
        #check if n=1:
        if len(M)==1:
            return M[0][0]
        #check if n=2:
        elif len(M)==2:
            det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
            return det
        elif len(M)==3:
            det=M[0][0]*determinant([[M[1][1],M[1][2]],[M[2][1],M[2][2]]])-M[0][1]*determinant([[M[1][0],M[1][2]],[M[2][0],M[2][2]]])+M[0][2]*determinant([[M[1][0],M[1][1]],[M[2][0],M[2][1]]])
            return det
