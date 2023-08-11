# https://en.wikipedia.org/wiki/Jenkins_hash_function
# http://www.burtleburtle.net/bob/hash/doobs.html

def jenkinshash(bs: bytes):
    h = 0
    for b in bs:
        h += b 
        h &= 0xFFFFFFFF
        h += h << 10
        h &= 0xFFFFFFFF
        h ^= h >> 6
        h &= 0xFFFFFFFF
    h += h << 3
    h &= 0xFFFFFFFF
    h ^= h >> 11
    h &= 0xFFFFFFFF
    h += h << 15
    h &= 0xFFFFFFFF
    return (h & 0xFFFFFFFF)

if __name__ == "__main__":
    data = "The quick brown fox jumps over the lazy dog".encode('utf-8')
    print(hex(jenkinshash(data)))
