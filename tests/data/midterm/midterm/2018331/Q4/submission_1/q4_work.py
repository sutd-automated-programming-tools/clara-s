def determinant(M):
    if len(M)<1 or len(M)>3:
        return None
    if len(M)==1:
        return M[0][0]
    elif len(M)==2:
        for i in M:
            if len(i)!=len(M):
                return None
        return (M[0][0]*M[1][1])-(M[0][1]*M[1][0])
    elif len(M)==3:
        for i in M:
            if len(i)!=len(M):
                return None
        a=M[0][0]
        b=M[0][1]
        c=M[0][2]
        deta=a*determinant([[M[1][1],M[1][2]],[M[2][1],M[2][2]]])
        detb=b*determinant([[M[1][0],M[1][2]],[M[2][0],M[2][2]]])
        detc=c*determinant([[M[1][0],M[1][1]],[M[2][0],M[2][1]]])
        return deta-detb+detc