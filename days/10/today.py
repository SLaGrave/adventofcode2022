
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data


def check(x):
    if x == 20:
        return True
    tmp = x-20
    if tmp % 40 == 0:
        return True
    return False

def part_one(data: list) -> int:
    counter = list()
    x = 1
    current_cycle = 1
    x_at_each = list()
    for command in data:
        if command == "noop":
            pass
        else:
            value = int(command.split(" ")[1])
            current_cycle += 1
            if check(current_cycle):
                counter.append(x*current_cycle)
            x_at_each.append(x)
            x += value
        current_cycle += 1
        if check(current_cycle):
            counter.append(x*current_cycle)
        x_at_each.append(x)
    return sum(counter), x_at_each


def part_two(data: list, x_at_each) -> int:
    counter = ""
    x = 1
    for clock_cycle in range(240):
        # Draw
        if abs((clock_cycle%40)-x) <= 1: counter += "#"
        else: counter += "."
        x = x_at_each[clock_cycle]
        

    print(counter[0:40])
    print(counter[41:80])
    print(counter[81:120])
    print(counter[121:160])
    print(counter[161:200])
    print(counter[201:240])
    return 0


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans, tmp = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data(), tmp)
    print(f"Ans: {ans}")
