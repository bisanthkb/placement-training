class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        s,e=0,(row*col)-1
        while s<=e:
            m=(s+e)//2
            i=m//col
            j=m%col
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                s=m+1
            else:
                e=m-1
        return False