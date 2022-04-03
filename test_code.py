board = {}

for x in range(5):
    for y in range(5):
        board[(x, y)] = 0

# print(board)

position_1 = [1, 4]
position_2 = [3, 2]

if position_1[0] == position_2[0]:
    if position_1[1] > position_2[1]:
        r = range(position_2[1], position_1[1] + 1)
    else:
        r = range(position_1[1], position_2[1] + 1)
    for new_y in r:
        position_to_mark = (position_1[0], new_y)
        board[position_to_mark] += 1
elif position_1[1] == position_2[1]:
    if position_1[0] > position_2[0]:
        r = range(position_2[0], position_1[0] + 1)
    else:
        r = range(position_1[0], position_2[0] + 1)
    for new_y in r:
        position_to_mark = (position_1[1], new_y)
        board[position_to_mark] += 1
else:
    initial_x = position_1[0]
    initial_y = position_1[1]
    total_movement = abs(position_1[0] - position_2[0]) + 1
    print('Im here')
    if position_1[0] > position_2[0]:
        if position_1[1] > position_2[1]:
            for add in range(total_movement):
                position_to_mark = (initial_x - add, initial_y - add)
                board[position_to_mark] += 1
        elif position_1[1] < position_2[1]:
            for add in range(total_movement):
                position_to_mark = (initial_x - add, initial_y + add)
                board[position_to_mark] += 1
    elif position_1[0] < position_2[0]:
        if position_1[1] > position_2[1]:
            for add in range(total_movement):
                position_to_mark = (initial_x + add, initial_y - add)
                board[position_to_mark] += 1
        elif position_1[1] < position_2[1]:
            for add in range(total_movement):
                position_to_mark = (initial_x + add, initial_y + add)
                board[position_to_mark] += 1

print(board)

values = board.values()
filtered_values = list(filter(lambda f: f >= 1, values))

print(filtered_values)
