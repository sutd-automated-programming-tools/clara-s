def decompose(pence):
     coins = [200, 100, 50, 20, 10, 5, 2, 1]
     for i in coins:
         pence2 = pence - i
         if pence2 < 1:
             count =  0
         elif pence2 == 0:
             count =  1
         else:
             try:
                 count += decompose(pence2)
             except:
                 count = decompose(pence2)
     return count