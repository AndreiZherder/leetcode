"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_end_"] = {}

    def search(self, word: str) -> bool:
        def dfs(i: int, root: dict) -> bool:
            current_dict = root
            for j in range(i, len(word)):
                if word[j] == '.':
                    ans = False
                    for d in current_dict.values():
                        ans = ans or dfs(j + 1, d)
                    return ans
                if word[j] not in current_dict:
                    return False
                current_dict = current_dict[word[j]]
            return "_end_" in current_dict

        return dfs(0, self.root)


def main():
    obj = WordDictionary()
    obj.addWord('bad')
    obj.addWord('dod')
    obj.addWord('dok')
    obj.addWord('d')
    print(obj.search('.'))


if __name__ == '__main__':
    main()
