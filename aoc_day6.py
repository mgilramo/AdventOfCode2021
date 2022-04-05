import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = True
RUN_PUZZLE_2 = True


def puzzle1():
    with open('input_files\\day6_input.txt', 'r') as f:
        lf_list = f.readline().split(',')
        lf_list = list(map(lambda x: int(x), lf_list))
        for n in range(80):
            to_extend = []
            for lf in range(len(lf_list)):
                if lf_list[lf]:
                    lf_list[lf] = lf_list[lf] - 1
                else:
                    lf_list[lf] = 6
                    to_extend.append(8)
            lf_list.extend(to_extend)
    return len(lf_list)


def puzzle2():
    with open('input_files\\day6_input.txt', 'r') as f:
        lf_list = f.readline().split(',')
        lf_list = list(map(lambda x: int(x), lf_list))

        initial_list = []
        for e1 in range(9):
            initial_list.append(0)

        for lf in lf_list:
            initial_list[lf] = initial_list[lf] + 1

        empty_list = []
        for e2 in range(9):
            empty_list.append(0)

        start_day_list = list(initial_list)

        days = 128

        for d in range(days):
            final_day_list = list(empty_list)

            for pos in range(8):
                final_day_list[pos] = start_day_list[pos + 1]

            # Special Cases
            final_day_list[6] = final_day_list[6] + start_day_list[0]
            final_day_list[8] = start_day_list[0]

            start_day_list = list(final_day_list)

        return sum(start_day_list)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(6)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
