# Merge Sort
# https://en.wikipedia.org/wiki/Merge_sort
# Time: O(N log N)
# Space: O(N)

def merge_sort(xs):
    if len(xs) < 2: return
    ys = xs.copy()
    n = len(xs)
    _split_merge(xs, 0, n, ys)

def _split_merge(ys, start, end, xs):
    if end - start <= 1: return
    # split into halves
    mid = (end + start) // 2
    _split_merge(xs, start, mid, ys)    # sort left
    _split_merge(xs, mid, end, ys)  # sort right
    _merge(ys, start, mid, end, xs)

def _merge(ys, start, mid, end, xs):
    i = start
    j = mid
    for k in range(start, end):
        if i < mid and (j >= end or xs[i] <= xs[j]):
            ys[k] = xs[i]
            i = i + 1
        else:
            ys[k] = xs[j]
            j = j + 1

if __name__ == "__main__":
    xs = [1,2,3,4,5,1,2,3,4,5]
    print(xs)
    merge_sort(xs)
    print(xs)
