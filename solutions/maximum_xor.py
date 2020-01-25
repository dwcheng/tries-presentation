class TrieNode:
    def __init__(self):
        self.children = [None, None]


flip = {
    '1': '0',
    '0': '1'
}


def insert(root, bin_string):
    cur = root
    for char in bin_string:
        index = int(char)
        if cur.children[index] is None:
            cur.children[index] = TrieNode()
        cur = cur.children[index]


class Solution:
    def findMaximumXOR(self, nums) -> int:
        root = TrieNode()

        for num in nums:
            bin_string = format(num, 'b').zfill(31)
            insert(root, bin_string)

        res = ''.zfill(31)
        for num in nums:
            cur = root
            bin_string = format(num, 'b').zfill(31)
            temp = []
            for c in bin_string:
                target = int(flip[c])
                if cur.children[target] is not None:
                    temp.append('1')
                    cur = cur.children[target]
                else:
                    temp.append('0')
                    cur = cur.children[int(c)]
            if ''.join(temp) > res:
                res = ''.join(temp)

        return int(res, 2)
