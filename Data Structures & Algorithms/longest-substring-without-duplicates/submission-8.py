class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(str)
        count, maxim, cut, iteration = 0,0,0,1
        if len(s) == 1:
            return 1
        for char in s:
            print(f"processing {char}, pos = {iteration}")
            if char in seen:
                if seen[char] > cut:
                    count -= seen[char] - cut 
                    print(f"applied cut as {seen[char]} > {cut}, now cut = {iteration} and count = {count}")
                    cut = seen[char]
                seen[char] = iteration
                print(f"new max {maxim}")
            else:
                print("adding to dic")
                seen[char] = iteration
            print(f"counter {count}")
            iteration += 1
            count += 1
            maxim = max(count, maxim)
        return max(maxim,count)