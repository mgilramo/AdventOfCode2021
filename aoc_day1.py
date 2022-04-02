import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def puzzle1():
    with open('input_files\\day1_input.txt', 'r') as f:
        result = 0
        lines = f.readlines()
        for x in range(1, len(lines)):
            if int(lines[x]) > int(lines[x-1]):
                result += 1
        return result


def puzzle2():
    with open('input_files\\day1_input.txt', 'r') as f:
        result = 0
        lines = f.readlines()
        lines_sum = []

        for x in range(1, len(lines)-1):
            lines_sum.append(int(lines[x-1]) + int(lines[x]) + int(lines[x+1]))

        # print(lines_sum)

        for y in range(1, len(lines_sum)):
            if lines_sum[y] > lines_sum[y - 1]:
                result += 1

        return result


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(1)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')