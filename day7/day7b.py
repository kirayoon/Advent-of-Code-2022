from collections import defaultdict


def day7a(lines: list[str]) -> int:
    """
    >>> ex_data = ["$ cd /", "$ ls", "dir a", "14848514 b.txt", "8504156 c.dat", "dir d", "$ cd a", "$ ls", "dir e", "29116 f", "2557 g", "62596 h.lst", "$ cd e", "$ ls", "584 i", "$ cd ..", "$ cd ..", "$ cd d", "$ ls", "4060174 j", "8033020 d.log", "5626152 d.ext", "7214296 k"]
    >>> print(day7a(ex_data))
    24933642
    """
    sizes = defaultdict(int)
    path = []

    for line in lines:
        if line.startswith('$ cd'):
            directory = line.split()[-1]
            if directory != '..':
                path.append(directory)
            else:
                path.pop()
        elif line.startswith('$ ls'):
            continue
        else:
            size = line.split()[0]
            if size.isdigit():
                for i in range(len(path)):
                    sizes['/'.join(path[:i + 1])] += int(size)

    unused = 70000000 - sizes['/']
    need = 30000000 - unused

    for v in sorted(sizes.values()):
        if v >= need:
            return v


if __name__ == '__main__':
    input_data = open('input', 'r').read().splitlines()
    print(day7a(input_data))


