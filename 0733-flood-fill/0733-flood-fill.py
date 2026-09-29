class Solution:          
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        r = len(image)
        c = len(image[0])
        initial_col = image[sr][sc]
        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = color
        while len(queue) != 0:
            i,j = queue.popleft()
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                new_i = i + x
                new_j = j + y
                if new_i < 0 or new_i >= r or new_j < 0 or new_j >= c:
                    continue
                if image[new_i][new_j] != initial_col:
                    continue
                image[new_i][new_j] = color    
                queue.append((new_i,new_j))    
        return image
        