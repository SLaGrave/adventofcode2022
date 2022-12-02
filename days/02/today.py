
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data

def part_one(data: list) -> int:
    scores = list()
    for item in data:
        plays = item.split(" ")
        addition = 0
        if plays[0] == "A":
            if plays[1] == "Y": addition += 6
            if plays[1] == "Z": addition += 0
            if plays[1] == "X": addition += 3
        if plays[0] == "B":
            if plays[1] == "Y": addition += 3
            if plays[1] == "Z": addition += 6
            if plays[1] == "X": addition += 0
        if plays[0] == "C":
            if plays[1] == "Y": addition += 0
            if plays[1] == "Z": addition += 3
            if plays[1] == "X": addition += 6
        if plays[1] == "X": scores.append(1+addition)
        if plays[1] == "Y": scores.append(2+addition)
        if plays[1] == "Z": scores.append(3+addition)

    return sum(scores)


def part_two(data: list) -> int:
    scores = list()
    for item in data:
        plays = item.split(" ")
        addition = 0
        number = 0
        if plays[0] == "A":
            if plays[1] == "X":
                addition += 0
                number = 3
            if plays[1] == "Y":
                addition += 3
                number = 1
            if plays[1] == "Z":
                addition += 6
                number = 2
        if plays[0] == "B":
            if plays[1] == "X":
                addition += 0
                number = 1
            if plays[1] == "Y":
                addition += 3
                number = 2
            if plays[1] == "Z":
                addition += 6
                number = 3
        if plays[0] == "C":
            if plays[1] == "X":
                addition += 0
                number = 2
            if plays[1] == "Y":
                addition += 3
                number = 3
            if plays[1] == "Z":
                addition += 6
                number = 1
        scores.append(number+addition)

    return sum(scores)


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
