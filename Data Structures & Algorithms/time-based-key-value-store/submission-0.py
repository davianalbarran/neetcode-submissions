class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.map.get(key, [])
        values.append((value, timestamp))
        self.map[key] = values

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, ())

        if not values:
            return ""
        
        # brute force is prob something like this in O(n)
        # closest_match = ("", -1)
        # for pair in values:
        #     if pair[1] <= timestamp and closest_match[1] < pair[1]:
        #         closest_match = pair
        
        # return closest_match[0]

        l, r = 0, len(values) - 1
        closest_match = ("", -1)

        while l <= r:
            mid = (r + l) // 2

            if values[mid][1] <= timestamp:
                closest_match = values[mid]
                l = mid + 1
            else:
                r = mid - 1
        
        return closest_match[0]