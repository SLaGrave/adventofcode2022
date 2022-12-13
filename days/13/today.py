
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    new_data = list()
    for item in data:
        if item != "":
            new_data.append(eval(item))
    return new_data

def test(left, right):
    if type(left) == int and type(right) == int:
        if left < right: return 1
        elif right < left: return -1
        else: return None
    if type(left) == list and type(right) == list:
        for i in range(max(len(right), len(left))):
            try:
                x = test(left[i], right[i])
                if x == 1 or x == -1: return x
            except:
                if len(left) < len(right):
                    return 1
                elif len(right) < len(left):
                    return -1
                else:
                    return None
    if type(left) != list and type(right) == list:
        return test([left], right)
    elif type(right) != list and type(left) == list:
        return test(left, [right])

def part_one(data: list) -> int:
    counter = 0
    idx = 0
    while True:
        try:
            left = data[2*idx]
            right = data[(2*idx)+1]
        except:
            break
        print(left, right)
        x = test(left, right)
        print(x)
        if x:
            counter += idx+1
        idx += 1

    return counter

from functools import cmp_to_key

def part_two(data: list) -> int:
    data.append([[2]])
    data.append([[6]])
    data.sort(key=cmp_to_key(test), reverse=True)
    print(data)
    return (data.index([[2]])+1)*(data.index([[6]])+1)


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    # ans = part_one(get_data())
    # print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
