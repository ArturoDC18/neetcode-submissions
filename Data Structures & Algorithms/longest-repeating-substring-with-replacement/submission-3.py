import queue
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf, l, r, letter = 0,0,0, 'A'
        rep = defaultdict(int)
        maxfound = 0
        while r < len(s):
            rep[s[r]] += 1
            maxf = max(maxf, rep[s[r]])
            r += 1
            while (r-l) - maxf > k:
                rep[s[l]] -= 1
                maxf = max(maxf, rep[s[l]])
                l += 1
            maxfound = max(maxfound, (r-l))
        return maxfound
