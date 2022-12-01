
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
    rt = 0
    for item in data:
        if item != "": rt += int(item)
        else:
            if rt >= counter: counter = rt
            rt = 0
    return counter


def part_two(data: list) -> int:
    top1 = 0
    top2 = 0
    top3 = 0
    rt = 0
    for item in data:
        if item != "": rt += int(item)
        else:
            if rt >= top1:
                top3 = top2
                top2 = top1
                top1 = rt
            elif rt >= top2:
                top3 = top2
                top2 = rt
            elif rt >= top3:
                top3 = rt
            rt = 0
    return top1+top2+top3


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
