class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # T: O(N LOG N) | S: O(N)
        # N = Size of input array
        position_speed = sorted(zip(position, speed), reverse=True)
        car_fleet = []
        for p, s in position_speed:
            hour = (target - p) / s
            if not car_fleet or car_fleet[-1] < hour:
                car_fleet.append(hour)
        return len(car_fleet)
