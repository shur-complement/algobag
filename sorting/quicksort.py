def quick_sort(xs):
    if len(xs) < 2: return
    quick_sort_impl(xs, 0, len(xs)-1)

def quick_sort_impl(xs, lo, hi):
    if lo >= hi: return
    pi = partition(xs, lo, hi)
    quick_sort_impl(xs, lo, pi - 1) # left
    quick_sort_impl(xs, pi + 1, hi) # right

def partition(xs, lo, hi):
    pivot = xs[hi]
    i = lo - 1
    for j in range(lo, hi):
        if xs[j] <= pivot:
            i = i + 1
            xs[i], xs[j] = xs[j], xs[i]
    xs[i + 1], xs[hi] = xs[hi], xs[i + 1]
    return i + 1

if __name__ == "__main__":
    xs = [1,2,3,4,5,1,2,3,4,5]
    print(xs)
    quick_sort(xs)
    print(xs)
