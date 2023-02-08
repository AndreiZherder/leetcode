"""
You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload"
to a server. You need to implement a data structure that calculates the length
of the longest uploaded prefix at various points in the upload process.

We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server.
The longest uploaded prefix is the maximum value of i that satisfies this definition.

Implement the LUPrefix class:

LUPrefix(int n) Initializes the object for a stream of n videos.
void upload(int video) Uploads video to the server.
int longest() Returns the length of the longest uploaded prefix defined above.


Example 1:

Input
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
Output
[null, null, 0, null, 1, null, 3]

Explanation
LUPrefix server = new LUPrefix(4);   // Initialize a stream of 4 videos.
server.upload(3);                    // Upload video 3.
server.longest();                    // Since video 1 has not been uploaded yet, there is no prefix.
                                     // So, we return 0.
server.upload(1);                    // Upload video 1.
server.longest();                    // The prefix [1] is the longest uploaded prefix, so we return 1.
server.upload(2);                    // Upload video 2.
server.longest();                    // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.


Constraints:

1 <= n <= 10^5
1 <= video <= n
All values of video are distinct.
At most 2 * 105 calls in total will be made to upload and longest.
At least one call will be made to longest.
"""


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.right = list(range(n))

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
            self.right[id1] = max(self.right[id1], self.right[id2])
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1
            self.right[id2] = max(self.right[id1], self.right[id2])



class LUPrefix:

    def __init__(self, n: int):
        self.dsu = DSU(n + 1)

    def upload(self, video: int) -> None:
        self.dsu.union(video, video - 1)

    def longest(self) -> int:
        return self.dsu.right[self.dsu.find(0)]


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()


def main():
    server = LUPrefix(4)
    print(server.upload(3))
    print(server.longest())
    print(server.upload(1))
    print(server.upload(2))
    print(server.longest())


if __name__ == '__main__':
    main()
