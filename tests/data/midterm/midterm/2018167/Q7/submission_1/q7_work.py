# MID-TERM EXAM: QUESTION 7



# for any input value n,the total number of combinations equals to the total number of combinations of its divider and the the total number of combinations of the divider
 
#for example n=5 5%1=0 result+1 5%2=1 result+1 5%5=0 result+1 totalresult =5


def decompose(n):
    result=0
    for i in range(0,n):
        if n%i==0:
            result+=i
        return result
    
        