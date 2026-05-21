class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left_max = self.prefix_max(height,n)
        right_max = self.suffix_max(height,n)
        total = 0
        for i in range(n):
            if left_max[i] > height[i] and right_max[i] > height[i]:
                total+= min(left_max[i],right_max[i]) - height[i]
        return total

    def prefix_max(self,height,n):
        prefix=[0]*n
        prefix[0]=height[0]
        for i in range(1,n):
            prefix[i] = max(prefix[i-1],height[i])
        return prefix

    def suffix_max(self,height,n):
        suffix = [0]*n
        suffix[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])
        return suffix        