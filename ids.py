
class Graph:

    def __init__(self, size: int) -> None:
        
        self.size = size
        self.vertices = [i for i in range(size)]
        self.succ = []


def example() -> Graph:
    pass    # TODO: Example graph

def dfs_limit(graph: Graph, current: int, limit: int) -> None:
    pass    # TODO: dfs with limit depth

def ids(Graph: Graph) -> None:
    pass    # TODO: iterative-deepening search
