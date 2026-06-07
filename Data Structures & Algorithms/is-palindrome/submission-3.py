class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = re.sub(r'[^a-zA-z0-9]','',s).lower()
        p1 = 0
        p2 = len(text) - 1

        for _ in range(len(text)-1):
            if text[p1] != text[p2]:
                return False 
            p1 += 1
            p2 -= 1

        return True