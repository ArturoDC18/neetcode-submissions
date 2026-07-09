class TimeMap:

    def __init__(self):
        self.hashh = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashh:
            self.hashh[key].append((timestamp,value))
        else:
            self.hashh[key] = [(timestamp,value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashh:
            l, r = 0,len(self.hashh[key])-1
            answ = ""
            while l <= r:
                c = (l+r)//2
                if self.hashh[key][c][0] <= timestamp:
                    answ = self.hashh[key][c][1]
                    l = c +1
                else:
                    r = c - 1
            return answ
        return ""
