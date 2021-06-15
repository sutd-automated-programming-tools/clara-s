# MID-TERM EXAM: QUESTION 5
import math
def nroot(n,t,num):
    ans = num ** (1/n)
    return round(ans,3)

def nroot_complex(n,t,num):
      if n % 2 == 0:
        ans3 = nroot(n,t,-num)
        ans4 = str(ans3) + 'j'
        return ans4
      elif n % 2 != 0:
        ans = nroot(n,t,-num)
        answ = -ans
        return answ
          
            