// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
// The same letter cell may not be used more than once.
// Example 1:
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
// Output: true
// Example 2:
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
// Output: true
// Example 3:
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
// Output: false
// Constraints:
// m == board.length
// n = board[i].length
// 1 <= m, n <= 6
// 1 <= word.length <= 15
// board and word consists of only lowercase and uppercase English letters.
// Follow up: Could you use search pruning to make your solution faster with a larger board?

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size();
        int m = board[0].size();

        board.emplace(board.begin(), vector<char>(m, '-'));
        board.emplace(board.end(), vector<char>(m, '-'));
        for (int i = 0; i < n + 2; i++) {
            board[i].emplace(board[i].begin(), '-');
            board[i].emplace(board[i].end(), '-');
        }
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= m; j++) {
                if (word[0] == board[i][j]) {
                    board[i][j] = '*';
                    if (word.size() == 1) {
                        return true;
                    } else if (solve(board, i, j, word, 1)) {
                        return true;
                    } else {
                        board[i][j] = word[0];
                    }
                }
            }
        }
        return false;
    }
private:
    vector<pair<int, int>> step = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    bool solve(vector<vector<char>>& board, int x, int y, string word, int letterNo) {
        for (auto& i : step) {
            if (word[letterNo] == board[x + i.first][y + i.second]) {
                board[x + i.first][y + i.second] = '*';
                if (letterNo == word.size() - 1) {
                    return true;
                } else if (solve(board, x + i.first, y + i.second, word, letterNo + 1)) {
                    return true;
                } else {
                    board[x + i.first][y + i.second] = word[letterNo];
                }
            }
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<vector<char>> board = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    //vector<vector<char>> board = {{'A','B'},{'C','D'}};
    string word = "ABCCED";
    //string word = "SEE";
    //string word = "ABCB";
    //string word = "ABCD";
    bool ans = solution.exist(board, word);
    if (ans) {
        cout << "true";
    } else {
        cout << "false";
    }
    return 0;
}

