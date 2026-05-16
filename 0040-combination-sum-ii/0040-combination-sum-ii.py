class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def backTrack(index,target,ds):
            if target == 0:
                result.append(ds[:])
                return

            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                backTrack(i+1,target-candidates[i],ds)
                ds.pop()
        backTrack(0,target,[])

        return result

        