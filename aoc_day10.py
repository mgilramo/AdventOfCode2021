import aoc_utils

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


class ChunkChar:
    d_open_char = {')': '(',
                   ']': '[',
                   '}': '{',
                   '>': '<'}

    d_close_char = {'(': ')',
                    '[': ']',
                    '{': '}',
                    '<': '>'}

    def __init__(self, open_char, position):
        self.open_char = open_char
        self.position = position
        self.opened = True

    def close(self):
        self.opened = False

    def __str__(self):
        return f'Open char: {self.open_char} - Opened: {self.opened} - Position: {self.position}'


def illegal_recognition(line):
    chunk_list = []
    for pos in range(len(line)):
        if line[pos] in '([{<':
            chunk = ChunkChar(line[pos], pos)
            chunk_list.append(chunk)
        elif line[pos] in ')]}>':
            open_chunks = list(filter(lambda c: c.opened, chunk_list))
            open_chunks_sorted = list(sorted(open_chunks, key=lambda s: s.position, reverse=True))
            if open_chunks_sorted[0].open_char != ChunkChar.d_open_char[line[pos]]:
                print(f'Close Char: {line[pos]}')
                print(f'Incorrect Open Chunk: {open_chunks_sorted[0]}')
                incorrect_char = line[pos]
                return 'INCORRECT', incorrect_char
            else:
                open_chunks_sorted[0].close()
    return 'CORRECT', ''


def closing_char(line):
    chunk_list = []
    for pos in range(len(line)):
        if line[pos] in '([{<':
            chunk = ChunkChar(line[pos], pos)
            chunk_list.append(chunk)
        elif line[pos] in ')]}>':
            open_chunks = list(filter(lambda c: c.opened, chunk_list))
            open_chunks_sorted = list(sorted(open_chunks, key=lambda s: s.position, reverse=True))
            open_chunks_sorted[0].close()
    open_chunks = list(filter(lambda c: c.opened, chunk_list))
    open_chunks_sorted_final = list(sorted(open_chunks, key=lambda s: s.position, reverse=True))
    return_list = list(map(lambda r: ChunkChar.d_close_char[r.open_char], open_chunks_sorted_final))
    return return_list


def puzzle1():
    d_illegal_character = {')': 3,
                           ']': 57,
                           '}': 1197,
                           '>': 25137}

    incorrect_closings = []
    with open('input_files\\day10_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        for line in lines:
            print(f'Processing line: {line}')
            result, incorrect_character = illegal_recognition(line)
            print(f'Result of the line: {result} ; Incorrect character: {incorrect_character}')
            if result == 'INCORRECT':
                incorrect_closings.append(incorrect_character)
    result = 0
    for incorrect_closing in incorrect_closings:
        value = d_illegal_character[incorrect_closing]
        result += value

    return result


def puzzle2():
    d_closing_character = {')': 1,
                           ']': 2,
                           '}': 3,
                           '>': 4}
    incomplete_lines = []
    with open('input_files\\day10_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        for line in lines:
            print(f'Processing line: {line}')
            result, incorrect_character = illegal_recognition(line)
            print(f'Result of the line: {result} ; Incorrect character: {incorrect_character}')
            if result == 'CORRECT':
                incomplete_lines.append(line)

    closing_scores = []
    for incomplete_line in incomplete_lines:
        closing_chars = closing_char(incomplete_line)
        score = 0
        for char in closing_chars:
            score *= 5
            score += d_closing_character[char]
        closing_scores.append(score)

    closing_scores = list(sorted(closing_scores))
    middle = (len(closing_scores)/2) - 0.5

    return closing_scores[int(middle)]


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(10)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
