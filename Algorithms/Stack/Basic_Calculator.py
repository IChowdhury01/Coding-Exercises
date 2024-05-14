class Solution:
    def calculate(self, s: str) -> int:
        cur, res = 0, 0
        sign = 1    # +
        stack = []  # (prev res, prev sign)
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c in ["+", "-"]:
                res += cur * sign
                sign = 1 if c == '+' else -1
                cur = 0
            elif c == '(':
                stack.append((res, sign))
                res, sign = 0, 1
            elif c == ')':
                prevRes, prevSign = stack.pop()
                res += cur * sign
                res = prevRes + prevSign * res
                cur = 0
        return res + cur * sign
