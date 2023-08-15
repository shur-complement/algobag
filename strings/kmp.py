# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# Searches for occurrences of a word within a text 
# Time:  Θ(m) preprocess
# Time:  Θ(n) match
# Space: Θ(m)

def kmp_search(haystack, needle):
    if len(haystack) == 0 or len(needle) == 0: return []
    T = build_table(needle)
    j, k = 0, 0
    matches = []
    while j < len(haystack):
        if needle[k] == haystack[j]:
            j += 1
            k += 1
            if k == len(needle):
                matches.append(j - k)
                k = T[k]
        else:
            k = T[k]
            if k < 0:
                j += 1
                k += 1
    return matches

def build_table(needle):
    T = [0]*(len(needle)+1)
    T[0] = -1
    position, candidate = 1, 0
    while position < len(needle):
        if needle[position] == needle[candidate]:
            T[position] = T[candidate]
        else:
            T[position] = candidate
            while candidate >= 0 and needle[position] != needle[candidate]:
                candidate = T[candidate]
        position += 1
        candidate += 1
    T[position] = candidate
    return T

if __name__ == "__main__":
    print(kmp_search("foobarbazbar", "bar"))
    print(kmp_search("", "foo"))
