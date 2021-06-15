def newton(expr, expr_prime, start):
    return start - (expr(start)/expr_prime(start))

def newton_iter(expr, expr_prime, start, iterations):
    '''Many rounds of Newton's method'''
    # keep track
    results = [start]
    errors = [expr(start)]
    
    for x in range(iterations):
        try:
            # single round, remember the result of newton and error (distance from 0)
            results.append(newton(expr, expr_prime, results[-1]))
            errors.append(expr(results[-1]))
        except ZeroDivisionError:
            # bad stuff
            print('Derivative at x={} is 0!'.format(results[-1]))
            break
        except OverflowError:
            print('Result too big at x={}!'.format(results[-1]))
            break
    
    return results, errors

def nroot(root_power, steps, num):
    expr = lambda x: x ** root_power - num
    expr_prime = lambda x: root_power * x ** (root_power - 1)
    
    results, errors = newton_iter(expr, expr_prime, 1, steps)
    return round(results[-1], 3)

def nroot_complex(root_power, steps, num):
    if root_power % 2 == 0:
        return complex(0, nroot(root_power, steps, abs(num)))
    else:
        return -nroot(root_power, steps, abs(num))