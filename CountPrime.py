def countPrime(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False 

    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range( i* i, n, i):
                primes[j] = False
    return sum(primes)


#brute-force approach with a very high time complexity
def countPrimes(self, n: int) -> int:
    count = 0

    def isPrime(num):
        if num == 2 or num == 3:
            return True
        if num == 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    for i in range(1, n):
        if isPrime(i):
            count += 1
