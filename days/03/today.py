
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data


def calc_priority(item) -> int:
    if ord(item) > 96:
        return ord(item)-96
    else:
        return ord(item)-38


def part_one(data: list) -> int:
    counter = 0
    for items in data:
        firstpart, secondpart = items[:len(items)//2], items[len(items)//2:]
        for item in firstpart:
            if item in secondpart:
                counter += calc_priority(item)
                break
    return counter


def part_two(data: list) -> int:
    counter = 0
    i = 0
    while True:
        try:
            one, two, three = data[i], data[i+1], data[i+2]
        except:
            break
        for item in one:
            if item in two and item in three:
                counter += calc_priority(item)
                break
        i += 3
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
