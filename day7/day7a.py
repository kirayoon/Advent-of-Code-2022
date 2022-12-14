from collections import defaultdict

x = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

lines = x.splitlines()
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

print(sizes)

print(sum([size for size in sizes.values() if size < 100000]))

