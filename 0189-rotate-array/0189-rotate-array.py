class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        def reverse_array(start,end):
            while start < end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        
        reverse_array(0,n-1)
        reverse_array(0,k-1)
        reverse_array(k,n-1)

        return nums
        