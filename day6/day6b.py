def main(data: str) -> int:
    """
    >>> x = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    >>> main(x)
    19
    >>> x = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    >>> main(x)
    23
    >>> x = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    >>> main(x)
    26
    """
    fourteen = data[:14]
    for i in range(14, len(data)):
        if len(set(fourteen)) == 14:
            return i
        fourteen = fourteen[1:] + data[i]


if __name__ == '__main__':
    file_data = open("input", 'r').read()
    print(main(file_data))
