# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    x5 = 0
    x6 = 0
    x7 = 0
    x8 = 0
    solution = 0
    for x1i in range(pence+1):
        x1=x1i
        if(x1+x2+x3+x4+x5+x6+x7+x8<pence):
            for x2i in range(pence+1):
                x2=x2i
                if(x1+x2+x3+x4+x5+x6+x7+x8<pence):
                    for x3i in range(pence+1):
                        x3=x3i
                        if(x1+x2+x3+x4+x5+x6+x7+x8<pence):
                            for x4i in range(pence+1):
                                x4=x4i
                                if(x1+x2+x3+x4+x5+x6+x7+x8<pence):
                                    for x5i in range(pence+1):
                                        x5=x5i
                                        if(x1+x2+x3+x4+x5+x6+x7+x8<pence):
                                          for x6i in range(pence+1):
                                              x6=x6i
                                              if(x1+x2+x3+x4+x5+x6+x7+x8<pence):
                                                  for x7i in range(pence+1):
                                                      x7=x7i
                                                      if(x1+x2+x3+x4+x5+x6+x7+x8==pence):
                                                           solution+=1
                                                           x8=0
                                              else:
                                                  x7=0
                                                  solution+=1
                                                  break
                                        else:
                                            x6=0
                                            solution+=1
                                            break
                                else:
                                    x5=0
                                    solution+=1
                                    break
                        else:
                            x4=0
                            solution+=1
                            break
                else:
                    x3=0
                    solution+=1
                    break
        else:
            x2=0
            solution+=1
            break
    else:
        x1=0
        solution+=1
        break
    return solution