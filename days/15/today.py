import math

def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    data2 = list()
    # Sensor at x=489739, y=1144461: closest beacon is at x=-46516, y=554951
    for line in data:
        line = line.replace("Sensor at x=", "")
        line = line.replace("y=", "")
        line = line.replace(": closest beacon is at x=", ",")
        line = line.replace("y=", "")
        tmp = eval(line)
        data2.append(list(tmp))
    return data2

def part_one(data: list) -> int:
    counter = 0
    Y = 2000000
    ranges = list()
    for pair in data:
        sx, sy, bx, by = pair
        man_dist = abs(sx-bx)+abs(sy-by)
        # If row Y within the range
        if (sy-man_dist) <= Y and Y <= (sy+man_dist):
            width = man_dist - abs(sy-Y)  # Width of the zone slice
            ranges.append((sx-width, sx+width))
    
    ranges = sorted(ranges)
    head = ranges[0][0]
    for x, y in ranges:
        if head < x:
            counter += y-x+1
            head = y
        elif head < y:
            counter += y-head
            head = y
    return counter



def part_two(data: list) -> int:
    for Y in range(4000000):
        ranges = list()
        for pair in data:
            sx, sy, bx, by = pair
            man_dist = abs(sx-bx)+abs(sy-by)
            if (sy-man_dist) <= Y and Y <= (sy+man_dist):
                width = man_dist - abs(sy-Y)  # Width of the zone slice
                ranges.append((sx-width, sx+width))
        ranges = sorted(ranges)
        head = ranges[0][0]
        for x, y in ranges:
            if head+1 < x:
                counter = Y + 4000000*(head+1)
            elif head < y:
                head = y
    return counter
            


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
