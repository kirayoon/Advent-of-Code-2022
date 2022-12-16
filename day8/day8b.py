def visible_trees(data, row, col) -> int:
    """
    return the number of visible trees from the given position
    """
    score = 1

    dir_score = 0
    for up in range(row - 1, -1, -1):
        if data[row][col] > data[up][col]:
            dir_score += 1
        else:
            dir_score += 1
            break
    score *= dir_score

    dir_score = 0
    for right in range(col + 1, len(data[row])):
        if data[row][col] > data[row][right]:
            dir_score += 1
        else:
            dir_score += 1
            break
    score *= dir_score

    dir_score = 0
    for down in range(row + 1, len(data)):
        if data[row][col] > data[down][col]:
            dir_score += 1
        else:
            dir_score += 1
            break
    score *= dir_score

    dir_score = 0
    for left in range(col - 1, -1, -1):
        if data[row][col] > data[row][left]:
            dir_score += 1
        else:
            dir_score += 1
            break
    score *= dir_score

    return score


def day8b(data: str) -> int:
    """
    >>> ex_data = '\\n'.join(["30373", "25512", "65332", "33549", "35390"])
    >>> print(day8b(ex_data))
    8
    """
    data = data.splitlines()

    highest_score = 1

    for row in range(len(data)):
        for col in range(len(data[row])):
            scenic_score = visible_trees(data, row, col)
            highest_score = max(highest_score, scenic_score)

    return highest_score


if __name__ == '__main__':
    input_data = open('input', 'r').read()
    print(day8b(input_data))
