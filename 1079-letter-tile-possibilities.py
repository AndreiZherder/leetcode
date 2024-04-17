"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1


Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.

"""
from itertools import chain, permutations


def powerset_from_permutations(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    """
    s = list(iterable)
    return chain.from_iterable(permutations(s, r) for r in range(len(s) + 1))

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(set(powerset_from_permutations(tiles))) - 1


def main():
    tiles = "AAABBC"
    print(Solution().numTilePossibilities(tiles))


if __name__ == '__main__':
    main()
