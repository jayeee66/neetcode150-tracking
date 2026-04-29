class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:            
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.store.get(key, [])
        # print(values[0][1])
        l = 0
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
            
        return res
        
