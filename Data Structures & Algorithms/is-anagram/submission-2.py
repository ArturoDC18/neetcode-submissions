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
        if str2 != str1:
            return False
        else:
            return True
        