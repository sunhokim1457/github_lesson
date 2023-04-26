def sum_fraction(numer1, denom1, numer2, denom2):

    # 최소공배수(분수 덧셈 계산)
    leastMultiple = max(denom1, denom2)
    i = 1
    while not (leastMultiple % denom1 == 0 and leastMultiple % denom2 == 0):
        i += 1
        leastMultiple = denom1 * i

    # 계산된 분자
    numer = numer1 * (leastMultiple // denom1) + numer2 * (leastMultiple // denom2) 
    
    # 최대공약수(기약분수 계산)
    GreatestMeasure = min(leastMultiple, numer)
    
    while not (leastMultiple % GreatestMeasure == 0 and numer % GreatestMeasure == 0):
        GreatestMeasure -= 1
    
    return [numer / GreatestMeasure , leastMultiple / GreatestMeasure]