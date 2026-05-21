class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pse1 = self.findpse1(nums,n)
        nse1 = self.findnse1(nums,n)
        pse2 = self.findpse2(nums,n)
        nse2 = self.findnse2(nums,n)
        total_min = 0
        total_max = 0
        for i in range(n):
            left_min = i - pse1[i]
            right_min = nse1[i] - i
            left_max = i - pse2[i]
            right_max = nse2[i] - i

            total_min += (left_min * right_min * nums[i])
            total_max += left_max * right_max *nums[i]
        return total_max - total_min
    def findpse1(self,nums,n):
        stack =[]
        pse1 = [-1]*n
        for i in range(n):
            while len(stack)!=0 and nums[stack[-1]] > nums[i]:
                stack.pop()
            if len(stack) == 0:
                pse1[i] = -1
            else:
                pse1[i] = stack[-1]
            stack.append(i)
        return pse1

    def findnse1(self,nums,n):
        stack = []
        nse1 = [-1]*n

        for i in range(n-1,-1,-1):
            while len(stack)!=0 and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if len(stack) == 0:
                nse1[i] = n
            else:
                nse1[i] = stack[-1]
            stack.append(i)
        return nse1  
    
    def findpse2(self,nums,n):
        stack = []
        pse2 =[-1]*n
        for i in range(n):
            while len(stack)!=0 and nums[stack[-1]] < nums[i]:
                stack.pop()
            if len(stack)==0:
                pse2[i] = -1
            else:
                pse2[i] = stack[-1]
            stack.append(i)
        return pse2
    def findnse2(self,nums,n):
        stack = []
        nse2 =[-1]*n
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if len(stack)==0:
                nse2[i] = n
            else:
                nse2[i] = stack[-1]
            stack.append(i)
        return nse2