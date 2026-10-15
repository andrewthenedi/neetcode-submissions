class TimeMap:

    def __init__(self):
        # T: O(1) | S: O(M * N)
        # M = Size of key
        # N = Size of timestamp and value
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # T: O(1) | S: O(1)
        timestamp_and_value = (timestamp, value)
        if key not in self.time_map or self.time_map[key][-1] != timestamp_and_value:
            self.time_map[key].append(timestamp_and_value)

    def get(self, key: str, timestamp: int) -> str:
        # T: O(LOG N) | S: O(1)
        value = ""
        if key not in self.time_map:
            return value
        timestamp_and_value = self.time_map[key]
        l, r = 0, len(timestamp_and_value) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if timestamp_and_value[mid][0] <= timestamp:
                value = timestamp_and_value[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return value
