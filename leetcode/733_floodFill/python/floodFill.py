class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        visited = {}
        h, w = len(image), len(image[0])
        pivot = image[sr][sc]
        
        # explores the 2D image
        def dfs(i, j):
            if i<0 or j<0 or i > (h-1) or j > (w-1) or image[i][j] != pivot:
                return
            
            if (i,j) not in visited:
                visited[(i,j)] = True
                image[i][j] = newColor
            else:
                return
                
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i+1, j)
            
        dfs(sr, sc)
        
        return image    
