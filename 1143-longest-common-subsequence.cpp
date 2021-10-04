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
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int n = text1.size();
        int m = text2.size();
        vector <vector<int>> a(n + 1, vector<int> (m + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    a[i][j] = a[i - 1][j - 1] + 1;
                } else {
                    a[i][j] = max(a[i - 1][j], a[i][j - 1]);
                }
            }
        }
        return a[n][m];
    }

    void longestCommonSubsequence1(string text1, string text2, int& answer_len, string& answer_text) {
        int n = text1.size();
        int m = text2.size();
        vector <vector<int>> a(n + 1, vector<int> (m + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    a[i][j] = a[i - 1][j - 1] + 1;
                } else {
                    a[i][j] = max(a[i - 1][j], a[i][j - 1]);
                }
            }
        }
        answer_len =  a[n][m];

        answer_text = "";
        int i = n;
        int j = m;
        while (i >= 1 && j >= 1) {
            if (text1[i - 1] == text2[j - 1]) {
                answer_text.push_back(text1[i - 1]);
                i--;
                j--;
            } else if (a[i][j - 1] > a[i - 1][j]) {
                j--;
            } else {
                i--;
            }
        }
        reverse(answer_text.begin(), answer_text.end());
    }
};

int main() {
    Solution solution;
    string text1 = "baccbca";
    string text2 = "abcabaac";
    int answer_len;
    string answer_text;
    solution.longestCommonSubsequence1(text1, text2, answer_len, answer_text);
    cout << answer_len << " " << answer_text;
}

