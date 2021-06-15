def nroot(n,i,num):
    result = 1
    for idx in range(i):
        result = result - ((result**n - num ) / (n*result))

    return round(result,3)

def nroot_complex(n,i,num):
    result = 1
    if num<0:
        if n %2 == 0:
            num = abs(num)
            for idx in range(i):
                result = result - ((result**n - num ) / (n*result))
            result = round(result,3)
            result *= 1j
        else:
            for idx in range(i):
                result = result - ((result**n - num ) / (n*result))
            result = round(result,3)

    else:
        result = nroot(n,i,num)
        result = round(result,3)

    return result