class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original=image[sr][sc]
        if original==coclo:
            return image
        def fill(i,j):
            if i<0 or i>=len(image) or j<0 or j>=len(image[0])or image[i][j]!=original:
                return
            image[i][j]=color
            fill(i-1,j)
            fill(i+1,j)
            fill(i,j-1)
            fill(i,j+1)
        fill(sr,sc)
        return image