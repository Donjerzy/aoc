visited_houses = {(0,0)}
directions = ''

with open('directions.txt') as f:
    directions = f.read().strip()

current = [0,0]
for direction in directions:
    if direction == '^':
        current[1] += 1
        visited_houses.add(tuple(current))
    elif direction == 'v':
        current[1] -= 1
        visited_houses.add(tuple(current))
    elif direction == '>':
        current[0] += 1
        visited_houses.add(tuple(current))
    elif direction == '<':
        current[0] -= 1
        visited_houses.add(tuple(current))

print(len(visited_houses))

