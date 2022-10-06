from typing import List, Tuple, Any

Weight_tuple = Tuple[int, int]    # adj, cost


class Graph:

    def __init__(self, size: int) -> None:
        
        self.size = size
        self.vertices = [i for i in range(size)]
        self.desc = {i: str(i) for i in self.vertices}
        self.succ: List[ List[Any] ] = []

    def add_node_description(self, desc: List[str]) -> None:
        assert len(desc) == self.size, "Invalid description item count"
        self.desc = { i: desc[i] for i in range(self.size) }


class DiGraph(Graph):
     def __init__(self, size: int) -> None:
        super().__init__(size)
        self.succ: List[ List[int] ] = [ [] for _ in range(size) ]


class WGraph(Graph):

    def __init__(self, size: int) -> None:
        super().__init__(size)
        self.succ: List[ List[Weight_tuple] ] = [ [] for _ in range(size) ]


def draw_directed(g: DiGraph, file: str) -> None:

    with open(f"{file}.dot", "w") as f:
        f.write("digraph MyGraph {\n")

        for i, succ in enumerate(g.succ):
            for j in succ:
                f.write(f"{g.desc[i]} -> {g.desc[j]}\n")

        f.write("}\n")


def draw_weighted(g: WGraph, file: str) -> None:

    with open(f"{file}.dot", "w") as f:
        f.write("digraph MyGraph {\n")

        for i, succ in enumerate(g.succ):
            for j, w in succ:
                f.write(f'{g.desc[i]} -> {g.desc[j]} [label="{w}"]\n')

        f.write("}\n")

def draw_graph(g: Graph, file: str) -> None:

    if type(g) == DiGraph:
        draw_directed(g, file)
    elif type(g) == WGraph:
        draw_weighted(g, file)
    else:
        assert False


def example_tree() -> DiGraph:
    """
    Binary tree
    """
    g = DiGraph(12)
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


def example_directed() -> DiGraph:
    """
    Directed graph
    """
    g = DiGraph(12)
    g.succ[0] = [1, 6, 7]
    g.succ[1] = [2, 5]
    g.succ[2] = [3, 4]
    g.succ[3] = [4, 5]
    g.succ[4] = [8, 11, 9, 5]
    g.succ[5] = [11, 6, 8]
    g.succ[6] = [3, 5, 1]
    g.succ[7] = [8, 11]
    g.succ[8] = [9, 10]
    g.succ[9] = [0, 7]
    g.succ[10] = [2]
    g.succ[11] = [2]

    return g


def example_weighted() -> WGraph:
    """
    Weighted graph
    """
    g = WGraph(12)
    g.succ[0] = [(1, 2), (6, 3), (7, 2)]
    g.succ[1] = [(2, 5), (5, -3)]
    g.succ[2] = [(3, 1), (4, 18)]
    g.succ[3] = [(4, 0), (5, -2)]
    g.succ[4] = [(8, 8), (11, 9), (5, 7)]
    g.succ[5] = [(11, 20), (6, 10), (8, 5)]
    g.succ[6] = [(3, 5), (5, 6), (1, 7)]
    g.succ[7] = [(8, 2), (11, -7)]
    g.succ[8] = [(9, 8), (10, -3)]
    g.succ[9] = [(0, 12), (7, 30)]
    g.succ[10] = [(2, 13)]
    g.succ[11] = [(2, 15)]

    return g


draw_graph(example_weighted(), "draw")
