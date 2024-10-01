"""
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.



Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs
each with sum divisible by 10.


Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105

"""
from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter()
        for num in arr:
            counter[num % k] += 1
        if counter[0] % 2 != 0:
            return False
        del counter[0]
        if k % 2 == 0:
            if counter[k // 2] % 2 != 0:
                return False
            del counter[k // 2]
        for num in counter:
            if counter[num] != counter[k - num]:
                return False
        return True


def main():
    arr = [1, 2, 3, 4, 5, 6]
    k = 10
    print(Solution().canArrange(arr, k))


if __name__ == '__main__':
    main()
