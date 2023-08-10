# Heap Sort
# https://en.wikipedia.org/wiki/Heapsort
# Time O(N log N)
# Space O(1)

def heap_sort(xs, count):
    if len(xs) < 2: return
    _heapify(xs, count)
    end = count - 1
    while end > 0:
        xs[end], xs[0] = xs[0], xs[end]
        end -= 1
        _sift_down(xs, 0, end)

def _heapify(xs, count):
    start = _parent(count - 1)
    while start >= 0:
        _sift_down(xs, start, count - 1)
        start -= 1

def _sift_down(xs, start, end):
    root = start
    while _left_child(root) <= end:
        child = _left_child(root)
        swap = root
        if xs[swap] < xs[child]:
            swap = child
        if child+1 <= end and xs[swap] < xs[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            xs[root], xs[swap] = xs[swap], xs[root]
            root = swap

def _parent(i):
    return (i-1) >> 1

def _left_child(i):
    return 2*i + 1

if __name__ == "__main__":
    xs = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
    print(xs)
    heap_sort(xs, len(xs))
    print(xs)
