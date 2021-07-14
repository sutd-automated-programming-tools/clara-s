# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    count = 1
    if pence > 2:
        number_of_coins = pence//2
        remaining_coins = pence%2
        count = count+1
        if number_of_coins > 1:
            for i in range(number_of_coins-1):
                number_of_coins = number_of_coins - 1
                remaining_coins = remaining_coins + 2
                count = count + 1
        number_of_coins1 = pence//5
        remaining_coins1 = pence%5
        count = count + 1
        if number_of_coins1 > 1:
            for j in range(number_of_coins1 - 1):
                number_of_coins1 = number_of_coins1 - 1
                remaining_coins1 = remaining_coins1 + 5
                count = count + 1
        number_of_coins2 = pence//10
        remaining_coins2 = pence%10
        count = count + 1
        if number_of_coins2 > 1:
            for k in range(number_of_coins2 - 1):
                number_of_coins2 = number_of_coins2 - 1
                remaining_coins2 = remaining_coins2 + 10
                count = count + 1
        number_of_coins3 = pence//20
        remaining_coins3 = pence%20
        count = count + 1
        if number_of_coins3 > 1:
            for l in range(number_of_coins3 - 1):
                number_of_coins3 = number_of_coins3 - 1
                remaining_coins3 = remaining_coins3 + 20
                count = count + 1
        number_of_coins4 = pence//50
        remaining_coins4 = pence%50
        count = count + 1
        if number_of_coins4 > 1:
            for m in range(number_of_coins4 - 1):
                number_of_coins4 = number_of_coins4 - 1
                remaining_coins4 = remaining_coins4 + 50
                count = count + 1
    return count