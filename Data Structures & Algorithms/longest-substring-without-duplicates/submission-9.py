class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(str)
        count, maxim, cut, iteration = 0,0,0,1
        for char in s:
            if char in seen:
                if seen[char] > cut:
                    count -= seen[char] - cut 
                    cut = seen[char]
                seen[char] = iteration
            else:
                seen[char] = iteration
            iteration += 1
            count += 1
            maxim = max(count, maxim)
        return max(maxim,count)