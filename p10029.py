import sys
import cProfile
from itertools import chain


class Word:
    def __init__(self, s):
        self.s = s
        self.next_in_ladder = set()
        self.discovered = False
        self.longest_found_path = 1

    def __repr__(self):
        return self.s

    def __lt__(self, other):
        return self.longest_found_path < other.longest_found_path

    def add_word(self, w):
        self.next_in_ladder.add(w)


class Trie:
    def __init__(self, word):
        ''' Word: none or instance of Word'''
        self.word = word
        self.subtrie = {}

    def insert_word(self, word, str_left):
        c = str_left[0]
        if len(str_left) == 1:
            if c in self.subtrie:
                self.subtrie[c].word = word
            else:
                self.subtrie[c] = Trie(word)
        else:
            if c not in self.subtrie:
                self.subtrie[c] = Trie(None)
            self.subtrie[c].insert_word(word, str_left[1:])

    def find_word(self, str_left):
        c = str_left[0]
        if c not in self.subtrie:
            return False
        if len(str_left) == 1:
            return self.subtrie[c].word
        return self.subtrie[c].find_word(str_left[1:])

    def find_subtrie(self, word):
        if not word:  # reached end of word
            return self
        if word[0] not in self.subtrie:
            return None
        else:
            return self.subtrie[word[0]].find_subtrie(word[1:])


def deletion_steps(word):
    """ yields all single edit steps of word"""
    # Deletions
    for i in range(1, len(word)):
        a = word[:i - 1]
        b = word[i:]
        yield word[:i - 1] + word[i:]
    yield word[:-1]


def mutation_steps(word, trie, index):
    # Yield all mutations at current position
    # Call one step deeper
    if index == len(word):
        return
    s = [c for c in word]
    original_val = s[index]
    for c in trie.subtrie.keys():
        if c < original_val:
            s[index] = c
            yield ''.join(s)
    if original_val in trie.subtrie:
        for s in mutation_steps(word, trie.subtrie[original_val], index + 1):
            yield s


def insertion_steps(word, trie):
    for i in range(len(word)):
        current_trie = trie.find_subtrie(word[:i])
        if not current_trie:
            continue
        s = [c for c in word]  # could just reassign two indices every time instead of rebuilding
        s.insert(i, '')
        original_val = s[i + 1]
        for c in current_trie.subtrie.keys():
            if c <= original_val:
                s[i] = c
                yield ''.join(s)


def edit_steps(word, trie):
    return chain(deletion_steps(word), mutation_steps(word, trie, 0), insertion_steps(word, trie))


def valid_edit_steps(word, trie):
    for x in edit_steps(word, trie):
        val = trie.find_word(x)  # None or instance of Word
        if val:
            yield val


def build_trie():
    result = []
    trie = Trie(None)
    i = 0
    with open("words.txt", 'r') as f:
        #for next_s in sys.stdin:
        for next_s in f.readlines():
        # if i % 1000 == 0:
            # print(i)
            next_s = next_s.rstrip()
            if not next_s:
                continue
            next_word = Word(next_s)
            for w in valid_edit_steps(next_s, trie):
                next_word.longest_found_path = max(next_word.longest_found_path, w.longest_found_path + 1)
            trie.insert_word(next_word, next_s)
            result.append(next_word)
            i += 1
    return max(result).longest_found_path


def main():
    cProfile.run('build_trie()')
    #print(build_trie())


if __name__ == '__main__':
    main()
