class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs and sort them by position in descending order.
        # We process cars from the one closest to the target to the one farthest away.
        cars = sorted(zip(position, speed), reverse=True)
        # Use a stack to keep track of the arrival times of different car fleets.
        stack = []
        
        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)