class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        res = []
        for i,num_1rst in enumerate(nums_sorted):
            # if num_1rst > target:
            #    # break since target can't be on the right
            #    break
            rest_nums = nums_sorted.copy()
            rest_nums.remove(num_1rst)
            for j, num_2nd in enumerate(rest_nums):
                #if num_2nd > target:
                #    break
                if num_1rst+num_2nd == target :
                    res = [nums.index(num_1rst),nums.index(num_2nd)]
                    break
                # else:
                #    rest_nums = rest_nums.remove(num_2nd)
        if res[0]==res[1]:
            duplicate = nums[res[0]]
            nums.remove(nums[res[0]])
            res[1] = nums.index(duplicate)  + 1
        return res
    
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        to_search = dict()
        res = []
        for i,num in enumerate(nums):
            to_search = dict()
            to_search[num] = nums.copy()
            to_search[num].remove(num)
            value = target - num
            if value in to_search[num]:
                res = [i,nums.index(value)]
        if res[0]==res[1]:
            duplicate = nums[res[0]]
            nums.remove(nums[res[0]])
            res[1] = nums.index(duplicate)  + 1
        return res
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            value = target - num
            if value in d:
                return [i,d[value]]
            else:
                d[num] = i
                
                