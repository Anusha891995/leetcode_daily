class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        
        # Step 1: Update heights row by row
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
            
            # Step 2: Create a copy of the current row and sort it
            # Sorting descending helps us find the max area at this row
            curr_row = sorted(matrix[i], reverse=True)
            
            # Step 3: Calculate max area for this row
            for k in range(n):
                height = curr_row[k]
                width = k + 1
                ans = max(ans, height * width)
                
        return ans