from aoc_day10 import ChunkChar


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
    print(len(line))
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

test_line = '[({(<(())[]>[[{[]{<()<>>'

print(closing_char(test_line))