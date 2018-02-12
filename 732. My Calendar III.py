class MyCalendarThree:
    
    def __init__(self):
        self.sts, self.ends = [], []
        self.mxv = 0
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        from bisect import bisect_left as bl, bisect_right as br, insort_left as il
        from heapq import heappop, heappush
        i, j = bl(self.ends, start), br(self.sts, end)
        il(self.sts, start, i, j)
        il(self.ends, end, i, j)
        heap = []
        for pp in range(i, j + 1):
            while heap and heap[0] <= self.sts[pp]:
                heappop(heap)
            heappush(heap, self.ends[pp])
            self.mxv = max(self.mxv, len(heap))
        return self.mxv    

    '''
    def __init__(self):
        self.start = []
        self.end = []
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        bisect.insort(self.start, start, 0, len(self.start))
        bisect.insort(self.end, end, 0, len(self.end))
        start_index = end_index = count = max_count = 0
        while start_index < len(self.start) and end_index < len(self.end):
            if self.start[start_index] < self.end[end_index]:
                start_index += 1
                count += 1
            else:
                end_index += 1
                count -= 1
            max_count = max(max_count, count)
        return max_count
    '''

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

if __name__ == "__main__":
    obj = MyCalendarThree()
    testcase = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
    for a in testcase:
        param = obj.book(a[0], a[1])
    print(obj.mxv)