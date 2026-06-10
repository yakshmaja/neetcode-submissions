class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i  in seen:
                return True
            seen.add(i)
        return False


        """nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False"""