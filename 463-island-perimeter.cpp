/*
 * Given two strings text1 and text2, return the length of their longest common subsequence.
 * If there is no common subsequence, return 0.
 * A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
 * For example, "ace" is a subsequence of "abcde".
 * A common subsequence of two strings is a subsequence that is common to both strings.
 *
 * Example 1:
 * Input: text1 = "abcde", text2 = "ace"
 * Output: 3
 * Explanation: The longest common subsequence is "ace" and its length is 3.
 * Example 2:
 * Input: text1 = "abc", text2 = "abc"
 * Output: 3
 * Explanation: The longest common subsequence is "abc" and its length is 3.
 * Example 3:
 * Input: text1 = "abc", text2 = "def"
 * Output: 0
 * Explanation: There is no such common subsequence, so the result is 0.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        for (int i = 0; i < n; i++) {
            grid[i].insert(grid[i].begin(), 0);
            grid[i].push_back(0);
        }
        grid.insert(grid.begin(), vector<int> (m + 2, 0));
        grid.emplace_back(m + 2, 0);
        n = n + 2;
        m = m + 2;
        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0 ; j < m - 1; j++) {
                ans = ans + (grid[i][j] ^ grid[i][j + 1]) + (grid[i][j] ^ grid[i + 1][j]);
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    //vector<vector<int>> grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    //vector<vector<int>> grid = {{1}};
    vector<vector<int>> grid = {{1,0,0}};
    cout << solution.islandPerimeter(grid);
}

