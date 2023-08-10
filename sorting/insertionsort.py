# https://en.wikipedia.org/wiki/Insertion_sort
# Time: O(N^2)
# Space: O(1)

def insertion_sort(xs):
    for i in range(1, len(xs)):
        t = xs[i]
        j = i
        while j > 0 and t < xs[j-1]:
            xs[j] = xs[j-1]
            j -= 1
        xs[j] = t

if __name__ == "__main__":
    xs = [1,2,3,4,5,1,2,3,4,5,]
    print(xs)
    insertion_sort(xs)
    print(xs)
