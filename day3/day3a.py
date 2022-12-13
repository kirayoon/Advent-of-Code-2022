import string


def day3a(data: list[str]) -> int:
    """
    >>> ex_data = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    >>> print(day3a(ex_data))
    157
    """
    low_letters = string.ascii_lowercase
    up_letters = string.ascii_uppercase

    common_letters = []
    score = 0

    # get letters in each compartment of rucksack
    for each_line in text:
        first_half = each_line[:int(len(each_line) / 2)]
        second_half = each_line[int(len(each_line) / 2):]
        # find letter that are in first_half and second_half
        for each_letter in first_half:
            if each_letter in second_half:
                common_letters.append(each_letter)
                break

    for letter in common_letters:
        if letter.islower():
            score += low_letters.index(letter) + 1
        else:
            score += up_letters.index(letter) + 27

    return score


if __name__ == '__main__':
    with open("input", "r") as f:
        text = f.read().splitlines()
    print(day3a(text))
