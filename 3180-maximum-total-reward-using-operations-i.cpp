/*
You are given an integer array rewardValues of length n, representing the values of rewards.

Initially, your total reward x is 0, and all indices are unmarked. You are allowed to perform the following
operation any number of times:

Choose an unmarked index i from the range [0, n - 1].
If rewardValues[i] is greater than your current total reward x, then add rewardValues[i] to x
(i.e., x = x + rewardValues[i]), and mark the index i.
Return an integer denoting the maximum total reward you can collect by performing the operations optimally.



Example 1:

Input: rewardValues = [1,1,3,3]

Output: 4

Explanation:

During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4,
which is the maximum.

Example 2:

Input: rewardValues = [1,6,4,3,2]

Output: 11

Explanation:

Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.



Constraints:

1 <= rewardValues.length <= 2000
1 <= rewardValues[i] <= 2000
 */

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        int n = rewardValues.size();
        sort(rewardValues.begin(), rewardValues.end());
        vector<vector<int>> cache(2001, vector<int>(4001, -1));

        return dp(0, 0, rewardValues, cache);
    }

private:
    int dp(int i, int total, vector<int>& rewardValues, vector<vector<int>>& cache) {
        if (cache[i][total] != -1) {
            return cache[i][total];
        }

        if (i == rewardValues.size()) {
            return 0;
        }

        int ans = 0;
        if (rewardValues[i] > total) {
            if (total + rewardValues[i] <= 4000) {
                ans = max(ans, dp(i + 1, total + rewardValues[i], rewardValues, cache) + rewardValues[i]);
            }
        }
        ans = max(ans, dp(i + 1, total, rewardValues, cache));

        cache[i][total] = ans;
        return ans;
    }
};

int main() {
    vector<int> rewardValues = {1, 6, 4, 3, 2};
    Solution solution;
    result = solution.maxTotalReward(rewardValues);
    cout << result;
    }
    return 0;
}
