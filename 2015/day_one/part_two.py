directions = ''
with open('directions.txt', 'r') as f:
    directions = f.read()

current_position = 0
i = 0
basement = 0

while i < len(directions):
    if directions[i] == '(':
        current_position += 1
    elif directions[i] == ')':
        current_position -= 1
    if current_position == -1:
        basement = i + 1
        break
    i += 1

print(basement)