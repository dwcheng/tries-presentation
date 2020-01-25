import collections
from typing import List, Dict


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children: Dict[str, TrieNode] = {}
        self.partial = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        partial = []
        for c in word:
            partial.append(c)
            if not cur.children.get(c):
                cur.children[c] = TrieNode()
                cur.children[c].partial = "".join(partial)
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        stack = collections.deque()
        stack.append(trie.root)
        res = ""

        while stack:
            cur = stack.pop()
            if len(cur.partial) > len(res) or (len(cur.partial) == len(res) and cur.partial < res):
                res = cur.partial
            for c in cur.children.values():
                if c.isWord:
                    stack.append(c)

        return res
