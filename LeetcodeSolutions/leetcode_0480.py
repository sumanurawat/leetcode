import heapq
from collections import defaultdict
from typing import List

class DualHeap:
    def __init__(self, k):
        # Max heap for the smaller half (invert values for max-heap in Python)
        self.small = []
        # Min heap for the larger half
        self.large = []
        # Dictionary to keep track of elements to be lazily deleted
        self.delayed = defaultdict(int)
        # Window size
        self.k = k
        # Sizes of the heaps (excluding delayed elements)
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        # Remove elements from the heap top that are marked for deletion
        while heap:
            # Get the actual value at the top (invert for max-heap)
            num = -heap[0] if heap is self.small else heap[0]
            # If this number is marked for deletion, remove it
            if self.delayed[num]:
                heapq.heappop(heap)
                self.delayed[num] -= 1
            else:
                break

    def balance(self):
        # Ensure the heaps are balanced:
        # - small can have at most one more element than large
        # - otherwise, they should be equal in size
        if self.small_size > self.large_size + 1:
            # Move the largest from small to large
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            # Move the smallest from large to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
            self.large_size -= 1
            self.small_size += 1
            self.prune(self.large)

    def insert(self, num):
        # Insert a new number into one of the heaps
        if not self.small or num <= -self.small[0]:
            # If small is empty or num is smaller than max of small, add to small
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            # Otherwise, add to large
            heapq.heappush(self.large, num)
            self.large_size += 1
        # Balance the heaps after insertion
        self.balance()

    def erase(self, num):
        # Mark a number for lazy deletion
        self.delayed[num] += 1
        # Adjust the size of the heap where the number would be
        if num <= -self.small[0]:
            self.small_size -= 1
            # If the number is at the top, prune it immediately
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)
        # Balance the heaps after deletion
        self.balance()

    def get_median(self):
        # Return the median depending on window size
        if self.k % 2 == 1:
            # Odd window size: median is top of small
            return float(-self.small[0])
        else:
            # Even window size: median is average of tops
            return (-self.small[0] + self.large[0]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Initialize the DualHeap with window size k
        dh = DualHeap(k)
        # Insert the first k elements into the heaps
        for num in nums[:k]:
            dh.insert(num)
        # Store the first median
        res = [dh.get_median()]
        # Slide the window through the rest of the array
        for i in range(k, len(nums)):
            # Insert the new element
            dh.insert(nums[i])
            # Remove the element that is sliding out of the window
            dh.erase(nums[i - k])
            # Append the current median
            res.append(dh.get_median())
        return res