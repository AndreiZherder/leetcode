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
//word and prefix consist only of lowercase English next.
//At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

#include <iostream>
#include <vector>
using namespace std;

class Trie {
public:
    Trie() {
        next.assign(26, nullptr);
    }

    void insert(string word) {
        Trie* node = this;
        for (auto now : word) {
            now -= 'a';
            if (node->next[now] == nullptr) {
                node->next[now] = new Trie();
            }
            node = node->next[now];
        }
        node->isEnd = true;
    }

    bool search(string word) {
        Trie* node = this;
        for (auto now : word) {
            now -= 'a';
            if (node->next[now] == nullptr) {
                return false;
            } else {
                node = node->next[now];
            }
        }
        return node->isEnd;
    }

    bool startsWith(string prefix) {
        Trie* node = this;
        for (auto now : prefix) {
            now -= 'a';
            if (node->next[now] == nullptr) {
                return false;
            } else {
                node = node->next[now];
            }
        }
        return true;
    }
private:
    vector <Trie*> next;
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

