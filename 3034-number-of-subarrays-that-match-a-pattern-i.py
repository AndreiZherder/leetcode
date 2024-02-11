"""
You are given a 0-indexed integer array nums of size n,
and a 0-indexed integer array pattern of size m consisting of integers -1, 0, and 1.

A
subarray
 nums[i..j] of size m + 1 is said to match the pattern if the following conditions hold for each element pattern[k]:

nums[i + k + 1] > nums[i + k] if pattern[k] == 1.
nums[i + k + 1] == nums[i + k] if pattern[k] == 0.
nums[i + k + 1] < nums[i + k] if pattern[k] == -1.
Return the count of subarrays in nums that match the pattern.



Example 1:

Input: nums = [1,2,3,4,5,6], pattern = [1,1]
Output: 4
Explanation: The pattern [1,1] indicates that we are looking for strictly increasing subarrays of size 3.
In the array nums, the subarrays [1,2,3], [2,3,4], [3,4,5], and [4,5,6] match this pattern.
Hence, there are 4 subarrays in nums that match the pattern.
Example 2:

Input: nums = [1,4,4,1,3,5,5,3], pattern = [1,0,-1]
Output: 2
Explanation: Here, the pattern [1,0,-1] indicates that we are looking for a sequence where the first number is smaller
than the second, the second is equal to the third, and the third is greater than the fourth. In the array nums,
the subarrays [1,4,4,1], and [3,5,5,3] match this pattern.
Hence, there are 2 subarrays in nums that match the pattern.


Constraints:

2 <= n == nums.length <= 100
1 <= nums[i] <= 109
1 <= m == pattern.length < n
-1 <= pattern[i] <= 1

"""
from typing import List

# https://github.com/TheAlgorithms/Python/blob/master/strings/rabin_karp.py

# Numbers of alphabet which we call base
alphabet_size = 256
# Modulus to hash a string
modulus = 10 ** 9 + 7


def rabin_karp(pattern: str, text: str) -> int:
    """
    The Rabin-Karp Algorithm for finding a pattern within a piece of text
    with complexity O(nm), most efficient when it is used with multiple patterns
    as it is able to check if any of a set of patterns match a section of text in o(1)
    given the precomputed hashes.
    This will be the simple version which only assumes one pattern is being searched
    for but it's not hard to modify
    1) Calculate pattern hash
    2) Step through the text one character at a time passing a window with the same
        length as the pattern
        calculating the hash of the text within the window compare it with the hash
        of the pattern. Only testing equality if the hashes match
    """
    p_len = len(pattern)
    t_len = len(text)
    if p_len > t_len:
        return -1

    p_hash = 0
    text_hash = 0
    modulus_power = 1

    # Calculating the hash of pattern and substring of text
    for i in range(p_len):
        p_hash = (ord(pattern[i]) + p_hash * alphabet_size) % modulus
        text_hash = (ord(text[i]) + text_hash * alphabet_size) % modulus
        if i == p_len - 1:
            continue
        modulus_power = (modulus_power * alphabet_size) % modulus

    ans = 0
    for i in range(0, t_len - p_len + 1):
        if text_hash == p_hash:
            ans += 1
        if i == t_len - p_len:
            continue
        # Calculate the https://en.wikipedia.org/wiki/Rolling_hash
        text_hash = ((text_hash - ord(text[i]) * modulus_power) * alphabet_size + ord(text[i + p_len])) % modulus
    return ans


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        arr = []
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                arr.append('a')
            elif nums[i] == nums[i - 1]:
                arr.append('b')
            else:
                arr.append('c')
        t = ''.join(arr)
        arr = []
        for i in range(m):
            if pattern[i] == 1:
                arr.append('a')
            elif pattern[i] == 0:
                arr.append('b')
            else:
                arr.append('c')
        p = ''.join(arr)
        return rabin_karp(p, t)


def main():
    nums = [1, 4, 4, 1, 3, 5, 5, 3]
    pattern = [1, 0, -1]
    print(Solution().countMatchingSubarrays(nums, pattern))


if __name__ == '__main__':
    main()
