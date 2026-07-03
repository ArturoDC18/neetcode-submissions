class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def comp(pres, dictt):
            if len(pres) != len(dictt):
                return False
            for char in pres:
                if not pres[char] >= dictt[char]:
                    return False
            return True
        dictt = defaultdict(int) #freq of t
        pres = defaultdict(int) #window freq
        ar, el = None, None
        for char in t:
            dictt[char] += 1
        l, window = -1,100000
        for r in range(len(s)):
            print(s[r])
            if s[r] in dictt:
                pres[s[r]] += 1
                print(f"l = {l}, r = {r}, window[s[r]== {pres[s[r]]}] ")
                if l == -1:
                    l = r
                while (s[l] not in dictt) or (pres[s[l]] > dictt[s[l]]):
                    print(f"Decreasing window l = {l}")
                    if s[l] in dictt:
                        pres[s[l]] -= 1
                        print(f"Decreasing {s[l]} from window, now {pres[s[l]]} ")
                        if pres[s[l]] == 0:
                            del pres[s[l]]
                    l += 1
                if comp(pres,dictt):
                    print(f"found match l = {l}, r = {r}")
                    if (r-l) < window:
                        window = (r-l)
                        ar,el = r, l
                        print(s[el:ar+1])
        if window < 100000:
            return s[el:ar+1]
        else:
            return ""

        