import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


class BingoItem:
    def __init__(self, number):
        self.number = number
        self.marked = False

    def mark_number(self):
        self.marked = True

    def __str__(self):
        return f'({self.number}, {self.marked})'


class BingoBoard:
    def __init__(self, board, size):
        self.board = []
        for number in board:
            bingo_item = BingoItem(number)
            self.board.append(bingo_item)
        self.size = size

    def mark_number(self, number):
        for bingo_item in self.board:
            if number == bingo_item.number:
                bingo_item.mark_number()

    def win(self):
        # Line Check
        for line_n in range(self.size):
            line_res = True
            for column_n in range(self.size):
                line_res = line_res and self.board[(line_n * self.size) + column_n].marked
            if line_res:
                break

        # Column Check
        for column_n in range(self.size):
            column_res = True
            for line_n in range(self.size):
                column_res = column_res and self.board[(line_n * self.size) + column_n].marked
            if column_res:
                break

        return line_res or column_res

    def __str__(self):
        board_str = ''
        for line_n in range(self.size):
            board_str += '['
            for column_n in range(self.size):
                board_item = self.board[(line_n * self.size) + column_n]
                board_str += board_item.__str__() + ', '
            board_str += ']\n'
        return board_str


def puzzle1():
    with open('input_files\\day4_input.txt') as f:
        # Number List - First Line
        number_list = f.readline().split(',')
        number_list = map(lambda x: int(x), number_list)

        # Empty Line
        f.readline()

        board_list = []

        while True:
            line1 = f.readline().split()
            if not len(line1):
                break
            line2 = f.readline().split()
            line3 = f.readline().split()
            line4 = f.readline().split()
            line5 = f.readline().split()

            board_numbers = line1 + line2 + line3 + line4 + line5
            board_numbers = map(lambda x: int(x), board_numbers)

            bingo_board = BingoBoard(board_numbers, 5)
            board_list.append(bingo_board)

            # Empty Line
            f.readline()

        for number in number_list:
            winner = False
            for board in board_list:
                board.mark_number(number)
                winner = board.win()
                if winner:
                    winner_board = board
                    break
            if winner:
                winner_number = number
                break

        sum_unmarked = 0
        for board_item in winner_board.board:
            if not board_item.marked:
                sum_unmarked += board_item.number

        result = sum_unmarked * winner_number
        return result


def puzzle2():
    with open('input_files\\day4_input.txt') as f:
        # Number List - First Line
        number_list = f.readline().split(',')
        number_list = map(lambda x: int(x), number_list)

        # Empty Line
        f.readline()

        board_list = []

        while True:
            line1 = f.readline().split()
            if not len(line1):
                break
            line2 = f.readline().split()
            line3 = f.readline().split()
            line4 = f.readline().split()
            line5 = f.readline().split()

            board_numbers = line1 + line2 + line3 + line4 + line5
            board_numbers = map(lambda x: int(x), board_numbers)

            bingo_board = BingoBoard(board_numbers, 5)
            board_list.append(bingo_board)

            # Empty Line
            f.readline()

        for number in number_list:
            boards_to_remove = []
            last_winner_number = 0
            for board in board_list:
                board.mark_number(number)
                if board.win() and len(board_list) > 1:
                    print(board)
                    boards_to_remove.append(board)
                elif board.win() and len(board_list) == 1:
                    last_winner_board = board
                    last_winner_number = number
                    break

            for board_to_remove in boards_to_remove:
                board_list.remove(board_to_remove)

            if last_winner_number:
                break

        sum_unmarked = 0
        for board_item in last_winner_board.board:
            if not board_item.marked:
                sum_unmarked += board_item.number

        result = sum_unmarked * last_winner_number
        return result


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(4)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
