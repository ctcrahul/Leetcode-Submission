class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        left = sum(x < target for x in nums)  # bisect_left: the values that come before the targets
        right = sum(x <= target for x in nums)  # bisect_right: the values up to the last target
        return list(range(left, right))