from typing import List, NamedTuple

class Reindeer(NamedTuple):
    name: str
    speed: int
    active_time: int
    recovery: int

def parse_line(line: str) -> Reindeer:
    line_split = line.split()
    return Reindeer(name = line_split[0],
                    speed = int(line_split[3]),
                    active_time = int(line_split[6]),
                    recovery = int(line_split[-2]))

#Used in initial p1 solution; not used in combined solution
def location_after(reindeer: Reindeer, time: int) -> int:
    cycle_time: int = reindeer.active_time + reindeer.recovery
    cycles: int
    rest:int
    cycles, rest = divmod(time, cycle_time)
    return cycles * reindeer.active_time * reindeer.speed + min(rest, reindeer.active_time) * reindeer.speed

def reindeer_movement(reindeer: Reindeer, time: int):
    cycle_time = reindeer.active_time + reindeer.recovery
    if time % cycle_time < reindeer.active_time:
        return reindeer.speed
    else:
        return 0

farthest: int = 0
reindeer_list: List[Reindeer] = []
with open("input-14.txt") as f:
    for line in f:
        reindeer = parse_line(line)
        reindeer_list.append(reindeer)

positions: List[int] = [0 for _ in reindeer_list]
scores: List[int] = [0 for _ in reindeer_list]

for i in range(2503):
    max_position = 0
    for r_index, reindeer in enumerate(reindeer_list):
        positions[r_index] += reindeer_movement(reindeer, i)
        max_position = max(max_position, positions[r_index])
    for p_index, position in enumerate(positions):
        if position == max_position:
            scores[p_index] += 1

print(max(positions))

print(max(scores))
    


