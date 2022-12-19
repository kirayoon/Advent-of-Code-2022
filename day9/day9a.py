def touching(tail, head) -> bool:
    return all([abs(head[0] - tail[0]) <= 1, abs(head[1] - tail[1]) <= 1])


def main(data):
    """
    >>> ex_data = '\\n'.join(["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"])
    >>> print(main(ex_data))
    13
    """
    data = data.splitlines()

    visited = set()
    head = [0, 0]
    tail = [0, 0]
    visited.add(tuple(tail))

    for line in data:
        direction, distance = line.split()
        distance = int(distance)

        for _ in range(distance):
            head_old = head.copy()
            if direction == "U":
                head[1] += 1
            if direction == "D":
                head[1] -= 1
            if direction == "R":
                head[0] += 1
            if direction == "L":
                head[0] -= 1

            if not touching(tail, head):
                tail = head_old
                visited.add(tuple(tail))

    return len(visited)


if __name__ == '__main__':
    input_data = open('input', 'r').read()
    print('part 1:', main(input_data))
