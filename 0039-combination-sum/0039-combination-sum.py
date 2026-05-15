#Time complexity : 2**t x k
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def backTrack(i,target,ds):
            if i == len(candidates):
                return
            if target == 0:
                result.append(ds[:])
                return
            
            if candidates[i]<=target:
                ds.append(candidates[i])
                backTrack(i,target-candidates[i],ds)
                ds.pop()
            backTrack(i+1,target,ds)

        backTrack(0,target,[])
        return result


        