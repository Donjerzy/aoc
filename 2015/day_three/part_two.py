visited_houses = {(0,0)}
directions = ''

with open('directions.txt') as f:
    directions = f.read().strip()

current_santa = [0,0]
current_robot = [0,0]
santa_moves = True
for direction in directions:
    if santa_moves:
        if direction == '^':
            current_santa[1] += 1
            visited_houses.add(tuple(current_santa))
        elif direction == 'v':
            current_santa[1] -= 1
            visited_houses.add(tuple(current_santa))
        elif direction == '>':
            current_santa[0] += 1
            visited_houses.add(tuple(current_santa))
        elif direction == '<':
            current_santa[0] -= 1
            visited_houses.add(tuple(current_santa))
        santa_moves = False
    else:
        if direction == '^':
            current_robot[1] += 1
            visited_houses.add(tuple(current_robot))
        elif direction == 'v':
            current_robot[1] -= 1
            visited_houses.add(tuple(current_robot))
        elif direction == '>':
            current_robot[0] += 1
            visited_houses.add(tuple(current_robot))
        elif direction == '<':
            current_robot[0] -= 1
            visited_houses.add(tuple(current_robot))
        santa_moves = True
print(len(visited_houses))