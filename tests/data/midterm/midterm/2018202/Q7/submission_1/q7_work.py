def decompose(pence):
    sol = 0
    for n1 in range(0, pence + 1):
        for n2 in range(0, pence+1):
            for n3 in range(0, pence+1):
                for n4 in range(0, pence+1):
                    for n5 in range(0, pence+1):
                        for n6 in range(0, pence+1):
                            for n7 in range(0, pence+1):
                                for n8 in range(0, pence+1):
                                    if n1 + (2*n2) + (5*n3) + (10*n4) +(20*n5) + (50*n6) + (100*n7) +(200*n8) == pence:
                                        sol += 1
    return sol