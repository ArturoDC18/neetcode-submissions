import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        j = len(nums)-1
        pre, post = [1] * len(nums),[1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                last_pre = 1
            else:
                pre[i] = last_pre * nums[i-1]
                last_pre = pre[i]
            
            if j == len(nums)-1:
                last_post = 1
                j -= 1
            else:
                post[j] = last_post * nums[j+1]
                last_post = post[j]
                j -= 1
        return list(np.multiply(np.array(pre), np.array(post)))
            
        