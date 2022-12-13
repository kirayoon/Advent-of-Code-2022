x = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


with open("input", "r") as f:
    data = f.read()

largest_sum = [0, 0, 0]


def get_largest_sum(data):
    global largest_sum
    groups = data.split("\n\n")

    for number in groups:
        numbers = number.split("\n")

        numbers = [int(i) for i in numbers]

        total = sum(numbers)

        for j in range(3):
            if total > largest_sum[j]:
                largest_sum[j + 1:] = largest_sum[j:-1]
                largest_sum[j] = total
                break

    return sum(largest_sum)

    # sums = [sum([int(n) for n in g.split("\n")]) for g in groups]
    # return max(sums)


print(get_largest_sum(data))
