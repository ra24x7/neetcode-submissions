class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warm = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                a = stack.pop()
                warm[a] = i - a
            stack.append(i)
        return warm

        