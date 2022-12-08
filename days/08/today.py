

def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    data2 = list()
    for item in data:
        data2.append([int(q) for q in list(item)])
    return data2

def is_visible(idx, data):
    h = data[idx[0]][idx[1]]
    ret = [True, True, True, True]
    # Up:
    try:
        for i in range (idx[0]-1, -1, -1):
            if data[i][idx[1]] >= h:
                ret[0] = False
                break
    except:
        pass
    # Left
    try:
        for i in range (idx[1]-1, -1, -1):
            if data[idx[0]][i] >= h:
                ret[1] = False
                break
    except:
        pass
    # Down:
    try:
        for i in range (idx[0]+1, len(data)):
            if data[i][idx[1]] >= h:
                ret[2] = False
                break
    except:
        pass
    # Right
    try:
        for i in range (idx[1]+1, len(data[0])):
            if data[idx[0]][i] >= h:
                ret[3] = False
                break
    except:
        pass
    return True in ret

def calc_score(idx, data):
    if (idx[0] == 0) or (idx[1] == 0) or (idx[0] == len(data)-1) or (idx[1] == len(data[0])-1): return 0
    h = data[idx[0]][idx[1]]
    dists = [0, 0, 0, 0]
    # Up
    delta = 1
    while True:
        try:
            tmp = data[idx[0]-delta][idx[1]]
            if idx[0]-delta < 0:break
        except:
            break
        dists[0] += 1
        if tmp >= h:
            break
        delta += 1
    # Down
    delta = 1
    while True:
        try:
            tmp = data[idx[0]+delta][idx[1]]
            if idx[0]-delta >= len(data):break
        except:
            break
        dists[1] += 1
        if tmp >= h:
            break
        delta += 1
    # Left
    delta = 1
    while True:
        try:
            tmp = data[idx[0]][idx[1]-delta]
            if idx[1]-delta < 0:break
        except:
            break
        dists[2] += 1
        if tmp >= h:
            break
        delta += 1
    # Right
    delta = 1
    while True:
        try:
            tmp = data[idx[0]][idx[1]+delta]
            if idx[1]+delta >= len(data[0]):break
        except:
            break
        dists[3] += 1
        if tmp >= h:
            break
        delta += 1
    return dists[0] * dists[1] * dists[2] * dists[3]

    


def part_one(data: list) -> int:
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_visible((i, j), data): counter += 1
    return counter


def part_two(data: list) -> int:
    counter = list()
    for i in range(len(data)):
        for j in range(len(data[0])):
            counter.append(calc_score((i, j), data))
    return list(reversed(sorted(counter)))[0]


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
