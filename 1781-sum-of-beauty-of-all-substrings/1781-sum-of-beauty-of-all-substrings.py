class Solution(object):
    def beautySum(self, s):
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0] * 26   # frequency array

            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1

                # compute beauty
                maxf = 0
                minf = float('inf')

                for f in freq:
                    if f > 0:
                        maxf = max(maxf, f)
                        minf = min(minf, f)

                total += (maxf - minf)

        return total