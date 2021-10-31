from typing import *

class Point:
    def __init__(self,val):
        self.val = val
        self.master = (0,0)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        first get a matrix where you can get the master of any idx and a hashmap of the masters and the size of the islands
        then go through all the zeroes and ask what the effect of each conversion to 1 would be
        return highest
        
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        """
        # map to store masters and size
        master_size = dict()
        max = 0
        # create new matrix
        augmented_matrix = [[Point(-1) for c in range(len(grid[0]))] for r in range(len(grid))]        
        
        # fill augmented matrix and master_size
        self.CountIslands(grid, augmented_matrix, master_size)
        for master in master_size:
            if master_size[master] > max:
                max = master_size[master]
        
        #go through augmented matrix and find max possible increase
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    continue

                temp_masters = set()
                # up
                if r > 0 and grid[r-1][c] == 2:
                    temp_masters.add(augmented_matrix[r-1][c].master)
                # right
                if c < len(grid[0])-1 and grid[r][c+1] == 2:
                    temp_masters.add(augmented_matrix[r][c+1].master)
                # down
                if r < len(grid)-1 and grid[r+1][c] == 2:
                    temp_masters.add(augmented_matrix[r+1][c].master)
                # left
                if c > 0 and grid[r][c-1] == 2:
                    temp_masters.add(augmented_matrix[r][c-1].master)

                possible_max = 1
                for master in temp_masters:
                    possible_max += master_size[master]
                
                if possible_max > max:
                    max = possible_max

        return max

    def CountIslands(self, grid: List[List[int]], augmented_matrix: List[List[Point]], master_size: dict):
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                """
                if seen skip (val = 2)
                if 1-> run dfs
                if 0 -> do nothing basically
                """
                if grid[r][c] == 2:
                    continue
                if grid[r][c] == 0:
                    augmented_matrix[r][c] = Point(0)
                if grid[r][c] == 1:
                    master_size[(r,c)] = 0
                    self.FindIsland(grid, augmented_matrix,master_size,r,c,(r,c))

        return

    def FindIsland(self, grid: List[List[int]], augmented_matrix: List[List[Point]], master_size: dict, r, c, master: tuple):
        grid[r][c] = 2
        master_size[master]+=1
        augmented_matrix[r][c] = Point(1)
        augmented_matrix[r][c].master = master

        # up
        if r > 0 and grid[r-1][c] == 1:
            self.FindIsland(grid, augmented_matrix,master_size,r-1,c,master)
        # right
        if c < len(grid[0])-1 and grid[r][c+1] == 1:
            self.FindIsland(grid, augmented_matrix,master_size,r,c+1,master)
        # down
        if r < len(grid)-1 and grid[r+1][c] == 1:
            self.FindIsland(grid, augmented_matrix,master_size,r+1,c,master)
        # left
        if c > 0 and grid[r][c-1] == 1:
            self.FindIsland(grid, augmented_matrix,master_size,r,c-1,master)

        return



        