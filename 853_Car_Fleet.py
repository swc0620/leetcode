class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for idx in range(len(position)):
            pairs.append((position[idx], (target - position[idx]) / speed[idx]))
        pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
        for pair in pairs:
            if not stack:
                stack.append(pair)
            if pair[1] > stack[-1][1]:
                stack.append(pair)
        return len(stack)
