from itertools import combinations
def decompose(pence):
    dem = [200, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    remainder = pence
    correct = []
    for curr in dem:
        if remainder > 0:
            old = remainder
            remainder = remainder%curr
            if remainder != old:
                correct.append(curr)
        if remainder == 0:
            count += 1
    for i, change in enumerate(correct):
        iter_correct = correct[i+1:]
        print(x for x in combinations(iter_correct, 2))
    return count