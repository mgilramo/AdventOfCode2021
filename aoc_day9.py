import aoc_utils
from collections import Counter

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


class Coord:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def __str__(self):
        return f'[({self.x}, {self.y}) - {self.h}]'


def near_items(pos, positions):
    comp_list = []

    # Up
    up_pos_list = list(filter(lambda p: p.x == pos.x and p.y == pos.y + 1, positions))
    if len(up_pos_list):
        comp_list.append(up_pos_list[0])
    # Down
    down_pos_list = list(filter(lambda p: p.x == pos.x and p.y == pos.y - 1, positions))
    if len(down_pos_list):
        comp_list.append(down_pos_list[0])
    # Right
    right_pos_list = list(filter(lambda p: p.x == pos.x + 1 and p.y == pos.y, positions))
    if len(right_pos_list):
        comp_list.append(right_pos_list[0])
    # Left
    left_pos_list = list(filter(lambda p: p.x == pos.x - 1 and p.y == pos.y, positions))
    if len(left_pos_list):
        comp_list.append(left_pos_list[0])

    return comp_list


def puzzle1():
    with open('input_files\\day9_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda t: t.strip(), lines))

        positions = []
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                position = Coord(int(x), int(y), int(line[x]))
                positions.append(position)

    lp_list = []

    for pos in positions:
        comp_list = near_items(pos, positions)
        comp_list = list(map(lambda c: c.h, comp_list))

        if pos.h < min(comp_list):
            # Low Point
            lp_list.append(pos)

    risk_level = 0
    for lp in lp_list:
        risk_level += (lp.h + 1)

    return risk_level


def puzzle2():
    with open('input_files\\day9_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda t: t.strip(), lines))

        positions = []
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                position = Coord(int(x), int(y), int(line[x]))
                positions.append(position)

    lp_list = []

    pos_n = 0
    for pos in positions:
        pos_n += 1
        print(f'Checking position number {pos_n} out of {len(positions)}')
        comp_list = near_items(pos, positions)
        comp_list = list(map(lambda c: c.h, comp_list))

        if pos.h < min(comp_list):
            # Low Point
            lp_list.append(pos)

    basins = []
    check = 0
    for lp in lp_list:
        check += 1
        print(f'Checking low point number {check} out of {len(lp_list)}')
        # print(f'Low point: {lp}')
        next_pos = [lp]
        basin = [lp]
        while True:
            if not len(next_pos):
                break
            current_pos = list(next_pos)
            next_pos = list()

            for pos in current_pos:
                comp_list = near_items(pos, positions)
                for comp in comp_list:
                    if pos.h < comp.h < 9:
                        next_pos.append(comp)
                        # print(f'Adding to basin: {comp}')

            for pos in next_pos:
                filtered_basin = list(filter(lambda b: b.x == pos.x and b.y == pos.y, basin))
                if not len(filtered_basin):
                    basin.append(pos)
        basins.append(len(basin))

    sorted_basins = list(sorted(basins, reverse=True))
    selected_basins = sorted_basins[:3]

    result = 1
    for sb in selected_basins:
        result *= sb

    return result


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(9)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
