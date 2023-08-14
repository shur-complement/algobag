BUCKETS = 8
def count_sort(xs):
    buckets = [0] * (1<<BUCKETS)
    for x in xs:
        buckets[x] += 1
    j = 0
    for i,c in enumerate(buckets):
        for _ in range(c):
            xs[j] = i
            j += 1

if __name__ == "__main__":
    xs = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
    print(xs)
    count_sort(xs)
    print(xs)

