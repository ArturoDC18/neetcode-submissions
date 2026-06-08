class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) # let n be the size of array
        answ = [1] * n # initialize n size array with 1s

        for i in range(1,n): #loop skipping the first value
            answ[i] = answ[i-1] * nums[i-1] # compute prefix prod
        
        suffix = 1 #initialize suffix prod
        for i in range(n-1, -1, -1): #start 1 before the end, stop at 0, decrease step by 1
            answ[i] *= suffix # multiply pre by post
            suffix *= nums[i] # compute post on the fly

        return answ