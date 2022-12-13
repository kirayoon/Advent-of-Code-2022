def main(data: str) -> int:
    """
    >>> x = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    >>> main(x)
    7
    >>> x = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    >>> main(x)
    5
    >>> x = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    >>> main(x)
    11
    """
    four = data[:4]
    for i in range(4, len(data)):
        if len(set(four)) == 4:
            return i
        four = four[1:] + data[i]


if __name__ == '__main__':
    file_data = open("input", 'r').read()
    print(main(file_data))

