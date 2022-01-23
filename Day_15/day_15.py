from distutils import extension
from numpy import full


def challenge_1():
    chitons_graph = Graph(load_chitons())
    print("Chitons loaded. Beginning search.")
    distance = find_shortest_path(
        chitons_graph,
        chitons_graph.chitons_map[0][0],
        chitons_graph.chitons_map[-1][-1]
        )
    print(distance)

class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.neighbors = []
        self.value = value
        self.distance = 10000000
        self.prev = None

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def to_string(self):
        return str(self.row) + " " + str(self.col)

class Graph:
    def __init__(self, chitons_map):
        self.chitons_map = chitons_map
        for row in range(len(chitons_map)):
            for col in range(len(chitons_map[row])):
                chitons_map[row][col] = Node(row, col, chitons_map[row][col])
        self.make_connections()

    def make_connections(self):
        for row in range(len(self.chitons_map)):
            for col in range(len(self.chitons_map[row])):
                for neighbor in self.find_neighbors(row, col):
                    self.chitons_map[row][col].add_neighbor(neighbor)

    def find_neighbors(self, row, col):
        neighbors = []
        if row > 0:
            neighbors.append(self.chitons_map[row - 1][col])
        if row < len(self.chitons_map) - 1:
            neighbors.append(self.chitons_map[row + 1][col])
        if col > 0:
            neighbors.append(self.chitons_map[row][col - 1])
        if col < len(self.chitons_map[0]) - 1:
            neighbors.append(self.chitons_map[row][col + 1])
        return neighbors

    def find_node(self, row, col):
        return self.chitons_map[row][col]

class Heap:
    def __init__(self):
        self.heap = [None]
    
    def add(self, node):
        self.heap.append(node)
        node_index = len(self.heap) - 1
        if node_index == 1:
            return
        while self.heap[node_index].distance < self.heap[node_index // 2].distance:
            self.heap[node_index] = self.heap[node_index // 2]
            self.heap[node_index // 2] = node
            node_index = node_index // 2
            if node_index == 1:
                break
    
    def remove_min(self):
        min = self.heap[1]
        self.heap[1] = self.heap[-1]
        popped = self.heap.pop()
        popped_index = 1

        if popped_index * 2 > len(self.heap) - 1:
            return min
        if popped_index * 2 == len(self.heap) - 1:
            if self.heap[popped_index].distance > self.heap[popped_index * 2].distance:
                self.heap[popped_index] = self.heap[popped_index * 2]
                self.heap[popped_index * 2] = popped
                return min

        while (
            popped.distance > self.heap[popped_index * 2].distance
            or popped.distance > self.heap[popped_index * 2 + 1].distance
            ):
            if self.heap[popped_index * 2].distance < self.heap[popped_index * 2 + 1].distance:
                self.heap[popped_index] = self.heap[popped_index * 2]
                self.heap[popped_index * 2] = popped
                popped_index = popped_index * 2
            else:
                self.heap[popped_index] = self.heap[popped_index * 2 + 1]
                self.heap[popped_index * 2 + 1] = popped
                popped_index = popped_index * 2 + 1

            if popped_index * 2 > len(self.heap) - 1:
                return min
            if popped_index * 2 == len(self.heap) - 1:
                if self.heap[popped_index].distance > self.heap[popped_index * 2].distance:
                    self.heap[popped_index] = self.heap[popped_index * 2]
                    self.heap[popped_index * 2] = popped
                return min

        return min

    def update_node(self, node, new_value):
        node_index = self.heap.index(node)
        node.distance = new_value

        while new_value < self.heap[node_index // 2].distance:
            self.heap[node_index] = self.heap[node_index // 2]
            self.heap[node_index // 2] = node
            node_index = node_index // 2
            if node_index == 1:
                break

        if node_index * 2 > len(self.heap) - 1:
            return
        if node_index * 2 == len(self.heap) - 1:
            if self.heap[node_index].distance > self.heap[node_index * 2].distance:
                self.heap[node_index] = self.heap[node_index * 2]
                self.heap[node_index * 2] = node
            return

        while (
            new_value > self.heap[node_index * 2].distance
            or new_value > self.heap[node_index * 2 + 1].distance
            ):
            if self.heap[node_index * 2].distance < self.heap[node_index * 2 + 1].distance:
                self.heap[node_index] = self.heap[node_index * 2]
                self.heap[node_index * 2] = node
                node_index = node_index * 2
            else:
                self.heap[node_index] = self.heap[node_index * 2 + 1]
                self.heap[node_index * 2 + 1] = node
                node_index = node_index * 2 + 1

            if node_index * 2 > len(self.heap) - 1:
                break
            if node_index * 2 == len(self.heap) - 1:
                if self.heap[node_index].distance > self.heap[node_index * 2].distance:
                    self.heap[node_index] = self.heap[node_index * 2]
                    self.heap[node_index * 2] = node
                break

    def display(self, index=1, padding=""):
        if index > len(self.heap) - 1:
            return
        self.display(index * 2 + 1, padding + "    ")
        print(padding + str(self.heap[index].row), self.heap[index].col)
        self.display(index * 2, padding + "    ")

def find_shortest_path(chitons_graph, start, target):
    heap = Heap()
    start.distance = 0
    for row in chitons_graph.chitons_map:
        for col in row:
            heap.add(col)

    while True:
        min = heap.heap[1]
        for neighbor in min.neighbors:
            if neighbor == target:
                return min.distance + neighbor.value
            if neighbor in heap.heap:
                if neighbor.distance > min.distance + neighbor.value:
                    heap.update_node(neighbor, min.distance + neighbor.value)
        heap.remove_min()

def load_chitons():
    chitons_map = []
    with open("Day_15/input.txt", "r+") as input:
        for line in input.readlines():
            chitons_map.append(list(map(lambda x: int(x), line.strip())))

    return chitons_map

def challenge_2():
    chitons_graph = Graph(find_full_map(load_chitons()))
    print("Chitons loaded. Beginning search.")
    distance = find_shortest_path(
        chitons_graph,
        chitons_graph.chitons_map[0][0],
        chitons_graph.chitons_map[-1][-1]
        )
    print(distance)

def find_full_map(chitons_map):
    extension_maps = []
    for row in range(5):
        new_row = []
        for col in range(5):
            new_row.append(get_extension_map(chitons_map, row + col))
        extension_maps.append(new_row)

    full_map = []

    for row in extension_maps:
        for sub_row in range(len(row[1])):
            new_row = []
            for extension_map in row:
                for col in extension_map[sub_row]:
                    new_row.append(col)
            full_map.append(new_row)
    return full_map

def get_extension_map(chitons_map, extension):
    extension_map = []
    for row in chitons_map:
        new_row = []
        for col in row:
            new_value = col + extension
            if new_value > 9:
                new_value -= 9
            new_row.append(new_value)
        extension_map.append(new_row)
    return extension_map

if __name__ == "__main__":
    challenge_1()
    challenge_2()
