# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
# Searches for occurrences of a word within a text 
# Time:  Θ(m) preprocess
# Time:  Θ(n) match
# Space: Θ(m)

def kmp_search(haystack, needle):
    if len(haystack) == 0 or len(needle) == 0: return []
    fail = build_table(needle)
    j, k = 0, 0
    matches = []
    while j < len(haystack):
        if needle[k] == haystack[j]:
            j += 1
            k += 1
            if k == len(needle):
                matches.append(j - k)
                k = fail[k]
        else:
            k = fail[k]
            if k < 0:
                j += 1
                k += 1
    return matches

def build_table(needle):
    fail = [0]*(len(needle)+1)
    fail[0] = -1
    position, candidate = 1, 0
    while position < len(needle):
        if needle[position] == needle[candidate]:
            fail[position] = fail[candidate]
        else:
            fail[position] = candidate
            while candidate >= 0 and needle[position] != needle[candidate]:
                candidate = fail[candidate]
        position += 1
        candidate += 1
    fail[position] = candidate
    return fail

if __name__ == "__main__":
    print(kmp_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD"))
