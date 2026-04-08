class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''n=len(nums)
        new_sorted = sorted(nums)
        def reverse_array(temp,start,end):
            while start < end:
                temp[start],temp[end]=temp[end],temp[start]
                start+=1
                end-=1
        for i in range(n):
            temp = nums[:]
            reverse_array(temp,0,i-1)
            reverse_array(temp,i,n-1)
            reverse_array(temp,0,n-1)
            if temp == new_sorted :
                return True
        
        return False'''

        n=len(nums)
        count=0

        for i in range(n):
            if nums[i] > nums[(i+1)%n] :
                count+=1
        
        return count <= 1


        

        