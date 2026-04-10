class Solution(object):
    def generate(self, numRows):
        if numRows==0:
            return []
        
        triangle =[[1]]

        for i in range (1,numRows):
            prev_row=triangle[-1]
            current_row=[1]

            for j in range(len(prev_row)-1):
                sum_val=prev_row[j]+prev_row[j+1]
                current_row.append(sum_val)
            current_row.append(1)
            triangle.append(current_row)
        return triangle
        