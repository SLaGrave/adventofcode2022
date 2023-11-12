
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    data2 = list()
    for item in data:
        data2.append([list(eval(q)) for q in item.split(" -> ")])
    return data2


def line(x0, y0, x1, y1):
    Xs = range(x0, x1+1)
    if len(Xs) == 0: Xs = range(x1, x0+1)
    Ys = range(y0, y1+1)
    if len(Ys) == 0: Ys = range(y1, y0+1)
    Xs = list(Xs)
    Ys = list(Ys)
    if len(Xs) == 1: return [[Xs[0], q] for q in Ys]
    else: return [[q, Ys[0]] for q in Xs]

def part_one(data: list) -> int:
    counter = 0

    spawn = [500, 0]
    maxx = 500
    maxy = 0
    for item in data:
        for pair in item:
            if pair[0] > maxx: maxx = pair[0]
            if pair[1] > maxy: maxy = pair[1]
    
    map = list()
    for _ in range(maxy+1): map.append(["."] * (maxx+1))

    for item in data:
        idx = 0
        while idx < len(item)-1:
            start = item[idx]
            end = item[idx+1]
            for p in line(start[0], start[1], end[0], end[1]):
                map[p[1]][p[0]] = "#"
            idx += 1

    b = False
    while True:
        curr_pos = [500, 0]
        if b: break
        while True:
            if curr_pos[0] < 0 or curr_pos[0] >= maxx or curr_pos[1] >= maxy:
                b = True
                break
            if map[curr_pos[1]+1][curr_pos[0]] == ".":
                curr_pos[1] += 1
                continue
            elif map[curr_pos[1]+1][curr_pos[0]-1] == ".":
                curr_pos[1] += 1
                curr_pos[0] -= 1
                continue
            elif map[curr_pos[1]+1][curr_pos[0]+1] == ".":
                curr_pos[1] += 1
                curr_pos[0] += 1
                continue
            else:
                map[curr_pos[1]][curr_pos[0]] = "O"
                counter += 1
                break

    return counter


def part_two(data: list) -> int:
    counter = 0

    spawn = [500, 0]
    maxx = 500
    maxy = 0
    for item in data:
        for pair in item:
            if pair[0] > maxx: maxx = pair[0]
            if pair[1] > maxy: maxy = pair[1]
    
    map = list()
    for _ in range(maxy+1): map.append(["."] * (maxx+1000))
    map.append(["."] * (maxx+1000))
    map.append(["#"] * (maxx+1000))

    for item in data:
        idx = 0
        while idx < len(item)-1:
            start = item[idx]
            end = item[idx+1]
            for p in line(start[0], start[1], end[0], end[1]):
                map[p[1]][p[0]] = "#"
            idx += 1

    b = False
    while True:
        curr_pos = [500, 0]
        if b: break
        while True:
            if map[curr_pos[1]+1][curr_pos[0]] == ".":
                curr_pos[1] += 1
                continue
            elif map[curr_pos[1]+1][curr_pos[0]-1] == ".":
                curr_pos[1] += 1
                curr_pos[0] -= 1
                continue
            elif map[curr_pos[1]+1][curr_pos[0]+1] == ".":
                curr_pos[1] += 1
                curr_pos[0] += 1
                continue
            else:
                map[curr_pos[1]][curr_pos[0]] = "O"
                if curr_pos == [500, 0]: b = True
                counter += 1
                break

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
