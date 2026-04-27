class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        # Directions: up, down, left, right
        dirs = {
            1: [(0, -1), (0, 1)],   # left, right
            2: [(-1, 0), (1, 0)],   # up, down
            3: [(0, -1), (1, 0)],   # left, down
            4: [(0, 1), (1, 0)],    # right, down
            5: [(0, -1), (-1, 0)],  # left, up
            6: [(0, 1), (-1, 0)]    # right, up
        }

        # Check if two cells are properly connected
        def is_connected(x, y, nx, ny):
            dx, dy = nx - x, ny - y
            if (dx, dy) not in dirs[grid[x][y]]:
                return False
            if (-dx, -dy) not in dirs[grid[nx][ny]]:
                return False
            return True

        visited = set()
        stack = [(0, 0)]
        visited.add((0, 0))

        while stack:
            x, y = stack.pop()

            if x == m - 1 and y == n - 1:
                return True

            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if is_connected(x, y, nx, ny):
                        visited.add((nx, ny))
                        stack.append((nx, ny))

        return False