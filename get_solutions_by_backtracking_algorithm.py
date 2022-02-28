import time


board1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

board2 = [
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
]


def print_board(board):
    for row in board:
        print("\t".join(map(str, row)))
    print("-" * 35)


def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None


def is_valid(board, row, col, value):
    # Check for row and column constraint
    for i in range(9):
        if value in [board[row][i], board[i][col]]:
            return False

    # Check for box constraint
    box_row_index = row // 3
    box_col_index = col // 3
    for r in range(3):
        for c in range(3):
            if board[box_row_index * 3 + r][box_col_index * 3 + c] == value:
                return False

    return True


def get_solutions_by_backtracking(board, solutions):
    # If only a single solution is desired
    # if solutions:
    #     return

    # locating the empty cell
    empty_cell = find_empty_cell(board)

    # base case: solution is found
    if empty_cell is None:
        solutions.append([[cell for cell in row] for row in board])
        return

    # fill in the empty cell with a value and perform backtracking algorithm thereafter
    row, col = empty_cell
    for value in range(1, 10):
        if is_valid(board, row, col, value):
            board[row][col] = value
            get_solutions_by_backtracking(board, solutions)
            board[row][col] = 0


if __name__ == "__main__":
    # display initial board state
    print_board(board1)

    # perform backtracking algorithm
    clock_start = time.time()
    solutions = []
    get_solutions_by_backtracking(board1, solutions)
    clock_end = time.time()

    # display all solutions
    for solution in solutions:
        print_board(solution)

    # display processing time
    print(f"Processing time: {len(solutions)} solutions in {round(clock_end - clock_start, 2)} seconds")