class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_eat = r
        while l <= r:
            mid = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += (p + mid - 1) // mid
                if total_time > h:
                    break

            if total_time <= h:
                if mid < min_eat:
                    min_eat = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return min_eat