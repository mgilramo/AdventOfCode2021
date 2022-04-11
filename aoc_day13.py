import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


class DottedPaper:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = {}
        for x in range(w):
            for y in range(h):
                self.grid[(x, y)] = False

    def __str__(self):
        grid_str = ''
        for y in range(self.h):
            line_str = ''
            for x in range(self.w):
                if self.grid[(x, y)]:
                    line_str += '#'
                else:
                    line_str += '·'
            line_str += '\n'
            grid_str += line_str
        return grid_str

    def dot(self, x, y):
        self.grid[(x, y)] = True

    def fold_x(self, x_fold):
        resulting_paper = DottedPaper(x_fold, self.h)
        for x in range(x_fold):
            for y in range(self.h):
                x_dist = (self.w - 1) - x
                resulting_paper.grid[(x, y)] = self.grid[(x, y)] or self.grid[(x_dist, y)]

        return resulting_paper

    def fold_y(self, y_fold):
        resulting_paper = DottedPaper(self.w, y_fold)
        for x in range(self.w):
            for y in range(y_fold):
                y_dist = (self.h - 1) - y
                resulting_paper.grid[(x, y)] = self.grid[(x, y)] or self.grid[(x, y_dist)]

        return resulting_paper


def puzzle1():
    with open('input_files\\day13_input.txt', 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda l: l.strip(), lines))
    print(lines)

    initial_dots = []
    dots_x = []
    dots_y = []

    fold_list = []

    for line in lines:
        if ',' in line:
            pos = line.split(',')
            dots_x.append(int(pos[0]))
            dots_y.append(int(pos[1]))
            initial_dots.append([int(pos[0]), int(pos[1])])
        elif 'fold along' in line:
            split1 = line.split()
            split2 = split1[-1].split('=')
            fold_list.append([split2[0], int(split2[1])])

    puzzle_input = DottedPaper(max(dots_x) + 1, max(dots_y) + 1)

    for dot in initial_dots:
        puzzle_input.dot(dot[0], dot[1])

    # print(puzzle_input)

    # print(fold_list)

    if fold_list[0][0] == 'y':
        fold_input = puzzle_input.fold_y(fold_list[0][1])
    elif fold_list[0][0] == 'x':
        fold_input = puzzle_input.fold_x(fold_list[0][1])

    # print(fold_input)

    result_values = list(filter(lambda fi: fi, fold_input.grid.values()))

    return len(result_values)


def puzzle2():
    with open('input_files\\day13_input.txt', 'r') as f:
        lines = f.readlines()

    lines = list(map(lambda l: l.strip(), lines))
    print(lines)

    initial_dots = []
    dots_x = []
    dots_y = []

    fold_list = []

    for line in lines:
        if ',' in line:
            pos = line.split(',')
            dots_x.append(int(pos[0]))
            dots_y.append(int(pos[1]))
            initial_dots.append([int(pos[0]), int(pos[1])])
        elif 'fold along' in line:
            split1 = line.split()
            split2 = split1[-1].split('=')
            fold_list.append([split2[0], int(split2[1])])

    puzzle_input = DottedPaper(max(dots_x) + 1, max(dots_y) + 1)

    for dot in initial_dots:
        puzzle_input.dot(dot[0], dot[1])

    # print(puzzle_input)

    # print(fold_list)

    fold_input = puzzle_input

    for fold in fold_list:
        if fold[0] == 'y':
            fold_input_new = fold_input.fold_y(fold[1])
        elif fold[0] == 'x':
            fold_input_new = fold_input.fold_x(fold[1])
        fold_input = fold_input_new

    print(fold_input)

    result_values = list(filter(lambda fi: fi, fold_input.grid.values()))

    return len(result_values)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(13)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
