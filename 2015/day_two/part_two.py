total = 0

with open('dimensions.txt') as f:
    for line in f:
        stripped_line = tuple(line.strip().split("x"))
        l, w, h = stripped_line
        volume = int(l) * int(w) * int(h)
        sides = [int(l), int(w), int(h)]
        lowest = sides[0]
        for x in sides:
            if x < lowest:
                lowest = x
        sides.remove(lowest)
        second_lowest = sides[0]
        for x in sides:
            if x < second_lowest:
                second_lowest = x
        total += volume + (lowest * 2) + (second_lowest * 2)

print(total)