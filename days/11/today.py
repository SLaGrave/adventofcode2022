import math

class Monkey:
    def __init__(self, items, operation, test, t, f):
        self.items = items
        self.operation = operation
        self.test = test
        self.t = t
        self.f = f
        self.inspected = 0
    
    def take_turn(self, lcm = None):
        ret = []
        for item in self.items:
            # Inspect
            worry_level = self.operation(item)
            self.inspected += 1
            # Update
            if lcm is not None:
                worry_level = worry_level % lcm
            else:
                worry_level = int(worry_level/3)
            # Check who to throw to
            if worry_level % self.test == 0:
                ret.append((self.t, worry_level))
            else:
                ret.append((self.f, worry_level))
        self.items = list()
        return ret

def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]

    monkeys = list()
    i = 1
    while i < len(data):
        numbers = data[i].replace("Starting items: ", "")
        items = [int(q) for q in numbers.split(", ")]
        op = data[i+1].replace("Operation: new = ", "")
        def tmp(op):
            return lambda old: eval(op)
        test = int(data[i+2].replace("Test: divisible by ", ""))
        t = int(data[i+3].replace("If true: throw to monkey ", ""))
        f = int(data[i+4].replace("If false: throw to monkey ", ""))
        monkeys.append(Monkey(items, tmp(op), test, t, f))
        i += 7

    return monkeys


def part_one(data: list) -> int:
    data_one = data.copy()
    for _ in range(20):
        for m in data_one:
            changes = m.take_turn()
            for change in changes:
                data_one[change[0]].items.append(change[1])
    tmp = sorted([q.inspected for q in data_one])
    return tmp[-1]*tmp[-2]


def part_two(data: list) -> int:
    data_two = data.copy()
    lcm = math.lcm(*[q.test for q in data_two])
    for _ in range(10000):
        for m in data_two:
            changes = m.take_turn(lcm)
            for change in changes:
                data_two[change[0]].items.append(change[1])
    tmp = sorted([q.inspected for q in data_two])
    return tmp[-1]*tmp[-2]


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
