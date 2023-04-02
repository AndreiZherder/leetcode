"""
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the
number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4. 
Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.
 

Constraints:

1 <= s.length <= 50
'0' <= s[i] <= '1'
"""



class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = 0
        state = 1
        cnt0 = 0
        cnt1 = 0
        for c in s:
            if state == 1:
                if c == '1':
                    cnt1 += 1
                    best = max(best, min(cnt0, cnt1))
                else:
                    state = 0
                    cnt0 = 1
                    cnt1 = 0
            else:
                if c == '1':
                    cnt1 = 1
                    best = max(best, min(cnt0, cnt1))
                    state = 1
                else:
                    cnt0 += 1
        return best * 2


def main():
    s = "0011101000001111001111111"
    print(Solution().findTheLongestBalancedSubstring(s))


if __name__ == '__main__':
    main()
