class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for char in s1:
            freq1[char] += 1
        l = 0
        for r in range(len(s2)):
            freq2[s2[r]] += 1
            while (r-l +1) > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
            if freq2 == freq1:
                return True
        return False