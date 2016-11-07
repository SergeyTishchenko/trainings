def multiplier(n):
    a = [] #вывод множителей
    b = 2
    while b * b <= n:
        if n % b == 0:
            a.append(b)
            n //= b
        else:
            b += 1
    if n > 1:
        a.append(n)
    return a
