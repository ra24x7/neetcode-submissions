class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warm = [0] * len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                a = stack.pop()
                warm[a] = i - a
            stack.append(i)
        return warm

        