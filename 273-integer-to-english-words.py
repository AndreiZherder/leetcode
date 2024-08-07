"""
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


Constraints:

0 <= num <= 231 - 1

"""



class Solution:
    def numberToWords(self, num: int) -> str:
        def f(num: str) -> str:
            n = len(num)
            if int(num) == 0:
                return ''
            ans = []
            if n == 1:
                return d[num]
            elif n == 2:
                if num in d:
                    return d[num]
                else:
                    ans = ''
                    if num[-2] != '0':
                        ans = d[num[-2] + "0"]
                        if num[-1] != '0':
                            ans += ' ' + d[num[-1]]
                    else:
                        if num[-1] != '0':
                            if ans:
                                ans += ' '
                            ans += d[num[-1]]
                    return ans
            else:
                ans = ''
                if num[-3] != '0':
                    ans += d[num[-3]] + ' Hundred'
                if num[-2:] in d:
                    if ans:
                        ans += ' '
                    ans += d[num[-2:]]
                else:
                    if num[-2] != '0':
                        if ans:
                            ans += ' '
                        ans += d[num[-2] + "0"]
                        if num[-1] != '0':
                            ans += ' ' + d[num[-1]]
                    else:
                        if num[-1] != '0':
                            if ans:
                                ans += ' '
                            ans += d[num[-1]]
                return ans

        d = {
            '0': '',
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen',
            '20': 'Twenty',
            '30': 'Thirty',
            '40': 'Forty',
            '50': 'Fifty',
            '60': 'Sixty',
            '70': 'Seventy',
            '80': 'Eighty',
            '90': 'Ninety'
        }
        if num == 0:
            return 'Zero'
        num = str(num)
        n = len(num)
        ans = ''
        for i, unit in zip(range(n - 3, n - 15, -3), ['', 'Thousand', 'Million', 'Billion']):
            if i >= -2:
                cur = f(num[max(0, i):i + 3])
                if cur:
                    if ans:
                        if unit:
                            ans = cur + ' ' + unit + ' ' + ans
                        else:
                            ans = cur + ' ' + ans
                    else:
                        if unit:
                            ans = cur + ' ' + unit
                        else:
                            ans = cur
        return ans


def main():
    num = 400000003
    print(Solution().numberToWords(num))


if __name__ == '__main__':
    main()
