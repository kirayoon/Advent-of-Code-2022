import string


def day3b(data: list[str]) -> int:
    """
    >>> ex_data = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    >>> print(day3b(ex_data))
    70
    """
    low_letters = string.ascii_lowercase
    up_letters = string.ascii_uppercase

    common_letters = []
    score = 0
    counter = 3

    # find common letters in each group of three lines
    for i in range(0, len(data), counter):
        for each_letter in data[i]:
            if each_letter in data[i + 1] and each_letter in data[i + 2]:
                common_letters.append(each_letter)
                break

    # calculate score
    for letter in common_letters:
        if letter.islower():
            score += low_letters.index(letter) + 1
        else:
            score += up_letters.index(letter) + 27

    return score


if __name__ == '__main__':
    with open("input", "r") as f:
        text = f.read().splitlines()
    print(day3b(text))
