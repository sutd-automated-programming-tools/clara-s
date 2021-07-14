# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    #1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
    counter = 0
    if pence % 200 < 200:
        twohunleft = pence % 200
        counter += (200 + 100 + 40 + 20 + 10 + 4 + 2 + 1)

        if twohunleft % 100 < 100:
            onehunleft = twohunleft % 100
            counter += (100 + 50 + 20 + 10 + 5 + 2 + 1)

            if onehunleft % 50 < 50:
                fiftyleft = onehunleft % 50
                counter += (50 + 25 + 10 + 5)

                if fiftyleft % 20 < 20:
                    twentyleft = fiftyleft % 20
                    counter += (20 + 10 + 4 + 2 + 1)

                    if twentyleft % 10 < 10:
                        tenleft = twentyleft % 10
                        counter += (10 + 5 + 2 + 1)

                        if tenleft % 5 < 5:
                            fiveleft = tenleft % 5
                            counter += (5 + 1)

                            if fiveleft % 2 < 2:
                                twoleft = fiveleft % 2
                                counter += (2 + 1)
    return counter