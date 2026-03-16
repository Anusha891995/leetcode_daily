class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()

        for r in range(m):
            for c in range(n):
                # Radius 0 (just the cell itself)
                sums.add(grid[r][c])
                
                # Try expanding the radius q
                q = 1
                while True:
                    # Check if all four corners are within bounds
                    if r - q < 0 or r + q >= m or c - q < 0 or c + q >= n:
                        break
                    
                    curr_sum = 0
                    # Traverse the 4 edges of the rhombus
                    for i in range(q):
                        curr_sum += grid[r - q + i][c + i]   # Top to Right
                        curr_sum += grid[r + i][c + q - i]   # Right to Bottom
                        curr_sum += grid[r + q - i][c - i]   # Bottom to Left
                        curr_sum += grid[r - i][c - q + i]   # Left to Top
                    
                    sums.add(curr_sum)
                    q += 1
        
        # Return the top 3 unique sums in descending order
        return sorted(list(sums), reverse=True)[:3]