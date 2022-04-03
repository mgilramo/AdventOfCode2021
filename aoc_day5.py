import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def puzzle1():
    board = {}

    for x in range(1000):
        for y in range(1000):
            board[(x, y)] = 0

    with open('input_files\\day5_input.txt', 'r') as f:
        while True:
            line = f.readline().split('->')
            if len(line) < 2:
                break

            position_1 = line[0].split(',')
            position_1 = list(map(lambda n: int(n), position_1))

            position_2 = line[1].split(',')
            position_2 = list(map(lambda n: int(n), position_2))

            print(f'Position 1: {position_1} ; Position 2: {position_2}')

            if position_1[0] == position_2[0]:
                if position_1[1] > position_2[1]:
                    r = range(position_2[1], position_1[1] + 1)
                else:
                    r = range(position_1[1], position_2[1] + 1)
                for new_y in r:
                    position_to_mark = (position_1[0], new_y)
                    # print(position_to_mark)
                    board[position_to_mark] += 1
            elif position_1[1] == position_2[1]:
                if position_1[0] > position_2[0]:
                    r = range(position_2[0], position_1[0] + 1)
                else:
                    r = range(position_1[0], position_2[0] + 1)
                for new_x in r:
                    position_to_mark = (new_x, position_1[1])
                    # print(position_to_mark)
                    board[position_to_mark] += 1

    # print(board)

    values = board.values()
    filtered_values = list(filter(lambda n: n >= 2, values))

    return len(filtered_values)


def puzzle2():
    board = {}

    for x in range(1000):
        for y in range(1000):
            board[(x, y)] = 0

    with open('input_files\\day5_input.txt', 'r') as f:
        while True:
            line = f.readline().split('->')
            if len(line) < 2:
                break

            position_1 = line[0].split(',')
            position_1 = list(map(lambda n: int(n), position_1))

            position_2 = line[1].split(',')
            position_2 = list(map(lambda n: int(n), position_2))

            print(f'Position 1: {position_1} ; Position 2: {position_2}')

            if position_1[0] == position_2[0]:
                if position_1[1] > position_2[1]:
                    r = range(position_2[1], position_1[1] + 1)
                else:
                    r = range(position_1[1], position_2[1] + 1)
                for new_y in r:
                    position_to_mark = (position_1[0], new_y)
                    # print(position_to_mark)
                    board[position_to_mark] += 1
            elif position_1[1] == position_2[1]:
                if position_1[0] > position_2[0]:
                    r = range(position_2[0], position_1[0] + 1)
                else:
                    r = range(position_1[0], position_2[0] + 1)
                for new_x in r:
                    position_to_mark = (new_x, position_1[1])
                    # print(position_to_mark)
                    board[position_to_mark] += 1
            else:
                initial_x = position_1[0]
                initial_y = position_1[1]
                total_movement = abs(position_1[0] - position_2[0]) + 1
                print('Im here')
                if position_1[0] > position_2[0]:
                    if position_1[1] > position_2[1]:
                        for add in range(total_movement):
                            position_to_mark = (initial_x - add, initial_y - add)
                            board[position_to_mark] += 1
                    elif position_1[1] < position_2[1]:
                        for add in range(total_movement):
                            position_to_mark = (initial_x - add, initial_y + add)
                            board[position_to_mark] += 1
                elif position_1[0] < position_2[0]:
                    if position_1[1] > position_2[1]:
                        for add in range(total_movement):
                            position_to_mark = (initial_x + add, initial_y - add)
                            board[position_to_mark] += 1
                    elif position_1[1] < position_2[1]:
                        for add in range(total_movement):
                            position_to_mark = (initial_x + add, initial_y + add)
                            board[position_to_mark] += 1


    # print(board)

    values = board.values()
    filtered_values = list(filter(lambda n: n >= 2, values))

    return len(filtered_values)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(5)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
