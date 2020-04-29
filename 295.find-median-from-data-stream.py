#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (41.43%)
# Likes:    2146
# Dislikes: 41
# Total Accepted:    175.5K
# Total Submissions: 417.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' + '[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
#
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
#
#
#
#
# Example:
#
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
#
#
#
# Follow up:
#
#
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
#
#
#

# @lc code=start
import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = None
        self.small_heap = []
        self.large_heap = []

    def addNum(self, num: int) -> None:
        assert len(self.large_heap) - len(self.small_heap) in [0, 1]

        if len(self.large_heap) == 0:
            self.large_heap.append(num)
            return
        elif len(self.small_heap) == 0:
            if num < self.large_heap[0]:
                self.small_heap.append(-num)
            else:
                self.small_heap.append(-self.large_heap[0])
                self.large_heap[0] = num
            return

        max_small_heap = self.small_heap[0] * -1
        min_large_heap = self.large_heap[0]

        assert max_small_heap <= min_large_heap

        if len(self.large_heap) == len(self.small_heap):
            if num < max_small_heap:
                heapq.heapreplace(self.small_heap, -num)
                heapq.heappush(self.large_heap, max_small_heap)
            else:
                heapq.heappush(self.large_heap, num)
        else:
            if num <= min_large_heap:
                heapq.heappush(self.small_heap, -num)
            else:
                heapq.heapreplace(self.large_heap, num)
                heapq.heappush(self.small_heap, -min_large_heap)

        assert len(self.large_heap) - len(self.small_heap) in [0, 1]

    def findMedian(self) -> float:
        assert len(self.large_heap) - len(self.small_heap) in [0, 1]

        if len(self.small_heap) == 0:
            return self.large_heap[0]

        if len(self.large_heap) == len(self.small_heap):
            max_small_heap = self.small_heap[0] * -1
            min_large_heap = self.large_heap[0]
            return (max_small_heap + min_large_heap) / 2
        else:
            return self.large_heap[0]


# @lc code=end

# Your MedianFinder object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2
