def open_file(filename: str) -> tuple[list[str], list[str]]:
    f = open(filename, 'r').read()
    board, moves = f.split("\n\n")
    board, moves = board.splitlines(), moves.splitlines()
    moves = list(map(lambda sub: (''.join([ele for ele in sub if ele.isnumeric()])), moves))
    return board, moves


def main(filename: str) -> str:
    board, moves = open_file(filename)

    stack = [""] * 9

    for i in range(len(board) - 2, -1, -1):
        for r in range(1, len(board[0]), 4):
            if board[i][r].isupper():
                stack[r // 4] += board[i][r]

    for move in moves:
        num, origin, dest = int(move[:-2]), int(move[-2]), int(move[-1])
        origin_index, dest_index = origin - 1, dest - 1
        for _ in range(num):
            stack[dest_index] += stack[origin_index][-1]
            stack[origin_index] = stack[origin_index][:-1]

    answer = ""
    for top_stack in stack:
        answer += top_stack[-1]

    return answer


if __name__ == '__main__':
    print(main("input"))
