# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    num_of_coins = 8
    return coin_combination(coins, num_of_coins, pence)


def coin_combination(coins, num_of_coins, summ):
    idx = num_of_coins - 1
    if summ < 0:
        return 0
    elif summ == 0:
        return 1
    elif idx < 0:
        return 0
    elif idx == 0:
        return 1
    else:
        output = 0
        count = 0
        while(summ - count * coins[idx] >= 0):
            output += coin_combination(coins, num_of_coins-1, summ - count * coins[idx])
            count += 1
        return output