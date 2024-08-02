a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range (2,len(a)+1 ):
    mn = []
    k = 2
    m = i
    n = m
    while k* k <= n:
        while n % k == 0:
            mn.append (k)
            n = n / k
        k = k + 1
    if n >=1:
        mn.append (n)
        if len (mn) == 1:
            primes.append (m)
        else:
            not_primes.append (m)
print ('Простые числа:', primes, 'Не простые числа:', not_primes)