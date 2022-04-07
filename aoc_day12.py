import aoc_utils
from collections import Counter

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = True
RUN_PUZZLE_2 = True


class Node:
    def __init__(self, name):
        self.name = name
        if str.isupper(self.name):
            self.type = 'b'
        else:
            self.type = 's'
        self.adj_nodes = []
        self.times_visited = 0

    def add_adj_node(self, new_adj_node):
        if new_adj_node not in self.adj_nodes and new_adj_node != 'start':
            self.adj_nodes.append(new_adj_node)

    def create_a_copy(self):
        copied_node = Node(self.name)
        for copied_adj_node in self.adj_nodes:
            copied_node.adj_nodes.append(copied_adj_node)
        copied_node.times_visited = self.times_visited
        return copied_node

    def __str__(self):
        return f'Node: {self.name} ; Adj Nodes: {self.adj_nodes}'


class Path:
    SMALL_REVISIT = 2

    def __init__(self):
        self.available_nodes = []
        self.path_nodes = []
        self.completed = False
        self.incompleted = False
        self.small_revisit = Path.SMALL_REVISIT
        self.small_revisit_initial = Path.SMALL_REVISIT

    def create_a_copy(self):
        copied_path = Path()
        for available_node in self.available_nodes:
            copied_path.available_nodes.append(available_node.create_a_copy())
        for path_node in self.path_nodes:
            copied_path.path_nodes.append(path_node.create_a_copy())
        copied_path.completed = self.completed
        copied_path.incompleted - self.incompleted
        copied_path.small_revisit = self.small_revisit
        copied_path.small_revisit_initial = self.small_revisit_initial
        return copied_path

    def path_str(self):
        path_str = ''
        for node_str in self.path_nodes:
            path_str += node_str.name + ' -> '
        return f'({path_str[:len(path_str)-4]})'

    def available_str(self):
        available_str = ''
        for node_str in self.available_nodes:
            available_str += node_str.name + f'({node_str.times_visited})' + ', '
        return f'({available_str[:len(available_str)-2]})'


def process_paths(file, revisit_number):
    Path.SMALL_REVISIT = revisit_number

    master_node_list = []
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        for line in lines:
            line = line.split('-')
            for node_name in line:
                fl_nn = list(filter(lambda nn: nn.name == node_name, master_node_list))
                if not len(fl_nn):
                    new_node = Node(node_name)
                    master_node_list.append(new_node)
            node0 = list(filter(lambda nn: nn.name == line[0], master_node_list))[0]
            node1 = list(filter(lambda nn: nn.name == line[1], master_node_list))[0]

            node0.add_adj_node(line[1])
            node1.add_adj_node(line[0])

    start_node = list(filter(lambda nn: nn.name == 'start', master_node_list))[0]
    path_list = []

    for adj_node_name in start_node.adj_nodes:
        new_node_list = []
        for node in master_node_list:
            if node.name != 'start':
                new_node_list.append(node.create_a_copy())
            else:
                new_start_node = node.create_a_copy()

        adj_node = list(filter(lambda nn: nn.name == adj_node_name, new_node_list))[0]
        adj_node.times_visited += 1

        new_path = Path()
        new_path.path_nodes.append(new_start_node)
        new_path.path_nodes.append(adj_node)
        new_path.available_nodes.extend(new_node_list)
        path_list.append(new_path)

    completed_paths = []

    while True:
        for path in path_list:
            last_node = path.path_nodes[-1]
            if last_node.name == 'end':
                path.completed = True
                completed_paths.append(path)
            else:
                last_node_adj = []
                last_node_adj_names = last_node.adj_nodes
                for available_node in path.available_nodes:
                    if available_node.name in last_node_adj_names:
                        if available_node.type == 'b' or (available_node.type == 's'
                                                          and available_node.times_visited < path.small_revisit):
                            last_node_adj.append(available_node)
                if not len(last_node_adj):
                    path.incompleted = True

        path_list = list(filter(lambda p: not p.completed and not p.incompleted, path_list))

        if not len(path_list):
            break

        paths_to_append = []
        for path in path_list:
            last_node = path.path_nodes[-1]
            last_node_adj = []
            last_node_adj_names = last_node.adj_nodes
            for available_node in path.available_nodes:
                if available_node.name in last_node_adj_names:
                    if available_node.type == 'b' or (available_node.type == 's'
                                                      and available_node.times_visited < path.small_revisit):
                        last_node_adj.append(available_node)
                        # available_node.times_visited += 1

            if len(last_node_adj) > 1:
                for x in range(1, len(last_node_adj)):
                    new_path = path.create_a_copy()
                    for available_node in new_path.available_nodes:
                        if available_node.name == last_node_adj[x].name:
                            new_path.path_nodes.append(available_node)
                            available_node.times_visited += 1
                            if available_node.type == 's' and \
                                    available_node.times_visited == new_path.small_revisit_initial:
                                new_path.small_revisit = 1
                    paths_to_append.append(new_path)

            path.path_nodes.append(last_node_adj[0])
            last_node_adj[0].times_visited += 1
            if last_node_adj[0].type == 's' and last_node_adj[0].times_visited == path.small_revisit_initial:
                path.small_revisit = 1

        path_list.extend(paths_to_append)

    valid_paths = []
    for path in completed_paths:
        small_nodes = list(filter(lambda n: n.type == 's', path.path_nodes))
        small_nodes_names = list(map(lambda n: n.name, small_nodes))
        c = Counter(small_nodes_names)

        duplicate = list(filter(lambda d: d == 2, c.values()))

        if len(duplicate) < 2:
            valid_paths.append(path)

    return len(valid_paths)


def puzzle1():
    return process_paths('input_files\\day12_input.txt', 1)


def puzzle2():
    return process_paths('input_files\\day12_input.txt', 2)


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(12)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
