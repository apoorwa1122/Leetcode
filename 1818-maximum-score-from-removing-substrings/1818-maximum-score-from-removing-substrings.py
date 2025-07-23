class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pairs(s, a, b, value):
            stack = []
            score = 0
            for c in s:
                if stack and stack[-1] == a and c == b:
                    stack.pop()
                    score += value
                else:
                    stack.append(c)
            return "".join(stack), score

        total_score = 0

        # Ưu tiên xóa cặp có giá trị cao hơn trước
        if x >= y:
            s, gain1 = remove_pairs(s, 'a', 'b', x)
            _, gain2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, gain1 = remove_pairs(s, 'b', 'a', y)
            _, gain2 = remove_pairs(s, 'a', 'b', x)

        return gain1 + gain2