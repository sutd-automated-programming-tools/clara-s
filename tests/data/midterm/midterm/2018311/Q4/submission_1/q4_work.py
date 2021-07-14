def determinant(matr):
    if len(matr) == len(matr[0]):
        if len(matr)==1:
            return (matr[0][0])
        if len(matr)==2:
            det=matr[0][0]*matr[1][1]-matr[1][0]*matr[0][1]
            return det
        if len(matr)==3:
            det=0
            k=0
            ls=[]
            for i in range(0,len(matr),1):
                #print(i,k,det,ls)
                if i==0:
                    #print("start")
                    det=(matr[i][0]*(matr[i+1][1]*matr[i+2][2]-matr[i+2][1]*matr[i+1][2]))
                elif i==len(matr)-1:
                    #print("end")
                    det=((-1)**(k))*(matr[i][0]*(matr[i-2][1]*matr[i-1][2]-matr[i-1][1]*matr[i-2][2]))
                else:
                    det=((-1)**k)*(matr[i][0]*(matr[i-1][1]*matr[i+1][2]-matr[i+1][1]*matr[i-1][2]))
                ls.append(det)
                k+=1
        ans=sum(ls)
        return ans
    else:
        return None