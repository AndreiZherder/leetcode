"""
There are n dominoes in a line, and we place each domino vertically upright.
In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left.
Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question,
we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = ['.' for i in range(len(dominoes))]
        last_left = 0
        i = 0
        while i < len(dominoes):
            while i < len(dominoes) and dominoes[i] != 'R':
                if dominoes[i] == 'L':
                    for j in range(last_left, i + 1):
                        ans[j] = 'L'
                    last_left = i
                i += 1
            if i == len(dominoes):
                return ''.join(ans)
            last_right = i
            while i < len(dominoes) and dominoes[i] != 'L':
                if dominoes[i] == 'R':
                    for j in range(last_right, i + 1):
                        ans[j] = 'R'
                    last_right = i
                i += 1
            if i == len(dominoes):
                for j in range(last_right, len(dominoes)):
                    ans[j] = 'R'
                return ''.join(ans)
            else:
                last_left = i
                if (i - last_right) % 2 == 0:
                    for j in range(last_right, last_right + (i - last_right) // 2):
                        ans[j] = 'R'
                    for j in range(last_right + (i - last_right) // 2 + 1, i + 1):
                        ans[j] = 'L'
                else:
                    for j in range(last_right, last_right + (i - last_right) // 2 + 1):
                        ans[j] = 'R'
                    for j in range(last_right + (i - last_right) // 2 + 1, i + 1):
                        ans[j] = 'L'
            i += 1
        return ''.join(ans)


def main():
    dominoes = ".L.R...LR..L.."
    print(Solution().pushDominoes(dominoes))


if __name__ == '__main__':
    main()
