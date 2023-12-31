# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
# Pollard's rho to factorize a number n = pq
# expected O(n^(1/4) * log n)

# (x^2+1) mod n
def poly(n: int):
    return lambda x: (x*x+1) % n

# greatest common divisor (Euclid's algorithm)
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Pollard's rho algorithm
def pollardrho(n: int) -> int: 
    g = poly(n)
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = gcd(abs(x - y), n)
    if d == n:
        raise RuntimeError("failed to factorize")
    return d

if __name__ == "__main__":
    for n in [20,500,1071,10_323, (1238926361552897 * 93461639715357977769163558199606896584051237541638188580280321)]:
        factor = pollardrho(n)
        print(n, factor, (n % factor == 0))
