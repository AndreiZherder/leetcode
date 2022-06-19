"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]


Constraints:

1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 104
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
"""
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = dict()
        for product in products:
            node = trie
            for c in product:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node['#'] = dict()

        node = trie
        ans = []
        for i, c in enumerate(searchWord):
            if c in node:
                words = []
                self.dfs(node[c], list(searchWord[:i + 1]), words)
                ans.append(words)
                node = node[c]
            else:
                for j in range(i, len(searchWord)):
                    ans.append([])
                break
        return ans

    def dfs(self, node: dict, prefix: List[str], words: List[str]) -> bool:
        for c in sorted(node):
            if c == '#':
                words.append(''.join(prefix))
                if len(words) == 3:
                    return True
            else:
                if self.dfs(node[c], prefix + [c], words):
                    return True


def main():
    # products = ["bags", "baggage", "banner", "box", "cloths"]
    # searchWord = "bags"
    # products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    # searchWord = "mouse"
    # products = ["havana"]
    # searchWord = "havana"
    products = ["havana"]
    searchWord = "tatiana"
    print(Solution().suggestedProducts(products, searchWord))


if __name__ == '__main__':
    main()
