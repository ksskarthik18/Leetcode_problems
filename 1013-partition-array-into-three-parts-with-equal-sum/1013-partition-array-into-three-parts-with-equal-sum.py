class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total_sum= sum(arr)
        if total_sum%3 != 0 :
            return False
        else:
            part_sum=total_sum//3
            curr_sum=0
            count=0
            for i in range(len(arr)):
                curr_sum+=arr[i]
                if curr_sum == part_sum :
                    curr_sum=0
                    count+=1
            return count >= 3
    



        