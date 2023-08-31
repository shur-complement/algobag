# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# algorithm for finding all prime numbers up to a given limit
# Time: O(n log log n)
# Space: O(N)

from math import sqrt, ceil

def sieve(n: int) -> int:
    if n < 2: return False
    isPrime = [True] * n
    for i in range(2, ceil(sqrt(n))):
        if isPrime[i]:
            i2 = i*i
            j = i2
            k = 0
            while j < n:
                isPrime[j] = False
                j = i2 + k*i
                k += 1
    return [i for i in range(2, len(isPrime)) if isPrime[i]]

if __name__ == "__main__":
    primes = list(map(str, sieve(282)))
    print(", ".join(primes[0:20]))
    print(", ".join(primes[20:40]))
    print(", ".join(primes[40:60]))
