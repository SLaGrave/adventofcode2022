
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data

def part_one(data: list) -> int:
    data = data[0]
    counter = 4
    while True:
        chars = data[counter-4:counter]
        flag = True
        for c in chars:
            if chars.count(c) > 1: flag = False
        if flag: return counter
        counter += 1


def part_two(data: list) -> int:
    data = data[0]
    counter = 14
    while True:
        chars = data[counter-14:counter]
        flag = True
        for c in chars:
            if chars.count(c) > 1: flag = False
        if flag: return counter
        counter += 1


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
