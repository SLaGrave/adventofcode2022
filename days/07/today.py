import re

def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data

def simplify_dirs(name, dirs):
    new_items = []
    for item in dirs[name]:
        if type(item)==str:
            simplify_dirs(item, dirs)
            new_items.append(dirs[item])
        else: new_items.append(item)
    dirs[name] = sum(new_items)


def part_one(data: list) -> int:
    dirs = {}
    idx = 0
    pwd = []
    while True:
        try:
            command = data[idx]
        except:
            break
        match = re.search("\$ cd (.+)", command)
        if match:
            if match.group(1) == "..": pwd.pop()
            elif match.group(1) == "/": pwd = ["/"]
            else: pwd.append(match.group(1))
        match = re.search("\$ ls", command)
        if match:
            while True:
                idx += 1
                try:
                    value = data[idx]
                except:
                    break
                if value[0] == "$": break
                name = "/".join(pwd)
                if name not in dirs: dirs[name] = []
                v = value.split(" ")
                if v[0] == "dir":
                    if f"{name}/{v[1]}" not in dirs[name]: dirs[name].append(f"{name}/{v[1]}")
                else:
                    dirs[name].append(int(v[0]))
        else: idx += 1
    simplify_dirs("/", dirs)
    ans = 0
    for _, value in dirs.items():
        if value <= 100000: ans += value
    return ans, dirs, dirs["/"]


def part_two(ans, dirs, total) -> int:
    unused = 70000000 - total
    needed = 30000000 - unused
    sizes = []
    for _, value in dirs.items():
        if value >= needed: sizes.append(value)
    sizes = sorted(sizes)
    return sizes[0]


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans, dirs, total = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(ans, dirs, total)
    print(f"Ans: {ans}")
