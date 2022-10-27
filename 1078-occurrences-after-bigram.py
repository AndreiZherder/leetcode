"""
Given two strings first and second, consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".



Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


Constraints:

1 <= text.length <= 1000
text consists of lowercase English letters and spaces.
All the words in text a separated by a single space.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""
from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        n = len(text)
        pattern = ' '.join([first, second])
        m = len(pattern)
        i = text.find(pattern)
        while i != -1:
            if i == 0 or text[i - 1] == ' ':
                beg = i + m + 1
                if beg < n:
                    end = beg
                    while end < n and text[end] != ' ':
                        end += 1
                    ans.append(text[beg:end])
                else:
                    break
            i = text.find(pattern, i + len(first) + 1)
        return ans


def main():
    text = "we will we will rock you"
    first = "we"
    second = "will"
    print(Solution().findOcurrences(text, first, second))


if __name__ == '__main__':
    main()
