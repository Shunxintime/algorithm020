class Solution:
    def combine(self, n: int, k: int) -> list:
        def backtrace(tmp, index):
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(index, n + 1):
                backtrace(tmp + [i], i + 1)

        res = []
        for i in range(1, n + 2 - k):
            backtrace([i], i + 1)
        return res