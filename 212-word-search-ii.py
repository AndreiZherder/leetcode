"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.



Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i: int, j: int, path: List[str], node: dict, parent: dict) -> List[str]:
            def inside(i: int, j: int) -> bool:
                return 0 <= i < n and 0 <= j < m
            steps = ((1, 0), (0, 1), (-1, 0), (0, -1))
            ans = []
            length = len(node)
            if '#' in node:
                ans.append(''.join(path + [board[i][j]]))
                length -= 1
            if length > 0:
                for di, dj in steps:
                    ni = i + di
                    nj = j + dj
                    if inside(ni, nj):
                        if board[ni][nj]:
                            if board[ni][nj] in node:
                                saved = board[i][j]
                                board[i][j] = ''
                                ans.extend(dfs(ni, nj, path + [saved], node[board[ni][nj]], node))
                                board[i][j] = saved
            else:
                del parent[board[i][j]]
            return ans


        root = dict()
        for word in words:
            node = root
            for c in word:
                if c in node:
                    node = node[c]
                else:
                    node[c] = dict()
                    node = node[c]
            node['#'] = dict()

        n = len(board)
        m = len(board[0])
        ans = []
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    ans.extend(dfs(i, j, [], root[board[i][j]], root))
        return list(set(ans))


def main():
    # board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    # words = ["oath", "pea", "eat", "rain", "pen", "pena"]
    board = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
     ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
    words = ["lllllll", "fffffff", "ssss", "s", "rr", "xxxx", "ttt", "eee", "ppppppp", "iiiiiiiii", "xxxxxxxxxx", "pppppp",
     "xxxxxx", "yy", "jj", "ccc", "zzz", "ffffffff", "r", "mmmmmmmmm", "tttttttt", "mm", "ttttt", "qqqqqqqqqq", "z",
     "aaaaaaaa", "nnnnnnnnn", "v", "g", "ddddddd", "eeeeeeeee", "aaaaaaa", "ee", "n", "kkkkkkkkk", "ff", "qq", "vvvvv",
     "kkkk", "e", "nnn", "ooo", "kkkkk", "o", "ooooooo", "jjj", "lll", "ssssssss", "mmmm", "qqqqq", "gggggg",
     "rrrrrrrrrr", "iiii", "bbbbbbbbb", "aaaaaa", "hhhh", "qqq", "zzzzzzzzz", "xxxxxxxxx", "ww", "iiiiiii", "pp",
     "vvvvvvvvvv", "eeeee", "nnnnnnn", "nnnnnn", "nn", "nnnnnnnn", "wwwwwwww", "vvvvvvvv", "fffffffff", "aaa", "p",
     "ddd", "ppppppppp", "fffff", "aaaaaaaaa", "oooooooo", "jjjj", "xxx", "zz", "hhhhh", "uuuuu", "f", "ddddddddd",
     "zzzzzz", "cccccc", "kkkkkk", "bbbbbbbb", "hhhhhhhhhh", "uuuuuuu", "cccccccccc", "jjjjj", "gg", "ppp", "ccccccccc",
     "rrrrrr", "c", "cccccccc", "yyyyy", "uuuu", "jjjjjjjj", "bb", "hhh", "l", "u", "yyyyyy", "vvv", "mmm", "ffffff",
     "eeeeeee", "qqqqqqq", "zzzzzzzzzz", "ggg", "zzzzzzz", "dddddddddd", "jjjjjjj", "bbbbb", "ttttttt", "dddddddd",
     "wwwwwww", "vvvvvv", "iii", "ttttttttt", "ggggggg", "xx", "oooooo", "cc", "rrrr", "qqqq", "sssssss", "oooo",
     "lllllllll", "ii", "tttttttttt", "uuuuuu", "kkkkkkkk", "wwwwwwwwww", "pppppppppp", "uuuuuuuu", "yyyyyyy", "cccc",
     "ggggg", "ddddd", "llllllllll", "tttt", "pppppppp", "rrrrrrr", "nnnn", "x", "yyy", "iiiiiiiiii", "iiiiii", "llll",
     "nnnnnnnnnn", "aaaaaaaaaa", "eeeeeeeeee", "m", "uuu", "rrrrrrrr", "h", "b", "vvvvvvv", "ll", "vv", "mmmmmmm",
     "zzzzz", "uu", "ccccccc", "xxxxxxx", "ss", "eeeeeeee", "llllllll", "eeee", "y", "ppppp", "qqqqqq", "mmmmmm",
     "gggg", "yyyyyyyyy", "jjjjjj", "rrrrr", "a", "bbbb", "ssssss", "sss", "ooooo", "ffffffffff", "kkk", "xxxxxxxx",
     "wwwwwwwww", "w", "iiiiiiii", "ffff", "dddddd", "bbbbbb", "uuuuuuuuu", "kkkkkkk", "gggggggggg", "qqqqqqqq",
     "vvvvvvvvv", "bbbbbbbbbb", "nnnnn", "tt", "wwww", "iiiii", "hhhhhhh", "zzzzzzzz", "ssssssssss", "j", "fff",
     "bbbbbbb", "aaaa", "mmmmmmmmmm", "jjjjjjjjjj", "sssss", "yyyyyyyy", "hh", "q", "rrrrrrrrr", "mmmmmmmm", "wwwww",
     "www", "rrr", "lllll", "uuuuuuuuuu", "oo", "jjjjjjjjj", "dddd", "pppp", "hhhhhhhhh", "kk", "gggggggg", "xxxxx",
     "vvvv", "d", "qqqqqqqqq", "dd", "ggggggggg", "t", "yyyy", "bbb", "yyyyyyyyyy", "tttttt", "ccccc", "aa", "eeeeee",
     "llllll", "kkkkkkkkkk", "sssssssss", "i", "hhhhhh", "oooooooooo", "wwwwww", "ooooooooo", "zzzz", "k", "hhhhhhhh",
     "aaaaa", "mmmmm"]
    print(Solution().findWords(board, words))


if __name__ == '__main__':
    main()
