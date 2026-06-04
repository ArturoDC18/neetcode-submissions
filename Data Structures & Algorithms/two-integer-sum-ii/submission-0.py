class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return None
        leftP = 0
        rightP = len(numbers) - 1

        while rightP != leftP:
            add = numbers[leftP] + numbers[rightP]
            if add > target:
                rightP -= 1
            elif add < target:
                leftP += 1
            elif add == target:
                return [leftP+1, rightP+1]

        return None
