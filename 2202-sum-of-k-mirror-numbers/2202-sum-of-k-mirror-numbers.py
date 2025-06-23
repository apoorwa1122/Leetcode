class Solution:
    def kMirror(self, k: int, n: int) -> int:
        count = 0
        hp = []
        length = 1
        res = 0
        def is_valid(num):
            tmp = []
            remain = num
            while remain:
                tmp.append(remain % k)
                remain //= k
            return tmp == tmp[::-1]
        def add_nums(l):
            if l == 1:
                for i in range(1, 10):
                    heapq.heappush(hp, i)
                return
            if l == 2:
                for i in range(1, 10):
                    heapq.heappush(hp, i * 11)
                return
            tmp = [str(i) for i in range(1, 10)]
            for _ in range((l - 1) // 2):
                next_l = []
                for item in tmp:
                    for i in range(10):
                        next_l.append(item + str(i))
                tmp = next_l[:]
            res = []
            for item in tmp:
                if l & 1:
                    new_item = item + item[::-1][1:]
                else:
                    new_item = item + item[::-1]
                heapq.heappush(hp, int(new_item))
            return
        while True:
            if not hp:
                add_nums(length)
                length += 1
            num = heapq.heappop(hp)
            if is_valid(num):
                res += num
                count += 1
                if count == n:
                    return res
        return res