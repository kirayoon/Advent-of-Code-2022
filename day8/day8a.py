def visible(data, row, col):
    """
    As soon as 1 direction is visible, return True
    At each direction, as soon as it's not visible, set visibility to False and break out of the for loop
    """
    visibility = True
    for up in range(row - 1, -1, -1):
        if data[row][col] <= data[up][col]:
            visibility = False
            break
        else:
            visibility = True
    if visibility:
        return visibility

    for right in range(col + 1, len(data[row])):
        if data[row][col] <= data[row][right]:
            visibility = False
            break
        else:
            visibility = True
    if visibility:
        return visibility

    for down in range(row + 1, len(data)):
        if data[row][col] <= data[down][col]:
            visibility = False
            break
        else:
            visibility = True
    if visibility:
        return visibility

    for left in range(col - 1, -1, -1):
        if data[row][col] <= data[row][left]:
            visibility = False
            break
        else:
            visibility = True
    if visibility:
        return visibility


def day8a(data):
    """
    >>> ex_data = '\\n'.join(["30373", "25512", "65332", "33549", "35390"])
    >>> print(day8a(ex_data))
    21
    """
    data = data.split()

    # find the number of trees on the edge
    forest_height = len(data)
    forest_width = len(data[0])
    edge_trees = 2 * forest_height + 2 * forest_width - 4

    counter = 0
    for row in range(1, forest_height - 1):
        for col in range(1, forest_width - 1):
            if visible(data, row, col):
                counter += 1
    return counter + edge_trees


if __name__ == '__main__':
    input_data = open('input', 'r').read()
    print('part 1:', day8a(input_data))

