/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
 */

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
     vector<int> twoSum(vector<int>& nums, int target) {
         vector<int> a(2, -1);
         unordered_map<int, int> b;
         for (int i = 0; i < nums.size(); i++) {
             if (b.find(target - nums[i]) != b.end()){
                 a[0] = b[target - nums[i]];
                 a[1] = i;
                 break;
             } else {
                 b[nums[i]] = i;
             }
         }
         return a;
    }
};

int main() {
    vector<int> nums = {3, 3};
    int target = 6;
    vector<int> result;
    Solution solution;
    result = solution.twoSum(nums, target);
    for (auto x : result) {
        cout << x << " ";
    }
    return 0;
}
