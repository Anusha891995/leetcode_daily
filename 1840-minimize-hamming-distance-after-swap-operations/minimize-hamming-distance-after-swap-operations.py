class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        parent = list(range(len(source)))

        # Find with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Step 1: Build components
        for a, b in allowedSwaps:
            union(a, b)

        # Step 2: Group indices by root
        from collections import defaultdict, Counter
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)

        # Step 3: Compute minimum Hamming distance
        hamming_distance = 0

        for indices in groups.values():
            count = Counter()
            
            # Count elements in source
            for i in indices:
                count[source[i]] += 1
            
            # Match with target
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    hamming_distance += 1

        return hamming_distance
        