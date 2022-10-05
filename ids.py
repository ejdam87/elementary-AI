from typing import List

class Graph:

    def __init__(self, size: int) -> None:
        
        self.size = size
        self.vertices = [i for i in range(size)]
        self.succ = [[] for _ in range(size)]


def example_tree() -> Graph:

    g = Graph(12)
    g.succ[0] = [1, 6, 7]
    g.succ[1] = [2, 5]
    g.succ[2] = [3, 4]
    g.succ[3] = []
    g.succ[4] = []
    g.succ[5] = []
    g.succ[6] = []
    g.succ[7] = [8, 11]
    g.succ[8] = [9, 10]
    g.succ[9] = []
    g.succ[10] = []
    g.succ[11] = []

    return g

def draw_graph(g: Graph, file: str) -> None:

    with open(f"{file}.dot", "w") as f:
        f.write("digraph MyGraph {\n")

        for i, succ in enumerate(g.succ):
            for j in succ:
                f.write(f"{i} -> {j}\n")

        f.write("}\n")


WHITE = 1
GRAY  = 2
BLACK = 3

def dfs_limit(graph: Graph,
              current: int,
              limit: int,
              visited: List[int],
              order: List[int]) -> None:
    
    visited[current] = GRAY
    order.append(current)
    if limit == 0:
        return

    for succ in graph.succ[current]:
        if visited[succ] == WHITE:
            dfs_limit(graph, succ, limit - 1, visited, order)

    visited[current] = BLACK


def ids(graph: Graph) -> List[int]:

    order = []
    limit = 0

    visited = [WHITE for _ in range(graph.size)]

    while WHITE in visited:

        visited = [WHITE for _ in range(graph.size)]
        dfs_limit(graph, 0, limit, visited, order)
        limit += 1
    
    return order    # Order in which vertices were traversed
