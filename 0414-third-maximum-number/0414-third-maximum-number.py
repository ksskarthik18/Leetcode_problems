class Solution(object):
    def thirdMax(self, nums):
        dist_nums=set(nums)

        if len(dist_nums)<3:
            return max(dist_nums)
        sorted_nums=sorted(list(dist_nums))

        return sorted_nums[-3]       