import re


def day4a(data: list[str]) -> int:
    """
    >>> ex_data = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]
    >>> print(day4a(ex_data))
    2
    """
    score = 0

    for i in data:
        each_line = re.findall(r"\d+", i)
        if (int(each_line[0]) <= int(each_line[2]) and int(each_line[1]) >= int(each_line[3])) or \
                (int(each_line[0]) >= int(each_line[2]) and int(each_line[1]) <= int(each_line[3])):
            score += 1

    return score


if __name__ == '__main__':
    with open("input", "r") as f:
        text = f.read().splitlines()
    print(day4a(text))
