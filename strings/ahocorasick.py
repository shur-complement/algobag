# Aho Corasick
# Simultaneously match a set of keywords on an input text
# https://dl.acm.org/doi/10.1145/360825.360855
# https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm
# Time: O(N+L+Z), where N is the length of text, L is the length of words to be searched, and Z is the number of matches
# Space: O(L*Q), where L is length of words to be searched, Q is length of alphabet

from collections import defaultdict, deque

ALPHABET_SIZE = 26
FAIL = -1
EMPTY = 0
class AhoCorasick:
    def __init__(self, words):
        NUM_STATES = sum(len(word) for word in words)
        self.out = [EMPTY] * (NUM_STATES + 1)
        self.fail = [FAIL] * (NUM_STATES + 1)
        self.go = [[FAIL] * ALPHABET_SIZE for _ in range(NUM_STATES + 1)]

        for i in range(len(words)):
            words[i] = words[i].lower()

        self.words = words

        self._build_goto()
        self._build_failure()


    def _build_goto(self):
        # Algorithm 2: Construction of the goto function
        k = len(self.words)
        states = 1
        for i in range(k):
            word = self.words[i]
            state = 0
            for char in word:
                c = ord(char) - ord('a')
                if self.go[state][c] == FAIL:
                    self.go[state][c] = states
                    states += 1
                state = self.go[state][c]
            self.out[state] |= (1 << i) # add word i to out set

        # add self-loop from 0->0 for all transitions not in trie
        # this ensures a character is always consumed per machine cycle
        for c in range(ALPHABET_SIZE):
            if self.go[0][c] == FAIL:
                self.go[0][c] = 0

    def _build_failure(self):
        # Algorithm 3: Construction of the failure function (BFS)
        q = deque()
        for c in range(ALPHABET_SIZE):
            s = self.go[0][c]
            if s != 0:
                q.append(s)
                self.fail[s] = 0
        while q:
            r = q.popleft()
            for c in range(ALPHABET_SIZE):
                s = self.go[r][c]
                if s != FAIL:
                    q.append(s)
                    state = self.fail[r]
                    while self.go[state][c] == FAIL:
                        state = self.fail[state]
                    self.fail[s] = self.go[state][c]
                    self.out[s] |= self.out[self.fail[s]]

    def matches(self, text):
        # Algorithm 1: Pattern matching machine
        text = text.lower()
        result = defaultdict(list)
        state = 0
        for i in range(len(text)):
            c = ord(text[i]) - ord('a')
            while self.go[state][c] == FAIL:
                state = self.fail[state]
            state = self.go[state][c]
            for j in range(len(self.words)):
                if self.out[state] & (1 << j):
                    word = self.words[j]
                    result[word].append(i-len(word)+1)
        return result

if __name__ == "__main__":
    words = ["he", "she", "hers", "his"]
    text = "ahishers"

    aho_chorasick = AhoCorasick(words)
    matches = aho_chorasick.matches(text)

    for word in matches:
        n = len(word)
        print(word)
        print([(i,i+n-1) for i in matches[word]])
