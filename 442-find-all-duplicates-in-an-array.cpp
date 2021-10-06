/*
 * Given an integer array nums of length n where all the integers of nums are in the range [1, n]
 * and each integer appears once or twice, return an array of all the integers that appears twice.
 * You must write an algorithm that runs in O(n) time and uses only constant extra space.
 * Example 1:
 * Input: nums = [4,3,2,7,8,2,3,1]
 * Output: [2,3]
 * Example 2:
 * Input: nums = [1,1,2]
 * Output: [1]
 * Example 3:
 * Input: nums = [1]
 * Output: []
 */
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_set<int> s;
        vector<int> ans;
        for (auto now : nums) {
            if (!s.insert(now).second) {
                ans.push_back(now);
            }
        }
        return ans;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {4,3,2,7,8,2,3,1};
    vector<int> ans = solution.findDuplicates(nums);
    for (auto now : ans) {
        cout << now << " ";
    }

}

