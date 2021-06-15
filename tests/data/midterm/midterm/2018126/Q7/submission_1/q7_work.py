def decompose(amt):
    binary_list = [1, 2, 5, 10, 20, 50, 100, 200]
    
    count = 0
    for x1 in range(amt):
        for x2 in range(amt):
            for x3 in range(amt):
                for x4 in range(amt):
                    for x5 in range(amt):
                        for x6 in range(amt):
                            for x7 in range(amt):
                                for x8 in range(amt):
                                    
  
                                    if x1 + x2 * 2 + x3 * 5 + x4 * 10 + x5 * 20 + x6 * 50 + x7 * 100 + x8 * 200 == amt:
                                        count += 1
                            
    return count + 1