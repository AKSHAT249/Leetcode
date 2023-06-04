class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                index_1 = i
            if nums[i]==len(nums):
                index_4 = i
                
        print(index_1, index_4)
                
        if index_1==0 and index_4==len(nums)-1:
            return 0
        if index_1<index_4:
            return index_1 + len(nums)-1-index_4
        if index_1>index_4:
            return index_1+len(nums)-index_4-2
        
