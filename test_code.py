from aoc_day13 import DottedPaper


with open('input_files\\day13_test.txt', 'r') as f:
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

print(puzzle_input)

print(fold_list)

if fold_list[0][0] == 'y':
    fold_input = puzzle_input.fold_y(fold_list[0][1])
elif fold_list[0][0] == 'x':
    fold_input = puzzle_input.fold_x(fold_list[0][1])

print(fold_input)
result_values = list(filter(lambda fi: fi, fold_input.grid.values()))

print(len(result_values))