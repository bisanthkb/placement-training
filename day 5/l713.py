class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        r,l=0,0
        cnt,p=0,1
        while (r<len(nums)):
            p*=nums[r]
            while p>=k:
                p//=nums[l]
                l+=1
            cnt+=r-l+1
            r+=1
        return cnt