class TimeMap:

    def __init__(self):
        # S: O(M * N)
        # M = Size of keys
        # N = Size of values
        self.key_to_timestamp_value = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # T: O(1) | S: O(1)
        if key in self.key_to_timestamp_value and \
            self.key_to_timestamp_value[key][-1] == (timestamp, value):
                return
        self.key_to_timestamp_value[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # T: O(LOG N) | S: O(1)
        # N = Size of values
        if key not in self.key_to_timestamp_value:
            return ""
        timestamp_value = self.key_to_timestamp_value[key]
        l, r = 0, len(timestamp_value) - 1
        result = ""
        while l <= r:
            m = l + (r - l) // 2
            timestamp_mid, value_mid = timestamp_value[m]
            if timestamp_mid <= timestamp:
                result = value_mid
                l = m + 1
            else:
                r = m - 1
        return result
