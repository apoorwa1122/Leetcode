
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i] can be written as nums[i] - i != nums[j] - j
        # bad pairs are two indices with different difs

        total_pairs = comb(len(nums), 2) # total combinations of two indices (pairs)

        dif_counter = Counter([n - i for i, n in enumerate(nums)]) # frequency of each dif
        good_pairs = sum(comb(count, 2) for count in dif_counter.values()) # total pairs with same dif
        
        return total_pairs - good_pairs # bad pairs = total pairs - good pairs