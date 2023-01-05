import edge   as e
import vertex as v

from typing import Iterator

class Graph:

    def __init__( self, size: int ) -> None:
        self.size = size
        self.vertices: list[ v.Vertex ] = [ v.Vertex( i ) for i in range(size) ]
        self.edges: list[ e.Edge ]      = []

    def get_verices( self ) -> list[ v.Vertex ]:
        return self.vertices

    def get_vertex_by_desc( self, desc: str ) -> v.Vertex:
        for vertex in self.vertices:
            if vertex.desc == desc:
                return vertex

        raise ValueError()

    def get_vertex_by_id( self, _id: int ) -> v.Vertex:
        return self.vertices[ _id ]

    def add_edge( self, v1: v.Vertex, v2: v.Vertex ) -> e.Edge:
        new = e.Edge( v1, v2 )
        self.edges.append( new )
        return new

    def get_successors( self, v: v.Vertex ) -> Iterator[ v.Vertex ]:
        """
        Un-weighted
        Un-directed
        """
        for edge in self.edges:
            v1, v2 = edge.get_verices()
            if v == v1:
                yield v2
            if v == v2:
                yield v1


class DGraph( Graph ):
    def get_successors( self, v: v.Vertex ) -> Iterator[ v.Vertex ]:
        """
        Un-weighted
        Directed
        """
        for edge in self.edges:
            v1, v2 = edge.get_verices()
            if v == v1:
                yield v2

class WGraph( Graph ):
    def get_weight( self, edge: e.Edge ) -> float:
        pass

class WDGraph( WGraph ):
    def get_successors( self, v: v.Vertex ) -> Iterator[ v.Vertex ]:
        """
        Weighted
        Directed
        """
        for edge in self.edges:
            v1, v2 = edge.get_verices()
            if v == v1:
                yield v2


def draw_directed(g: DGraph, file: str) -> None:

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
