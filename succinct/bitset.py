# https://en.wikipedia.org/wiki/Bit_array

from math import ceil

BITS = 32

class BitSet:

    def __init__(self, nbits):
        self.data = [0] * int(ceil(nbits / 32))

    def __len__(self):
        return len(self.data) * BITS

    def set(self, i):
        mask = 1 << (i % BITS)
        idx = i // BITS
        self.data[idx] |= mask

    def get(self, i):
        mask = 1 << (i % BITS)
        idx = i // BITS
        return self.data[idx] & mask > 0

    def clear(self, i):
        mask = 1 << (i % BITS)
        idx = i // BITS
        self.data[idx] &= ~mask

if __name__ == "__main__":
    bs = BitSet(32)
    bs.set(0)
    bs.set(1)
    print(bs.get(0))
    print(bs.get(1))
    print(bs.get(2))
    print(bs.get(31))
    print(len(bs))
    bs.clear(0)
    bs.clear(1)
    print(bs.get(0))
    print(bs.get(1))
