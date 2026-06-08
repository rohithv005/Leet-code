class Solution:
    def twoEggDrop(self, n: int) -> int:
        moves = 0
        total = 0

        while total < n:
            moves += 1
            total += moves

        return moves