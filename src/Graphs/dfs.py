class Queue:

    def __init__(self, collection=[]):
        self.collection = collection
        self.cursor = 0

    def current(self):
        if self.cursor < len(self.collection):
            return self.collection[self.cursor]

    def next(self):
        if len(self.collection) >= self.cursor + 1:
            self.cursor += 1

    def has_next(self):
        has = len(self.collection) >= self.cursor + 1
        if not has: self.cursor = 0
        return has

    def add(self, item):
        self.collection.append(item)

    def pop(self, item):
        return self.collection.pop(item)


class Visited:

    def __init__(self, collection=set()):
        self.collection = collection

    def has(self, item):
        return item in self.collection

    def add(self, item):
        self.collection.add(item)

    def remove(self, item):
        self.collection.remove(item)


graph = {

    "Кустанайская": [(3, "Ореховый бульвар"), (2, "Шипиловская")],
    "Ореховый бульвар": [(3, "Кустанайская"), (3, "Задонский проезд"), (4, "Ореховый проезд"), (5, "Генерала Белова")],
    "Шипиловская": [(2, "Кустанайская"), (4, "Задонский проезд"), (4, "Ореховый проезд"), (6, "Генерала Белова")],
    "Задонский проезд": [(3, "Ореховый бульвар"), (4, "Шипиловская")],
    "Ореховый проезд": [(4, "Ореховый бульвар"), (4, "Шипиловская")],
    "Генерала Белова":[(5, "Ореховый бульвар"), (6, "Шипиловская")]}

def bfs_shortest(start_node, end_node):
    queue = Queue([(0, start_node, [])])
    visited = Visited()

    while queue.has_next():
        (cost, node, path) = queue.pop(0)
        if not visited.has(node):
            visited.add(node)
            path = path + [node]

            if node == end_node:
                print('->'.join(street for street in path))
                print(cost)

            for c, neighbour in graph[node]:
                if not visited.has(neighbour):
                    queue.add((cost+c, neighbour, path))


def dfs_path(graph, node, final_node):
    global counter, visit
    if node == final_node:
        counter+=1

    visit.add(node)
    for c, neighbor in graph[node]:
        if not visit.has(neighbor):
            dfs_path(graph, neighbor, final_node)

    visit.remove(node)

if __name__ == "__main__":
    # bfs_shortest('Генерала Белова', 'Кустанайская')

    visit = Visited()
    counter = 0
    dfs_path(graph, 'Генерала Белова', 'Кустанайская')
    print(counter)



