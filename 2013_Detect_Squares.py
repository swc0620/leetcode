class DetectSquares:

    def __init__(self):
        self.counts = {}
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] = self.counts.get(tuple(point), 0) + 1
        self.points.append(tuple(point))

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        for x2, y2 in self.points:
            if abs(x2 - x1) != abs(y2 - y1) or x1 == x2 or y1 == y2:
                continue
            res += self.counts.get((x1, y2), 0) * self.counts.get((x2, y1), 0)
        
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)