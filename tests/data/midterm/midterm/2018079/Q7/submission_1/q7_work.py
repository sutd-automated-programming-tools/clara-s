# MID-TERM EXAM: QUESTION 7
count = 0
def decompose(pence):
    if pence>=200:
        remainder = pence%200
        count += 1
        if remainder == 0:
            return count
        elif remainder >200:
            return decompose (remainder)
        else:
            remainder = remainder%100
            count += 1
            if remainder == 0:
            return count
            elif remainder >100:
                return decompose (remainder)
            else:
                remainder = remainder%50
                count += 1
                if remainder == 0:
                    return count
                elif remainder >50:
                    return decompose(remainder)
                else:
                    remainder = remainder%20
                    count += 1
                    if remainder == 0:
                        return count
                    elif remainder > 20:
                        return decompose (remainder)
                    else:
                        remainder = remainder%10
                        count+=1
                        if remainder == 0:
                            return count
                        elif remainder > 10:
                            return decompose(remainder)
                        else:
                            remainder = remainder%5
                            count += 1
                            if remainder ==0:
                                return count
                            elif remainder>5:
                                return decompose (remainder)
                            else:
                                remainder = remainder % 2
                                count += 1
                                if remainder == 0:
                                    return count
                                elif remainder>2:
                                    return decompose(remainder)
                                else: 
                                    count+=remainder
                                    return count
    elif pence>=100:
        remainder = pence%100
            count += 1
            if remainder == 0:
            return count
            elif remainder >100:
                return decompose (remainder)
            else:
                remainder = remainder%50
                count += 1
                if remainder == 0:
                    return count
                elif remainder >50:
                    return decompose(remainder)
                else:
                    remainder = remainder%20
                    count += 1
                    if remainder == 0:
                        return count
                    elif remainder > 20:
                        return decompose (remainder)
                    else:
                        remainder = remainder%10
                        count+=1
                        if remainder == 0:
                            return count
                        elif remainder > 10:
                            return decompose(remainder)
                        else:
                            remainder = remainder%5
                            count += 1
                            if remainder ==0:
                                return count
                            elif remainder>5:
                                return decompose (remainder)
                            else:
                                remainder = remainder % 2
                                count += 1
                                if remainder == 0:
                                    return count
                                elif remainder>2:
                                    return decompose(remainder)
                                else: 
                                    count+=remainder
                                    return count
    elif pence>=50:
        remainder = pence%50
                count += 1
                if remainder == 0:
                    return count
                elif remainder >50:
                    return decompose(remainder)
                else:
                    remainder = remainder%20
                    count += 1
                    if remainder == 0:
                        return count
                    elif remainder > 20:
                        return decompose (remainder)
                    else:
                        remainder = remainder%10
                        count+=1
                        if remainder == 0:
                            return count
                        elif remainder > 10:
                            return decompose(remainder)
                        else:
                            remainder = remainder%5
                            count += 1
                            if remainder ==0:
                                return count
                            elif remainder>5:
                                return decompose (remainder)
                            else:
                                remainder = remainder % 2
                                count += 1
                                if remainder == 0:
                                    return count
                                elif remainder>2:
                                    return decompose(remainder)
                                else: 
                                    count+=remainder
                                    return count
    elif pence>=20:
        remainder = pence%20
                    count += 1
                    if remainder == 0:
                        return count
                    elif remainder > 20:
                        return decompose (remainder)
                    else:
                        remainder = remainder%10
                        count+=1
                        if remainder == 0:
                            return count
                        elif remainder > 10:
                            return decompose(remainder)
                        else:
                            remainder = remainder%5
                            count += 1
                            if remainder ==0:
                                return count
                            elif remainder>5:
                                return decompose (remainder)
                            else:
                                remainder = remainder % 2
                                count += 1
                                if remainder == 0:
                                    return count
                                elif remainder>2:
                                    return decompose(remainder)
                                else: 
                                    count+=remainder
                                    return count
    elif pence>=10:
        
        