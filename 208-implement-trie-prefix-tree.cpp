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
        Trie* node = this;
        for (auto now : word) {
            if (node->letters.find(now) == node->letters.end()) {
                node->letters[now] = new Trie();
            }
            node = node->letters[now];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie* node = this;
        for (auto now : word) {
            auto it = node->letters.find(now);
            if (it == node->letters.end()) {
                return false;
            } else {
                node = it->second;
            }
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        Trie* node = this;
        for (auto now : prefix) {
            auto it = node->letters.find(now);
            if (it == node->letters.end()) {
                return false;
            } else {
                node = it->second;
            }
        }
        return true;
    }
private:
    unordered_map <char,Trie*> letters = {};
    bool isEnd = false;
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

