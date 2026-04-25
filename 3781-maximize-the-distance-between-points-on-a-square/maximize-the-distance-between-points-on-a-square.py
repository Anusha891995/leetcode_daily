class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        def pos(x, y):
            if y == 0:
                return x
            if x == side:
                return side + y
            if y == side:
                return 3 * side - x
            return 4 * side - y

        arr = sorted(pos(x, y) for x, y in points)
        n = len(arr)
        L = 4 * side
        ext = arr + [x + L for x in arr]

        def can(d):
            # next[i] = first index j > i such that ext[j] - ext[i] >= d
            nxt = [0] * (2 * n)
            j = 0
            for i in range(2 * n):
                if j < i + 1:
                    j = i + 1
                while j < 2 * n and ext[j] - ext[i] < d:
                    j += 1
                nxt[i] = j

            # try every start
            for start in range(n):
                cur = start
                ok = True

                # greedily jump k-1 times
                for _ in range(k - 1):
                    cur = nxt[cur]
                    if cur >= start + n:
                        ok = False
                        break

                # also need wrap-around distance valid
                if ok and ext[start] + L - ext[cur] >= d:
                    return True

            return False

        lo, hi = 0, 2 * side
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
        