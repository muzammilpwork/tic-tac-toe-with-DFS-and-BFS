import random


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = '0'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            # self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.current_player == "X":
                self.current_player = '0'
            else:
                self.current_player = 'X'
            return True
        return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)


def depth_first_search(board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == player:
                if dfs_helper(board, player, row, col, set()):
                    return True
    return False

def dfs_helper(board, player, row, col, visited):
    if (row, col) not in visited:
        visited.add((row, col))
        if len(visited) == 3:
            return True
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= i < 3 and 0 <= j < 3 and board[i][j] == player:
                if dfs_helper(board, player, i, j, visited):
                    return True
    return False

def breadth_first_search(board, player):
    for row in range(3):
        for col in range(3):
            if board[row][col] == player:
                if bfs_helper(board, player, row, col):
                    return True
    return False

def bfs_helper(board, player, start_row, start_col):
    queue = [(start_row, start_col)]
    visited = set(queue)

    while queue:
        row, col = queue.pop(0)

        # Check all adjacent cells
        for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= i < 3 and 0 <= j < 3 and board[i][j] == player and (i, j) not in visited:
                visited.add((i, j))
                queue.append((i, j))
                if len(visited) == 3:
                    return True

    return False

def computer_move(board, player):
    # Try to win using DFS
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                if depth_first_search(board, player):
                    return row, col
                board[row][col] = ' '

    # Try to win using BFS
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                if breadth_first_search(board, player):
                    return row, col
                board[row][col] = ' '

    # Block the user from winning using DFS
    opponent = 'X' if player == 'O' else 'O'
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = opponent
                if depth_first_search(board, opponent):
                    board[row][col] = player
                    return row, col
                board[row][col] = ' '

    # Block the user from winning using BFS
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = opponent
                if breadth_first_search(board, opponent):
                    board[row][col] = player
                    return row, col
                board[row][col] = ' '

    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)



tic_tac_toe = TicTacToe()

while True:
    tic_tac_toe.display_board()
    print("current player: ", tic_tac_toe.current_player)

    if tic_tac_toe.current_player == 'X':
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if not tic_tac_toe.make_move(row, col):
            print("Invalid move. Try again.")
            continue
    else:
        print("Computer's move:")
        row, col = computer_move(tic_tac_toe.board, '0')
        s = tic_tac_toe.make_move(row, col)

    winner = tic_tac_toe.check_winner()
    if winner:
        tic_tac_toe.display_board()
        print(f"{winner} wins!")
        break
    elif tic_tac_toe.is_board_full():
        tic_tac_toe.display_board()
        print("It's a tie!")
        break

