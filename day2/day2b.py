input_data = open("input", "r").read().splitlines()


def get_score_part2(data: list[str]) -> int:
    """
    >>> ex_data = '\\n'.join(["A Y", "B X", "C Z"]).splitlines()
    >>> print(get_score_part2(ex_data))
    12
    """
    score = 0

    for each_round in data:
        each_round = each_round.split()
        enemy_choice = each_round[0]
        my_choice = each_round[1]

        if my_choice == 'X':
            score += 0  # need to lose
            if enemy_choice == 'A':
                score += 3  # choose scissors
            elif enemy_choice == 'B':
                score += 1  # choose rock
            elif enemy_choice == 'C':
                score += 2  # choose paper
        elif my_choice == 'Y':
            score += 3
            if enemy_choice == 'A':
                score += 1
            elif enemy_choice == 'B':
                score += 2
            elif enemy_choice == 'C':
                score += 3
        elif my_choice == 'Z':
            score += 6
            if enemy_choice == 'A':
                score += 2
            elif enemy_choice == 'B':
                score += 3
            elif enemy_choice == 'C':
                score += 1

    return score


if __name__ == '__main__':
    print(get_score_part2(input_data))
