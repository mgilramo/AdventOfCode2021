import aoc_utils
from collections import Counter
from math import ceil

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


def puzzle1():
    with open('input_files\\day14_input.txt', 'r') as f:
        # Creation of the initial variables reading the file
        polymer = f.readline().strip()
        empty_line = f.readline()
        insertion_rules_list = f.readlines()
        insertion_rules_list = list(map(lambda l: l.strip(), insertion_rules_list))

        # Creation of the master dictionary with the rules
        insertion_rules_d = {}
        for insertion_rule in insertion_rules_list:
            insertion_rule = insertion_rule.split(' -> ')
            insertion_rules_d[insertion_rule[0]] = insertion_rule[1]

    # Loop through steps
    steps = 10
    for x in range(steps):
        modified_polymer = polymer[0]
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            new_char = insertion_rules_d[pair]
            modified_polymer += new_char + polymer[i+1]
        polymer = modified_polymer

    c = Counter(polymer)
    mc_letter, mc_val = c.most_common()[0]
    lc_letter, lc_val = c.most_common()[-1]

    return mc_val - lc_val


def puzzle2():
    with open('input_files\\day14_input.txt', 'r') as f:
        # Creation of the initial variables reading the file
        polymer = f.readline().strip()
        empty_line = f.readline()
        insertion_rules_list = f.readlines()
        insertion_rules_list = list(map(lambda l: l.strip(), insertion_rules_list))

        polymer_count = {}

        for i in range(len(polymer)-1):
            polymer_count[polymer[i:i+2]] = 1

        # Creation of the master dictionary with the rules
        insertion_rules_d = {}
        for insertion_rule in insertion_rules_list:
            insertion_rule = insertion_rule.split(' -> ')
            insertion_rules_d[insertion_rule[0]] = insertion_rule[1]

    print(polymer_count)

    if 'NN' in polymer_count:
        print('OK')
    else:
        print('NOK')

    # Loop through steps
    steps = 40
    for x in range(steps):
        new_polymer_count = {}
        for pair_str in polymer_count:
            # New Letter
            new_letter = insertion_rules_d[pair_str]

            # New Pair 1
            new_pair_1 = pair_str[0] + new_letter
            if new_pair_1 in new_polymer_count:
                new_polymer_count[new_pair_1] += polymer_count[pair_str]
            else:
                new_polymer_count[new_pair_1] = polymer_count[pair_str]

            # New Pair 2
            new_pair_2 = new_letter + pair_str[1]
            if new_pair_2 in new_polymer_count:
                new_polymer_count[new_pair_2] += polymer_count[pair_str]
            else:
                new_polymer_count[new_pair_2] = polymer_count[pair_str]

        polymer_count = new_polymer_count

    print(polymer_count)

    # Count after final step
    count_d = {}
    for pair_str in polymer_count:
        letter_1 = pair_str[0]
        if letter_1 in count_d:
            count_d[letter_1] += polymer_count[pair_str]
        else:
            count_d[letter_1] = polymer_count[pair_str]

        letter_2 = pair_str[1]
        if letter_2 in count_d:
            count_d[letter_2] += polymer_count[pair_str]
        else:
            count_d[letter_2] = polymer_count[pair_str]

    print(count_d)

    # Each letter should be the half
    for letter in count_d:
        count_d[letter] = ceil(count_d[letter]/2)

    print(count_d)

    letter_count = list(count_d.values())

    return max(letter_count) - min(letter_count)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(14)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
