# Miller-Rabin Primality test
# checks whether a given number is *probably* prime.
# Time: O(k log^3 n)

from random import randint

def miller_rabin(n: int, k: int) -> bool:

    if n < 2: return False
    elif n <= 3: return True
    elif n % 2 == 0: return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

if __name__ == "__main__":
    NUMS = [
        15,
        81,
        219393505127470997364893003951,
        835416756268191626619132356767,
        647664498883831924196175418027,
        844894497809932163874202076083,
        790108262029434974440938508481,
    ]
    for i in NUMS:
        print(i, miller_rabin(i, 40))
