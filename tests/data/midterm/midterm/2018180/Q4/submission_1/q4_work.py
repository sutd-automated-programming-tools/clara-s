def deter2(n):
    a=0
    b=len(n[0])-1
    det=0
    while a<len(n):
            if a%2==0:
                det+= n[0][a]*n[1][a+1]
                
            else:
                det -= n[0][a]*n[1][a-1]
            a+=1
    return det

def determinant(n):
    if len(n) != len(n[0]) or len(n)<0 or len(n)>3 or len(n[0])<0 or len(n[0])>3:
        return None
    if len(n)==1:
        return n[0][0]
    elif len(n)==2:
        return deter2(n)
    elif len(n)==3:
        det=0
        smaller=[]
        for i in range(len(n)):
            smaller.append([])
            if i == 0:
                smaller[i].append([n[1][1],n[1][2]])
                smaller[i].append([n[2][1],n[2][2]])
            if i==1:
                smaller[i].append([n[1][0],n[1][2]])
                smaller[i].append([n[2][0],n[2][2]])
            if i==2:
                smaller[i].append([n[1][0],n[1][1]])
                smaller[i].append([n[2][0],n[2][1]])
        print(smaller)
        print(deter2(smaller[1]))
        for j in range(len(n[0])):
            if j%2 ==0:
                det+= n[0][j]*deter2(smaller[j])
            else:
                det -=n[0][j]*deter2(smaller[j])
        return det
