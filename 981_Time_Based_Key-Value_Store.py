class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.ds:
            self.ds[key].append((value, timestamp))
        else:
            self.ds[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds:
            return ""
        
        if timestamp < self.ds[key][0][1]:
            return ""

        if key in self.ds:
            res = ""
            l, r = 0, len(self.ds[key]) - 1
            while l <= r:
                mid = (l+r) // 2
                if self.ds[key][mid][1] <= timestamp:
                    res = self.ds[key][mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
            return res
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)