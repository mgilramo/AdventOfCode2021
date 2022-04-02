import aoc_utils

DOWNLOAD_INPUT = True
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = False


def puzzle1():
    return False


def puzzle2():
    return False


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(3)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')