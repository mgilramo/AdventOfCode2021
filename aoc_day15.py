import aoc_utils
import heapq
import time

DOWNLOAD_INPUT = False
RUN_PUZZLE_1 = False
RUN_PUZZLE_2 = True


class Node:
    def __init__(self, x, y, risk):
        self.pos = (x, y)
        self.risk = risk
        self.tentative_risk = 99999999999999999999999999
        self.visited = False
        self.neighbors = []

    def __str__(self):
        return f'{self.pos} / {self.risk} / {self.tentative_risk} / {self.visited}'

    def __lt__(self, other):
        return self.tentative_risk < other.tentative_risk


def puzzle1():
    # Definition of parameters
    node_list = []
    with open('input_files\\day15_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        max_pos = (len(lines[0]) - 1, len(lines) - 1)

        for y in range(len(lines)):
            for x in range(len(lines)):
                new_node = Node(x, y, int(lines[y][x]))

                # Upper Node?
                up = (x, y - 1)
                if 0 <= up[0] <= max_pos[0] and 0 <= up[1] <= max_pos[1]:
                    new_node.neighbors.append(up)

                # Lower node
                down = (x, y + 1)
                if 0 <= down[0] <= max_pos[0] and 0 <= down[1] <= max_pos[1]:
                    new_node.neighbors.append(down)

                # Left node
                left = (x - 1, y)
                if 0 <= left[0] <= max_pos[0] and 0 <= left[1] <= max_pos[1]:
                    new_node.neighbors.append(left)

                # Right node
                right = (x + 1, y)
                if 0 <= right[0] <= max_pos[0] and 0 <= right[1] <= max_pos[1]:
                    new_node.neighbors.append(right)

                node_list.append(new_node)

    # Algorithm start
    node_list[0].tentative_risk = 0
    current_node = node_list[0]
    while True:
        # Looking for unvisited neighbors
        unvisited_neighbors = list(filter(lambda n: n.pos in current_node.neighbors and not n.visited, node_list))

        # Looping through unvisited neighbors
        for unvisited_neighbor in unvisited_neighbors:
            new_tentative = current_node.tentative_risk + unvisited_neighbor.risk

            if new_tentative < unvisited_neighbor.tentative_risk:
                unvisited_neighbor.tentative_risk = new_tentative

        # Marking current node as visited
        current_node.visited = True

        # Selecting the new current_node
        unvisited_nodes = list(filter(lambda n: not n.visited, node_list))
        if not len(unvisited_nodes):
            for node in node_list:
                print(node)
            print('Not more unvisited nodes available')
            break

        # Showing some statistics
        print(f'Unvisited number of nodes: {len(unvisited_nodes)}')

        current_node = unvisited_nodes[0]
        for unvisited_node in unvisited_nodes:
            if unvisited_node.tentative_risk < current_node.tentative_risk:
                current_node = unvisited_node

        # Checking whether the new current_node is the last_node
        if current_node.pos == max_pos:
            return current_node.tentative_risk


def puzzle2():
    # Definition of parameters
    node_list = []
    with open('input_files\\day15_input.txt', 'r') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

        max_pos = ((len(lines[0]) * 5) - 1, (len(lines) * 5) - 1)

        print(f'Max pos: {max_pos}')

        for y in range(len(lines)):
            for x in range(len(lines[0])):
                new_node = Node(x, y, int(lines[y][x]))

                # Upper Node?
                up = (x, y - 1)
                if 0 <= up[0] <= max_pos[0] and 0 <= up[1] <= max_pos[1]:
                    new_node.neighbors.append(up)

                # Lower node
                down = (x, y + 1)
                if 0 <= down[0] <= max_pos[0] and 0 <= down[1] <= max_pos[1]:
                    new_node.neighbors.append(down)

                # Left node
                left = (x - 1, y)
                if 0 <= left[0] <= max_pos[0] and 0 <= left[1] <= max_pos[1]:
                    new_node.neighbors.append(left)

                # Right node
                right = (x + 1, y)
                if 0 <= right[0] <= max_pos[0] and 0 <= right[1] <= max_pos[1]:
                    new_node.neighbors.append(right)

                node_list.append(new_node)

    print('Initial table completed')

    # First line
    nodes_to_append = []
    for node in node_list:
        for col in range(1, 5):
            new_x = node.pos[0] + (len(lines[0]) * col)
            new_y = node.pos[1]
            new_risk = node.risk + col
            while new_risk > 9:
                new_risk -= 9
            new_node = Node(new_x, new_y, new_risk)

            # Upper Node?
            up = (new_x, new_y - 1)
            if 0 <= up[0] <= max_pos[0] and 0 <= up[1] <= max_pos[1]:
                new_node.neighbors.append(up)

            # Lower node
            down = (new_x, new_y + 1)
            if 0 <= down[0] <= max_pos[0] and 0 <= down[1] <= max_pos[1]:
                new_node.neighbors.append(down)

            # Left node
            left = (new_x - 1, new_y)
            if 0 <= left[0] <= max_pos[0] and 0 <= left[1] <= max_pos[1]:
                new_node.neighbors.append(left)

            # Right node
            right = (new_x + 1, new_y)
            if 0 <= right[0] <= max_pos[0] and 0 <= right[1] <= max_pos[1]:
                new_node.neighbors.append(right)

            nodes_to_append.append(new_node)

    node_list.extend(nodes_to_append)

    # Rest of lines
    nodes_to_append = []
    for node in node_list:
        for line in range(1, 5):
            new_x = node.pos[0]
            new_y = node.pos[1] + (len(lines) * line)
            new_risk = node.risk + line
            while new_risk > 9:
                new_risk -= 9
            new_node = Node(new_x, new_y, new_risk)

            # Upper Node?
            up = (new_x, new_y - 1)
            if 0 <= up[0] <= max_pos[0] and 0 <= up[1] <= max_pos[1]:
                new_node.neighbors.append(up)

            # Lower node
            down = (new_x, new_y + 1)
            if 0 <= down[0] <= max_pos[0] and 0 <= down[1] <= max_pos[1]:
                new_node.neighbors.append(down)

            # Left node
            left = (new_x - 1, new_y)
            if 0 <= left[0] <= max_pos[0] and 0 <= left[1] <= max_pos[1]:
                new_node.neighbors.append(left)

            # Right node
            right = (new_x + 1, new_y)
            if 0 <= right[0] <= max_pos[0] and 0 <= right[1] <= max_pos[1]:
                new_node.neighbors.append(right)

            nodes_to_append.append(new_node)

    node_list.extend(nodes_to_append)

    # Algorithm start
    print('Algorithm Starts')
    node_list[0].tentative_risk = 0

    # List of unvisited nodes
    unvisited_nodes = list(node_list)
    current_node = unvisited_nodes[0]

    # heapq.heapify(unvisited_nodes)
    # current_node = heapq.heappop(unvisited_nodes)

    start_time = time.time()
    while True:
        # List of unvisited neighbors
        unvisited_neighbors = list(filter(lambda n: n.pos in current_node.neighbors and not n.visited, unvisited_nodes))

        # Looping through unvisited neighbors
        for unvisited_neighbor in unvisited_neighbors:
            new_tentative = current_node.tentative_risk + unvisited_neighbor.risk

            if new_tentative < unvisited_neighbor.tentative_risk:
                unvisited_neighbor.tentative_risk = new_tentative

        # Marking current node as visited
        current_node.visited = True

        # Selecting the new current_node
        n_unvisited_nodes = len(unvisited_nodes)
        if not len(unvisited_nodes):
            for node in node_list:
                print(node)
            print('Not more unvisited nodes available')
            break

        # Showing some statistics
        if not n_unvisited_nodes % 500:
            print(f'{n_unvisited_nodes = }')
            print(f'{current_node.tentative_risk = }')
            end_time = time.time()
            elapsed_time = end_time - start_time

            print(f'{elapsed_time = }')

            start_time = time.time()

        # current_node = heapq.heappop(unvisited_nodes)

        current_node = unvisited_nodes[0]
        for unvisited_node in unvisited_nodes:
            if unvisited_node.tentative_risk < current_node.tentative_risk:
                current_node = unvisited_node

        unvisited_nodes.remove(current_node)

        # Checking whether the new current_node is the last_node
        if current_node.pos == max_pos:
            return current_node.tentative_risk


if __name__ == '__main__':
    if DOWNLOAD_INPUT:
        aoc_utils.download_input(15)

    if RUN_PUZZLE_1:
        puzzle1_result = puzzle1()
        print(f'The result of the Puzzle 1 is: {puzzle1_result}')

    if RUN_PUZZLE_2:
        puzzle2_result = puzzle2()
        print(f'The result of the Puzzle 2 is: {puzzle2_result}')
