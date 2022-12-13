with open("input", "r") as f:
    input_file = f.read().splitlines()


def get_score(data: list[str]) -> int:
    """
    >>> ex_data = '\\n'.join(["A Y", "B X", "C Z"]).splitlines()
    >>> print(get_score(ex_data))
    15
    """
    score = 0

    for each_round in data:
        each_round = each_round.split()
        enemy_choice = each_round[0]
        my_choice = each_round[1]

        if my_choice == 'X':
            score += 1
        elif my_choice == 'Y':
            score += 2
        elif my_choice == 'Z':
            score += 3

        if enemy_choice == 'A':
            if my_choice == 'X':
                score += 3
            elif my_choice == 'Y':
                score += 6
            elif my_choice == 'Z':
                score += 0

        elif enemy_choice == 'B':
            if my_choice == 'X':
                score += 0
            elif my_choice == 'Y':
                score += 3
            elif my_choice == 'Z':
                score += 6

        elif enemy_choice == 'C':
            if my_choice == 'X':
                score += 6
            elif my_choice == 'Y':
                score += 0
            elif my_choice == 'Z':
                score += 3

    return score


if __name__ == '__main__':
    print(get_score(input_file))
