from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits, startPos, k):
        pos = [p for p, _ in fruits]
        prefix = [0]

        for _, amount in fruits:
            prefix.append(prefix[-1] + amount)

        def get_sum(left, right):
            l = bisect_left(pos, left)
            r = bisect_right(pos, right)
            return prefix[r] - prefix[l]

        ans = 0

        # Go left first, then right
        for x in range(k + 1):
            left = startPos - x
            right = startPos + max(0, k - 2 * x)
            ans = max(ans, get_sum(left, right))

        # Go right first, then left
        for x in range(k + 1):
            right = startPos + x
            left = startPos - max(0, k - 2 * x)
            ans = max(ans, get_sum(left, right))

        return ans