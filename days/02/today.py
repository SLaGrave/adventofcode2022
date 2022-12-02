
def get_data() -> list:
    with open("./input.txt", "r") as f:
        data = f.readlines()
    # Strip end of line
    data = [q.strip() for q in data]
    # Make int
    # data = [int(q) for q in data]
    return data

SCORE_VALUE = {"rock": 1, "paper": 2, "scissors": 3}
ENEMY_MAPPING = {"A": "rock", "B": "paper", "C": "scissors"}
ME_MAPPING = {"X": "rock", "Y": "paper", "Z": "scissors"}
GOAL_MAPPING = {"X": "lose", "Y": "draw", "Z": "win"}

def play_game(me, enemy) -> int:
    if me == enemy: return 3
    if me == "rock" and enemy == "scissors": return 6
    if me == "paper" and enemy == "rock": return 6
    if me == "scissors" and enemy == "paper": return 6
    return 0

def get_move(goal, enemy) -> str:
    if goal == "draw": return enemy
    if enemy == "rock": return "paper" if goal=="win" else "scissors"
    if enemy == "paper": return "scissors" if goal=="win" else "rock"
    if enemy == "scissors": return "rock" if goal=="win" else "paper"


def part_one(data: list) -> int:
    scores = list()
    for item in data:
        plays = item.split(" ")
        me = ME_MAPPING[plays[1]]
        enemy = ENEMY_MAPPING[plays[0]]
        scores.append(SCORE_VALUE[me] + play_game(me, enemy))

    return sum(scores)


def part_two(data: list) -> int:
    scores = list()
    for item in data:
        plays = item.split(" ")
        goal = GOAL_MAPPING[plays[1]]
        enemy = ENEMY_MAPPING[plays[0]]
        move = get_move(goal, enemy)
        scores.append(SCORE_VALUE[move] + play_game(move, enemy))

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
