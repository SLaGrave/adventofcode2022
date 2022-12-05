
STACKS1 = [
    'GTRW',
    'GCHPMSVW',
    'CLTSGM',
    'JHDMWRF',
    'PQLHSWFJ',
    'PJDNFMS',
    'ZBDFGCSJ',
    'RTB',
    'HNWLC'
]

STACKS2 = [
    'GTRW',
    'GCHPMSVW',
    'CLTSGM',
    'JHDMWRF',
    'PQLHSWFJ',
    'PJDNFMS',
    'ZBDFGCSJ',
    'RTB',
    'HNWLC'
]

def get_data() -> list:
    with open("./input_keep.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    data2 = []
    for item in data:
        item = item.replace("move ", "")
        item = item.replace(" from ", ",")
        item = item.replace(" to ", ",")
        data2.append([int(q) for q in item.split(",")])
    return data2

def part_one(data: list) -> int:
    for item in data:
        move = STACKS1[item[1]-1][0-item[0]:]
        STACKS1[item[1]-1] = STACKS1[item[1]-1][:0-item[0]]
        STACKS1[item[2]-1] = STACKS1[item[2]-1] + move[::-1]
    s = ''
    for stack in STACKS1:
        s += stack[-1]
    return s


def part_two(data: list) -> int:
    for item in data:
        move = STACKS2[item[1]-1][0-item[0]:]
        STACKS2[item[1]-1] = STACKS2[item[1]-1][:0-item[0]]
        STACKS2[item[2]-1] = STACKS2[item[2]-1] + move
    s = ''
    for stack in STACKS2:
        s += stack[-1]
    return s


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
