class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_remainder = sum(nums) % p
        if total_remainder == 0:
            return 0
        last_seen_index = {0: -1}
        current_prefix_sum = 0
        min_length = len(nums)
        for index, num in enumerate(nums):
            current_prefix_sum = (current_prefix_sum + num) % p
            target_prefix_sum = (current_prefix_sum - total_remainder + p) % p
            if target_prefix_sum in last_seen_index:
                subarray_length = index - last_seen_index[target_prefix_sum]
                min_length = min(min_length, subarray_length)
            last_seen_index[current_prefix_sum] = index
        return -1 if min_length == len(nums) else min_length