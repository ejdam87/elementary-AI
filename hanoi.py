from typing import List, Tuple

Transition_list = List[ Tuple[ str, str ] ]

def hanoi(n: int,
          source: str,
          dest: str,
          spare: str) -> Transition_list:
    
    res = []
    hanoi_rec( n, source, dest, spare, res )
    return res

def hanoi_rec(n: int,
              source: str,
              dest: str,
              spare: str,
              res: Transition_list) -> None:
    
    if n == 1:
        res.append( (source, dest) )
        return

    hanoi_rec( n - 1, source, spare, dest, res )
    res.append( (source, dest) )
    hanoi_rec( n - 1, spare, dest, source, res )
