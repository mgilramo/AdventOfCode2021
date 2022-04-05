import aoc_utils
import pdb

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def decoder(item_list):
    d = {}

    one = list(filter(lambda x: len(x) == 2, item_list))[0]
    four = list(filter(lambda x: len(x) == 4, item_list))[0]
    seven = list(filter(lambda x: len(x) == 3, item_list))[0]
    eight = list(filter(lambda x: len(x) == 7, item_list))[0]

    # Groups to check
    five_group = list(filter(lambda x: len(x) == 5, item_list))
    six_group = list(filter(lambda x: len(x) == 6, item_list))

    # Three
    for fg1 in range(len(five_group)):
        to_check = five_group[fg1]
        f_matches = 0
        o_matches = 0
        for l in range(2):
            if one[l] in to_check:
                o_matches += 1
        for m in range(4):
            if four[m] in to_check:
                f_matches += 1
            else:
                not_matching = four[m]
        if f_matches == 3 and o_matches == 2:
            three = to_check
            five_group.remove(to_check)
            break
    # Five and Two
    for fg2 in range(len(five_group)):
        to_check = five_group[fg2]
        if not_matching in to_check:
            five = to_check
            five_group.remove(to_check)
            break
    two = five_group[0]

    # Nine
    for n in range(len(six_group)):
        to_check = six_group[n]
        matches = 0
        for m in range(4):
            if four[m] in to_check:
                matches += 1
        if matches == 4:
            nine = to_check
            six_group.remove(to_check)
            break
    # Six and Zero
    for n in range(len(six_group)):
        to_check = six_group[n]
        matches = 0
        for m in range(5):
            if five[m] in to_check:
                matches += 1
        if matches == 5:
            six = to_check
            six_group.remove(to_check)
            break
    zero = six_group[0]

    d[''.join(sorted(zero))] = '0'
    d[''.join(sorted(one))] = '1'
    d[''.join(sorted(two))] = '2'
    d[''.join(sorted(three))] = '3'
    d[''.join(sorted(four))] = '4'
    d[''.join(sorted(five))] = '5'
    d[''.join(sorted(six))] = '6'
    d[''.join(sorted(seven))] = '7'
    d[''.join(sorted(eight))] = '8'
    d[''.join(sorted(nine))] = '9'

    return d


def puzzle1():
    with open('input_files\\day8_input.txt', 'r') as f:
        full_output_list = []
        while True:
            fd_output_val = f.readline().split('|')
            if len(fd_output_val) < 2:
                break
            fd_output = fd_output_val[1].split(' ')
            fd_output = list(map(lambda x: x.strip(), fd_output))

            full_output_list.extend(fd_output)

    digit_count = 0
    for output_item in full_output_list:
        if len(output_item) in [2, 3, 4, 7]:
            digit_count += 1

    return digit_count


def puzzle2():
    with open('input_files\\day8_input.txt', 'r') as f:
        output_list = []
        decoding_list = []
        while True:
            fd_output_val = f.readline().split('|')
            if len(fd_output_val) < 2:
                break

            d_output = fd_output_val[0].split(' ')
            d_output = list(map(lambda d: d.strip(), d_output))

            d_output_clean = d_output[:10]

            decoding_list.append(d_output_clean)

            fd_output = fd_output_val[1].split(' ')
            fd_output = list(map(lambda fd: fd.strip(), fd_output))

            fd_output_clean = fd_output[1:]

            output_list.append(fd_output_clean)

        digit_list = []
        for x in range(len(decoding_list)):
            digit = ''
            print(f'Decoding: {decoding_list[x]}')
            print(f'Values: {output_list[x]}')
            d_decoder = decoder(decoding_list[x])
            for item in output_list[x]:
                digit_to_append = d_decoder[''.join(sorted(item))]
                digit += digit_to_append
            digit_list.append(digit)
            print(f'Digit: {digit}')

        digit_list = list(map(lambda d: int(d), digit_list))

        return sum(digit_list)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(8)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
