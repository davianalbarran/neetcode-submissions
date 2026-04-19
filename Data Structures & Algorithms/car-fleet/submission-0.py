class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_pairs = [[pos, speed] for pos, speed in zip(position, speed)]
        fleet_stack = []

        for pos, speed in reversed(sorted(pos_speed_pairs)):
            fleet_stack.append((target - pos) / speed)

            if len(fleet_stack) >= 2 and fleet_stack[-1] <= fleet_stack[-2]:
                fleet_stack.pop()
        
        return len(fleet_stack)