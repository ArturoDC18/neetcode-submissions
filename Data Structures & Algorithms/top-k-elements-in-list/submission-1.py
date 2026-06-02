class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        recollecter = {}
        for num in nums:
            if num in recollecter:
                recollecter[num][1] += 1
            else:
                recollecter[num] = [num, 1]
        to_return = list(recollecter.values())
        new_list = sorted(to_return, key=lambda sublist: sublist[1])
        lista= []
        tracker = len(to_return)
        for _ in range(0,k):
            lista.append(new_list[tracker-1][0])
            tracker -= 1
        return lista