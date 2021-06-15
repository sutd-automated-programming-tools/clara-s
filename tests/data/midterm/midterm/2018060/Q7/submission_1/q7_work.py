# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    if pence != 1:
        two_pound = pence//200
        mid = pence%200
        one_pound = mid//100
        mid = mid%100
        fifty = mid//50
        mid = mid%50
        twenty = mid//20
        mid = mid%20
        ten = mid//10
        mid = mid%10
        five = mid//5
        mid = mid$%5
        two = mid//2
        mid = mid%2
        one = mid//1
        return two_pound * decompose(200)   + one_pound * decompose(pence)
    