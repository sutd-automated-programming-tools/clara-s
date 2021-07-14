pseudocode

import cmath

first, i would create two functions named nroot and nroot_complex

in the body of both functions, i would write down the formulae provided on the exam sheet, and insert
the value of the parameters provided. 

value= output of the parameters in the formulae

return value



then, i would create a third function, named testvalue(n), which basically tests whether the value of 
n is positive or negative.

If n is postive, then 
    value=nroot(n)

else:
    value=nroot_complex(n)
    
return value