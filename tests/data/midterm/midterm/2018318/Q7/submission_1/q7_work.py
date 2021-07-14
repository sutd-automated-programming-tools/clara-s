# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    coins = [1,2,5,10,20,50,100,200]
    output= []
    for i in coins:
        while pence >= i:
            if pence%1==0:
                output.append(1)
                
                if pence%5==0:
                    output.append(1)
            #if (pence%2)%1==0:
                #output.append(2)
             
            #if (((pence%5)%2)%1)==0:
                #output.append(3)
            
            
            
                return(sum(output))


# find the number of combination 
    
        

        
        
    
    