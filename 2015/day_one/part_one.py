directions = ''
with open('directions.txt', 'r') as f:
    directions = f.read()
movement = {'up': 0, 'down': 0}

for direction in directions:
    if direction == '(':
        movement['up'] += 1
    elif direction == ')':
        movement['down'] +=1

print(0 + movement['up'] - movement['down'])