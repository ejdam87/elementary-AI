import random

Vector = list[ float ]

def dot( v1: Vector, v2: Vector ) -> float:

    res = 0
    for a, b in zip( v1, v2 ):
        res += a * b
    return res

def plus( v1: Vector, v2: Vector ) -> Vector:
    res = []
    for a, b in zip( v1, v2 ):
        res.append( a + b )
    return res

def minus( v1: Vector, v2: Vector ) -> Vector:
    res = []
    for a, b in zip( v1, v2 ):
        res.append( a - b )
    return res

def mult( v: Vector, c: int ) -> Vector:
    return [ c * a for a in v ]

def extended( v: Vector ) -> Vector:
    return [ 1 ] + v

class Perceptron:

    def __init__( self, dim: int ) -> None:
        self.dim = dim
        self.weights = [ random.random( ) for _ in range( dim + 1 ) ]

    def set_weights( self, v: Vector ) -> None:
        self.weights = v

    def classify( self, vector: Vector ) -> bool:
        return self.weights[ 0 ] + dot( self.weights[ 1: ], vector ) >= 0


train = [ ( [ -1, 0 ], True ), ( [ 0, 1 ], True ), ( [ 3, 0 ], False ) ]
Sample = tuple[ Vector, bool ]

def learn( p: Perceptron, epochs: int, dataset: list[ Sample ] ) -> None:
    
    n = len( dataset )
    for i in range( epochs ):

        sample, exp = dataset[ i % n ]
        actual = p.classify( sample )

        diff = int( actual ) - int( exp )
        new = minus( p.weights, mult( extended( sample ), diff ) )
        p.weights = new
