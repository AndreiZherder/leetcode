// A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
// There are various applications of this data structure, such as autocomplete and spellchecker.
//
//Implement the Trie class:
//
//Trie() Initializes the trie object.
//void insert(String word) Inserts the string word into the trie.
//boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
//boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
//
//Example 1:
//
//Input
//["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
//[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
//Output
//[null, null, true, false, true, null, true]
//
//Explanation
//Trie trie = new Trie();
//trie.insert("apple");
//trie.search("apple");   // return True
//trie.search("app");     // return False
//trie.startsWith("app"); // return True
//trie.insert("app");
//trie.search("app");     // return True
//
//Constraints:
//
//1 <= word.length, prefix.length <= 2000
//word and prefix consist only of lowercase English letters.
//At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

#include <iostream>
#include <unordered_map>
using namespace std;

class Trie {
public:
    Trie() {

    }

    void insert(string word) {
        Trie* pTrie = this;
        word += '.';
        for (int i = 0; i < word.size(); i++) {
            auto it = pTrie->letters.find(word[i]);
            if (it == pTrie->letters.end()) {
                if (i == word.size() - 1) {
                    pTrie->letters[word[i]] = nullptr;
                } else {
                    Trie* tmp = new Trie();
                    pTrie->letters[word[i]] = tmp;
                    pTrie = tmp;
                }
            } else {
                if (it->second == nullptr) {
                    if (i < word.size() - 1) {
                        it->second = new Trie();
                        pTrie = it->second;
                    }
                } else {
                    pTrie = it->second;
                }
            }
        }
    }

    bool search(string word) {
        Trie* pTrie = this;
        for (auto now : word) {
            auto it = pTrie->letters.find(now);
            if (it == pTrie->letters.end()) {
                return false;
            } else {
                pTrie = it->second;
            }
        }
        return (pTrie->letters.find('.') != pTrie->letters.end());
    }

    bool startsWith(string prefix) {
        Trie* pTrie = this;
        for (auto now : prefix) {
            auto it = pTrie->letters.find(now);
            if (it == pTrie->letters.end()) {
                return false;
            } else {
                pTrie = it->second;
            }
        }
        return true;
    }
private:
    unordered_map <char,Trie*> letters;
};

int main() {
    Trie trie;
    trie.insert("apple");
    cout << trie.search("apple") << endl;   // return True
    cout << trie.search("app") << endl;     // return False
    cout << trie.startsWith("app") << endl; // return True
    trie.insert("app");
    cout << trie.search("app") << endl;     // return True
    return 0;
}

