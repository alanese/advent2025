from typing import Dict, Tuple, Set
from itertools import permutations
from collections import defaultdict

def parse_line(line: str) -> Tuple[str, str, int]:
    """Returns (p1, p2, val) meaning p1 would gain/lose val points by sitting next to p2"""
    line_split = line.strip()[:-1].split()
    p1 = line_split[0]
    p2 = line_split[-1]
    val = int(line_split[3])
    if line_split[2] == "lose":
        val = -val
    return p1, p2, val

def arrangement_value(order: Tuple[str, ...], values: Dict[Tuple[str, str], int]) -> int:
    value = 0
    for i in range(len(order)-1):
        value += values[(order[i], order[i+1])] + values[(order[i+1], order[i])]
    value += values[(order[0], order[-1])] + values[(order[-1], order[0])]
    return value


values: Dict[Tuple[str, str], int] = defaultdict(lambda: 0)
people: Set[str] = set()


with open("input-13.txt") as f:
    for line in f:
        p1, p2, val = parse_line(line)
        values[(p1, p2)] = val
        people.add(p1)

max_happiness:int | None = None
for order in permutations(people):
    happiness = arrangement_value(order, values)
    if max_happiness is None or happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)

#-------------
people.add("me")
max_happiness = None
for order in permutations(people):
    happiness = arrangement_value(order, values)
    if max_happiness is None or happiness > max_happiness:
        max_happiness = happiness

print(max_happiness)