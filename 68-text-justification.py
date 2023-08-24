"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly
maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.",
"Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def append_line(last: bool = False):
            if last:
                if len(cur) == 1:
                    ans.append(cur[0] + ' ' * (maxWidth - l))
                else:
                    line = []
                    size = 0
                    for w in cur:
                        if maxWidth - size == len(w):
                            line.append(w)
                        else:
                            line.append(w + ' ')
                        size += len(w) + 1
                    line.append(' ' * (maxWidth - size))
                    ans.append(''.join(line))
                return
            if len(cur) == 1:
                ans.append(cur[0] + ' ' * (maxWidth - l))
            else:
                x = (maxWidth - l) // (len(cur) - 1)
                y = (maxWidth - l) % (len(cur) - 1)
                line = []
                for w in cur[:len(cur) - 1]:
                    if y:
                        line.append(w + ' ' * (x + 1))
                        y -= 1
                    else:
                        line.append(w + ' ' * x)
                line.append(cur[len(cur) - 1])
                ans.append(''.join(line))

        ans = []
        cur = []
        l = 0
        free = 0
        for word in words:
            if free >= len(word) + 1:
                free -= len(word) + 1
                cur.append(word)
                l += len(word)
            else:
                if cur:
                    append_line()
                free = maxWidth - len(word)
                cur = [word]
                l = len(word)
        append_line(last=True)
        return ans


def main():
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth))


if __name__ == '__main__':
    main()
