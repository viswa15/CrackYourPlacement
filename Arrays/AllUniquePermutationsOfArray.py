class Solution:
    def uniquePerms(self, arr, n):
        # code here
        def backtrack(path, used):
            if len(path) == n:
                res.append(path[:])  # Add a copy of the current permutation
                return

            for i in range(n):
                # Skip used elements
                if used[i]:
                    continue

                # Skip duplicates: Only allow the first occurrence of duplicates
                if i > 0 and arr[i] == arr[i - 1] and not used[i - 1]:
                    continue

                # Choose the element
                used[i] = True
                path.append(arr[i])

                # Recurse
                backtrack(path, used)

                # Backtrack: Unchoose the element
                path.pop()
                used[i] = False

        arr.sort()
        res = []
        backtrack([], [False] * n)  # Initial call
        return res