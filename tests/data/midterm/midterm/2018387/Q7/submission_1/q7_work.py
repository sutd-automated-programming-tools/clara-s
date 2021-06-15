def decompose (p):
    #decompose 2 pound, find left over, pass over
    count2pd = range(p, -1, -200)
    #decompose 1 pound, find left over, pass over
    count1pd = range(p, -1, -100)
    #decompose 50p, find left over, pass over
    count50p = range(p, -1, -50)
    #decompose 20p, find left over, pass over
    count20p = range(p, -1, -20)
    #decompose 10p, find left over, pass over
    count10p = range(p, -1, -10)
    #decompose 5p, find left over, pass over
    count5p = range(p, -1, -5)
    #decompose 2p, find left over, pass over
    count2p = range(p, -1, -2)
    #decompose 1p, find left over, pass over
    count1p = range(p, -1, -1)
    count = 1
    return count