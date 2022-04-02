import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def puzzle1():
    with open('input_files\\day2_input.txt', 'r') as f:
        h_pos = 0
        v_pos = 0

        lines = f.readlines()

        for line in lines:
            action = line.split(' ')
            if action[0].lower() == 'forward':
                h_pos += int(action[1])
            elif action[0].lower() == 'down':
                v_pos += int(action[1])
            elif action[0].lower() == 'up':
                v_pos -= int(action[1])

    result = h_pos * v_pos

    return result


def puzzle2():
    with open('input_files\\day2_input.txt', 'r') as f:
        aim = 0
        h_pos = 0
        v_pos = 0

        lines = f.readlines()

        for line in lines:
            action = line.split(' ')
            if action[0].lower() == 'forward':
                h_pos += int(action[1])
                v_pos += (aim * int(action[1]))
            elif action[0].lower() == 'down':
                aim += int(action[1])
            elif action[0].lower() == 'up':
                aim -= int(action[1])

    result = h_pos * v_pos

    return result


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(2)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')