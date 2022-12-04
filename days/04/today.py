
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data

def part_one(data: list) -> int:
    counter = 0
    for line in data:
        areas = line.split(",")
        one = [int(q) for q in areas[0].split("-")]
        two = [int(q) for q in areas[1].split("-")]
        if (one[0] <= two[1] and one[1] >= two[1]) or (two[0] <= one[0] and two[1] >= one[1]): counter += 1

    return counter


def part_two(data: list) -> int:
    counter = 0
    for line in data:
        areas = line.split(",")
        one = [int(q) for q in areas[0].split("-")]
        two = [int(q) for q in areas[1].split("-")]
        if (one[0] <= two[1] and one[1] >= two[0]) or (two[0] <= one[1] and two[1] >= one[1]): counter += 1

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
