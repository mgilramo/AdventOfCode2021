import aoc_utils
from collections import Counter

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def puzzle1():
    with open('input_files\\day3_input.txt', 'r') as f:
        order_lists = []
        for x in range(12):
            order_lists.append(list())

        lines = f.readlines()

        for line in lines:
            for x in range(12):
                order_list = order_lists[x]
                order_list.append(line[x])

        gamma = ''
        epsilon = ''

        for position in order_lists:
            c = Counter(position)
            if c['0'] > c['1']:
                gamma += '0'
                epsilon += '1'
            else:
                gamma += '1'
                epsilon += '0'

    decimal_gamma = int(gamma, 2)
    decimal_epsilon = int(epsilon, 2)

    result = decimal_gamma * decimal_epsilon

    return result


def puzzle2():
    with open('input_files\\day3_input.txt', 'r') as f:
        lines = f.readlines()

        # Oxygen Generator Rating
        ogr_list = list(lines)

        # CO2 Scrubber Rating
        csr_list = list(lines)

        # Most Repeated
        for x in range(12):
            pos_x_list = []
            for item in ogr_list:
                pos_x_list.append(item[x])

            c = Counter(pos_x_list)

            if c['1'] >= c['0']:
                to_filter = '1'
            else:
                to_filter = '0'

            ogr_list = list(filter(lambda n: n[x] == to_filter, ogr_list))

            if len(ogr_list) == 1:
                break

        # Less Repeated
        for x in range(12):
            pos_x_list = []
            for item in csr_list:
                pos_x_list.append(item[x])

            c = Counter(pos_x_list)

            if c['0'] <= c['1']:
                to_filter = '0'
            else:
                to_filter = '1'

            csr_list = list(filter(lambda n: n[x] == to_filter, csr_list))

            if len(csr_list) == 1:
                break

        decimal_ogr = int(ogr_list[0], 2)
        decimal_csr = int(csr_list[0], 2)

        result = decimal_ogr * decimal_csr

        return result


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(3)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
