class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # T: O(N LOG N) | S: O(N)
        # N = Size of the input array
        pos_speed = sorted(zip(position, speed), reverse=True)
        fleets = []
        for pos, speed in pos_speed:
            time = (target - pos) / speed
            if not fleets or fleets[-1] < time:
                fleets.append(time)
        return len(fleets)
