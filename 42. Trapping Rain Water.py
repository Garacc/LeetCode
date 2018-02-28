class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 2: return 0
        
        stack = [height[0]]
        water = 0
        for i in range(1, length):
            if max(stack) <= height[i]:
                water += max(stack) * len(stack) - sum(stack)
                stack = []
            stack.append(height[i])
        remain = list(reversed(stack))
        stack = [remain[0]]
        for i in range(1, len(remain)):
            if max(stack) <= remain[i]:
                water += max(stack) * len(stack) - sum(stack)
                stack = []
            stack.append(remain[i])
            
        return water
'''
a better solution with similar method
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum = 0
        start = 0
        end = len(height)-1
        while start < end:
            if height[start] <= height[end]:
                i = start + 1
                while i < end and height[i] <= height[start]:
                    sum += (height[start]-height[i])
                    i += 1
                start = i
            else:
                i = end -1
                while i > start and height[i] <= height[end]:
                    sum += (height[end]-height[i])
                    i -= 1
                end = i
        return sum
'''