# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

from random import randint

def fisheryates(xs):
    n = len(xs)
    for i in range(n):
        j = randint(i, n - 1)
        xs[i], xs[j] = xs[j], xs[i]
    return xs

if __name__ == "__main__":
    xs = [1,2,3,4,5,6]
    print(xs)
    fisheryates(xs)
    print(xs)

