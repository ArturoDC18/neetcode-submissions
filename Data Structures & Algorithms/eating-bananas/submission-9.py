class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        if len(piles) == h:
            return piles[-1]
        def canweeat(piles, h, k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours
        l, r, rate = 1, piles[-1], 0
        while l <= r:
            c = l + (r-l) // 2
            hours= canweeat(piles,h,c)
            if hours <= h:
                rate = c
                r = c - 1
            else:
                l = c +1
        return rate
                
