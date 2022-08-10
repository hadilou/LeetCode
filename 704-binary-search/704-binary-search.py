class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = right - 1
            else:
                left = left + 1
        return -1