class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in buff_dict:
                return [buff_dict[target - nums[i]],i]
            else:
                buff_dict[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9
p = Solution()
m = p.twoSum(nums, target)
print(m)
