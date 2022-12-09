
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data


def make():
    field = []
    for _ in range(500):
        tmp = []
        for _ in range(500):
            tmp.append(False)
        field.append(tmp)
    return field

def dist(head, tail):
    if abs(head[0]-tail[0]) < 2 and abs(head[1]-tail[1]) < 2: return [0, 0]
    delta = [0, 0]
    if head[1] > tail[1]: delta[1] = 1
    if head[1] < tail[1]: delta[1] = -1
    if head[0] > tail[0]: delta[0] = 1
    if head[0] < tail[0]: delta[0] = -1
    return delta


def part_one(data: list) -> int:
    field = make()
    head = [250, 250]
    tail = [250, 250]
    for command in data:
        field[tail[0]][tail[1]] = True
        direction = command.split(" ")[0]
        amount = int(command.split(" ")[1])
        for _ in range(amount):
            if direction == "R": head[1] += 1
            if direction == "L": head[1] -= 1
            if direction == "U": head[0] -= 1
            if direction == "D": head[0] += 1
            tmp = dist(head, tail)
            tail = [tail[0]+tmp[0], tail[1]+tmp[1]]
            field[tail[0]][tail[1]] = True
    counter = 0
    for row in field:
        for item in row:
            if item: counter += 1
    return counter




def part_two(data: list) -> int:
    field = make()
    locations = list()
    for i in range(10):
        locations.append([250, 250])
    for command in data:
        field[locations[9][0]][locations[9][1]] = True
        direction = command.split(" ")[0]
        amount = int(command.split(" ")[1])
        for _ in range(amount):
            if direction == "R": locations[0][1] += 1
            if direction == "L": locations[0][1] -= 1
            if direction == "U": locations[0][0] -= 1
            if direction == "D": locations[0][0] += 1
            for i in range(9):
                tmp = dist(locations[i], locations[i+1])
                locations[i+1] = [locations[i+1][0]+tmp[0], locations[i+1][1]+tmp[1]]
            field[locations[9][0]][locations[9][1]] = True
    counter = 0
    for row in field:
        for item in row:
            if item: counter += 1
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
