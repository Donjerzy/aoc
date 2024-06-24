total = 0

with open('dimensions.txt') as f:
    for line in f:
        stripped_line = tuple(line.strip().split("x"))
        l, w, h = stripped_line
        side_one = 2*int(l)*int(w)
        side_two = 2*int(w)*int(h)
        side_three =  2*int(h)*int(l)
        sides = [int(l), int(w), int(h)]
        area = side_one + side_two + side_three
        lowest = sides[0]
        for x in sides:
            if x < lowest:
                lowest = x
        sides.remove(lowest)
        second_lowest = sides[0]
        for x in sides:
            if x < second_lowest:
                second_lowest = x
        total += second_lowest * lowest + area
print(total)

