import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def puzzle1():
    with open('input_files\\day7_input.txt', 'r') as f:
        initial_positions = f.readline().split(',')
        initial_positions = list(map(lambda x: int(x), initial_positions))

        options = list(initial_positions)
        fuel_list = []

        for option in options:
            fuel = 0
            for initial_position in initial_positions:
                fuel += abs(option - initial_position)
            fuel_list.append(fuel)

        return min(fuel_list)


def puzzle2():
    with open('input_files\\day7_input.txt', 'r') as f:
        initial_positions = f.readline().split(',')
        initial_positions = list(map(lambda x: int(x), initial_positions))

        max_option = max(initial_positions)
        
        fuel_list = []

        # print(f'Different options: {max(options)}')

        for option in range(1, max_option + 1):
            # print(f'Option: {option}')
            fuel = 0
            for initial_position in initial_positions:
                steps = abs(option - initial_position)

                for step in range(1, steps+1):
                    fuel += step

            fuel_list.append(fuel)

    return min(fuel_list)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(7)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
