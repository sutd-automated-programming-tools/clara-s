def nroot(n, i, num):
  if num >= 0:
    x = 1
    
    no = 0
    for no in range (i):
        f = x**n - num
        fprime = n*x**(n-1)
        x = x - f/fprime                   
        no += 1
  return round (x,3)


def nroot_complex (n, i, num):
   if n%2 == 0:
    if num <0:
        positivenum = abs(num)
        
        x = nroot (n, i, positivenum)
        x = round (x, 3)
    return (x*1j)

   elif n%2 !=0:
       if num <0:
           positivenum = abs(num)
        
           x = nroot (n, i, positivenum)
           x = round (x, 3)
   return (-x)