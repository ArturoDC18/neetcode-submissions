class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}

        for char in s:
            if char in str1:
                str1[char] = str1[char] + 1
            else:
                str1[char] = 1
        for char in t:
            if char in str2:
                str2[char] = str2[char] + 1
            else:
                str2[char] = 1
        if len(str1) == len(str2):
            for char in str1:
                if char not in str2:
                    return False
                if str1[char] != str2[char]:
                    return False
                else:
                    continue
            return True
        else:
            return False
        