import gain
import pandas as pd
from typing import List

GOAL = "Tenis"
CHART = pd.read_excel( "tenis.xlsx" )


class Node:
    def __init__( self, is_leaf: bool=False, val: str="" ) -> None:
        self.is_leaf = is_leaf
        self.val = val
        self.children: List[ "Node" ] = []

    def draw( self, indent: int=0 ) -> str:
        print( indent * " ", end="" )
        print( self.val )
        for child in self.children:
            child.draw( indent + 2 )


def best_attr( data: pd.DataFrame ) -> str:
    gains = [ ( gain.gain( data, attr, GOAL ), attr ) for attr in data if attr != GOAL ]
    return max( gains )[ 1 ]


def split_by( data: pd.DataFrame, attr: str ) -> List[ pd.DataFrame ]:
    
    vals = gain.get_distr( data, attr )
    return [ data.loc[ data[ attr ] == val ] for val in vals ]


def decision_tree( data: pd.DataFrame ) -> Node:

    classes = data[ GOAL ].unique()
    if len( classes ) == 1:
        return Node( is_leaf=True, val=classes[ 0 ] )

    attr = best_attr( data )
    new = Node( val=attr + "?" )
    for partition in split_by( data, attr ):
        new.children.append( decision_tree( partition ) )

    return new
