import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


class Dumbo:
    def __init__(self, x, y, e, grid):
        self.x = x
        self.y = y
        self.e = e
        self.f = False
        self.adjacent = []
        for v in range(self.y - 1, self.y + 2):
            for h in range(self.x - 1, self.x + 2):
                if 0 <= v <= grid - 1 and 0 <= h <= grid - 1 and (h, v) != (self.x, self.y):
                    self.adjacent.append((h, v))

    def flash(self):
        self.f = True

    def reset(self):
        if self.f:
            self.f = False
            self.e = 0

    def __str__(self):
        return f'({self.x}, {self.y}) - e: {self.e} - f: {self.f}'


def puzzle1():
    dumbo_list = []
    with open('input_files\\day11_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        for y_pos in range(len(lines)):
            line = lines[y_pos]
            for x_pos in range(len(line)):
                dumbo_item = Dumbo(x_pos, y_pos, int(line[x_pos]), len(line))
                dumbo_list.append(dumbo_item)

    # Number of turns
    turns = 100

    # Count number of flashes
    flash_count = 0

    for turn in range(turns):
        # Step 1 - add 1 energy to all dumbos
        for dumbo_item in dumbo_list:
            dumbo_item.e += 1

        # Step 2 - filter all items with energy above than 9 that haven't been flashed
        dumbos_to_flash = list(filter(lambda dtf: dtf.e > 9 and not dtf.f, dumbo_list))

        while len(dumbos_to_flash) > 0:
            # Step 3 - flash those items and create a list with their adjacent
            adjacent_dumbos = []
            for dumbo_to_flash in dumbos_to_flash:
                dumbo_to_flash.flash()
                flash_count += 1
                for coord_adj_x, coord_adj_y in dumbo_to_flash.adjacent:
                    adjacent_dumbo = list(filter(lambda ad: ad.x == coord_adj_x and ad.y == coord_adj_y, dumbo_list))[0]
                    adjacent_dumbos.append(adjacent_dumbo)

            # step 4 - add 1 energy to the adjacent (if repeated, additional energy needs to be added)
            for adjacent_dumbo in adjacent_dumbos:
                adjacent_dumbo.e += 1

            # step 5 - return to step 2
            dumbos_to_flash = list(filter(lambda dtf: dtf.e > 9 and not dtf.f, dumbo_list))

        # step 6 - if step 2 does not return any value, un-flash all dumbos
        for dumbo_item in dumbo_list:
            dumbo_item.reset()

    for dumbo_item in dumbo_list:
        print(dumbo_item)

    return flash_count


def puzzle2():
    dumbo_list = []
    with open('input_files\\day11_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        for y_pos in range(len(lines)):
            line = lines[y_pos]
            for x_pos in range(len(line)):
                dumbo_item = Dumbo(x_pos, y_pos, int(line[x_pos]), len(line))
                dumbo_list.append(dumbo_item)

    # Number of turns
    turns = 10000

    for turn in range(turns):
        # Count number of flashes in each turn
        flash_count = 0

        # Step 1 - add 1 energy to all dumbos
        for dumbo_item in dumbo_list:
            dumbo_item.e += 1

        # Step 2 - filter all items with energy above than 9 that haven't been flashed
        dumbos_to_flash = list(filter(lambda dtf: dtf.e > 9 and not dtf.f, dumbo_list))

        while len(dumbos_to_flash) > 0:
            # Step 3 - flash those items and create a list with their adjacent
            adjacent_dumbos = []
            for dumbo_to_flash in dumbos_to_flash:
                dumbo_to_flash.flash()
                flash_count += 1
                for coord_adj_x, coord_adj_y in dumbo_to_flash.adjacent:
                    adjacent_dumbo = list(filter(lambda ad: ad.x == coord_adj_x and ad.y == coord_adj_y, dumbo_list))[0]
                    adjacent_dumbos.append(adjacent_dumbo)

            # step 4 - add 1 energy to the adjacent (if repeated, additional energy needs to be added)
            for adjacent_dumbo in adjacent_dumbos:
                adjacent_dumbo.e += 1

            # step 5 - return to step 2
            dumbos_to_flash = list(filter(lambda dtf: dtf.e > 9 and not dtf.f, dumbo_list))

        if flash_count == len(dumbo_list):
            return turn + 1

        # step 6 - if step 2 does not return any value, un-flash all dumbos
        for dumbo_item in dumbo_list:
            dumbo_item.reset()

    for dumbo_item in dumbo_list:
        print(dumbo_item)

    return flash_count


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(11)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
