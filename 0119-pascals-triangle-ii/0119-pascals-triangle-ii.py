class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            curr_row=[1]
        curr_row=[1]
        for _ in range(rowIndex):
            next_row=[1]
            for j in range(len(curr_row)-1):
                sum_val=curr_row[j]+curr_row[j+1]
                next_row.append(sum_val)
            next_row.append(1)
            curr_row=next_row
        return curr_row
            

            