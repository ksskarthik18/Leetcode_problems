class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        nge = {}

        for num in nums2:

            while stack and num > stack[-1]:
                nge[stack.pop()] = num

            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            nge[stack.pop()] = -1

        result = []

        for num in nums1:
            result.append(nge[num])

        return result
        