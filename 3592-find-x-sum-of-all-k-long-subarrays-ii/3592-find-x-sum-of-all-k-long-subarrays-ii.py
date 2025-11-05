import collections
from sortedcontainers import SortedList
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        
        freq_map = collections.Counter(nums[:k])
        window_sum = sum(nums[:k])
        
        all_items = SortedList()
        for val, count in freq_map.items():
            if count > 0:
                all_items.add((count, val))

        u = len(all_items)
        target_top_size = min(x, u)
        
        sl_top = SortedList(all_items[u - target_top_size:])
        sl_rest = SortedList(all_items[:u - target_top_size])
        
        x_sum = sum(c * v for c, v in sl_top)
        
        if x >= u:
            ans.append(window_sum)
        else:
            ans.append(x_sum)

        for i in range(n - k):
            left_val = nums[i]
            right_val = nums[i + k]
            
            window_sum = window_sum - left_val + right_val
            
            old_count_left = freq_map[left_val]
            pair_left = (old_count_left, left_val)
            
            if pair_left in sl_top:
                sl_top.remove(pair_left)
                x_sum -= old_count_left * left_val
            else:
                sl_rest.remove(pair_left)
            
            freq_map[left_val] -= 1
            new_count_left = freq_map[left_val]
            
            if new_count_left > 0:
                sl_rest.add((new_count_left, left_val))

            old_count_right = freq_map[right_val]
            
            if old_count_right > 0:
                pair_right = (old_count_right, right_val)
                if pair_right in sl_top:
                    sl_top.remove(pair_right)
                    x_sum -= old_count_right * right_val
                else:
                    sl_rest.remove(pair_right)

            freq_map[right_val] += 1
            new_count_right = freq_map[right_val]
            
            sl_rest.add((new_count_right, right_val))

            u = len(sl_top) + len(sl_rest)
            target_top_size = min(x, u)
            
            while len(sl_top) > target_top_size:
                c, v = sl_top.pop(0)
                x_sum -= c * v
                sl_rest.add((c, v))
                
            while len(sl_top) < target_top_size and len(sl_rest) > 0:
                c, v = sl_rest.pop(-1)
                x_sum += c * v
                sl_top.add((c, v))

            while sl_top and sl_rest and sl_top[0] < sl_rest[-1]:
                c_top, v_top = sl_top.pop(0)
                c_rest, v_rest = sl_rest.pop(-1)
                
                sl_top.add((c_rest, v_rest))
                sl_rest.add((c_top, v_top))
                
                x_sum = x_sum - (c_top * v_top) + (c_rest * v_rest)

            if x >= u:
                ans.append(window_sum)
            else:
                ans.append(x_sum)

        return ans