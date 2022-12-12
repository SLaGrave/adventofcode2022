from collections import deque


def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    data = [list(q) for q in data]
    start_list = list()
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if v == "S":
                start = (i, j)
                start_list.append(start)
                data[i][j] = "a"
            elif v == "E":
                end = (i, j)
                data[i][j] = "z"
            elif v == "a":
                start_list.append((i, j))
    return data, start, end, start_list


def traverse(map, start, end):
    q = deque()
    q.append((start, 0))
    visited = set()
    while q:
        position, distance = q.popleft()
        if position == end:
            return distance
        if position in visited:
            continue
        visited.add(position)
        x, y = position
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (0 <= x + dx < len(map)) and (0 <= y + dy < len(map[0])) and (ord(map[x + dx][y + dy]) - ord(map[x][y]) <= 1):
                q.append(((x + dx, y + dy), distance + 1))
    return float("inf")


def part_one(data: list) -> int:
    map = data[0]
    start = data[1]
    end = data[2]
    return traverse(map, start, end)


def part_two(data: list) -> int:
    map = data[0]
    start_list = data[3]
    end = data[2]
    return min([traverse(map, q, end) for q in start_list])


if __name__ == "__main__":
    print("#"*20)
    print("Part one")
    ans = part_one(get_data())
    print(f"Ans: {ans}")

    print("#"*20)
    print("Part two")
    ans = part_two(get_data())
    print(f"Ans: {ans}")
