from math import log2
from typing import List, Dict
import pandas as pd
from collections import defaultdict

def get_entropy( probs: List[ float ] ) -> int:
    res = 0
    for p in probs:
        res += -p * log2( p )

    return res

def get_distr( data: pd.DataFrame, attr: str ) -> Dict[ str, int ]:
    vals = defaultdict( int )
    for res in data[ attr ]:
        vals[ res ] += 1

    return vals


def get_partial_distr(  data: pd.DataFrame, attr: str, val: str, goal: str) -> Dict[ str, int ]:
    vals = defaultdict( int )
    partial = data.loc[ data[ attr ] == val ]
    return get_distr( partial, goal )


def get_probs( distr: Dict[ str, int ] ) -> List[ float ]:
    total = sum( distr.values() )
    return [ p / total for p in distr.values() ]


def entropy( data: pd.DataFrame, goal: str ) -> int:
    distr = get_distr( data, goal )
    return get_entropy( get_probs( distr ) )


def gain( data: pd.DataFrame, attr: str, goal: str ) -> int:
    
    res = entropy( data, goal )
    distr = get_distr( data, attr )
    total = sum( distr.values() )

    for val, count in distr.items():
        partial_distr = get_partial_distr( data, attr, val, goal )
        res -= ( count / total ) * get_entropy( get_probs( partial_distr ) )

    return res
