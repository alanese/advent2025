from itertools import pairwise, permutations

distances = {}
locations = set()

min_length = 0
with open("input-09.txt") as f:
    for line in f:
        line = line.split()
        distances[(line[0], line[2])] = int(line[4])
        distances[(line[2], line[0])] = int(line[4])
        locations.add(line[0])
        locations.add(line[2])
        min_length += int(line[4])

max_length = -1
for order in permutations(locations):
    route_length = 0
    for pair in pairwise(order):
        route_length += distances[pair]
    if min_length is None or route_length < min_length:
        min_length = route_length
    if route_length > max_length:
        max_length = route_length
print(min_length)
print(max_length)