def num(n):
    c = 0
    for number in range(1, n + 1):
        if n % number == 0:
            c += 1
    return c

def max(m, n):
    max_num = m
    max_divisors = 0
    for number in range(m, n + 1):
        divisors = num(number)
        if divisors > max_divisors:
            max_num = number
            max_divisors = divisors
    return max_num