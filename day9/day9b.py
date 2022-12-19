def main(data) -> int:
    """
    >>> ex_data = '\\n'.join(["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"])
    >>> print(main(ex_data))
    36
    """
    data = data.splitlines()

    visited = set()
    knot_length = [[0, 0] for _ in range(9)]
    head = [0, 0]
    tail = knot_length[8]
    visited.add(tuple(tail))

    for line in data:
        direction, distance = line.split()
        distance = int(distance)

        for _ in range(distance):
            if direction == "U":
                head[1] += 1
            if direction == "D":
                head[1] -= 1
            if direction == "R":
                head[0] += 1
            if direction == "L":
                head[0] -= 1

            head_pos = head.copy()
            for knot in knot_length:
                dx = head_pos[0] - knot[0]
                dy = head_pos[1] - knot[1]
                if not (abs(dx) <= 1 and abs(dy) <= 1):
                    if dx != 0:
                        knot[0] += int(abs(dx) / dx)
                    if dy != 0:
                        knot[1] += int(abs(dy) / dy)
                head_pos = list(knot)
            visited.add(tuple(tail))

    return len(visited)


if __name__ == '__main__':
    input_data = open('input', 'r').read()
    print('part 2:', main(input_data))
