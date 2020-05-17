from typing import List, Tuple, Iterable
from numpy import array
from scipy.sparse.csgraph import minimum_spanning_tree as mst
from math import hypot
from itertools import product


def connect_stars(coords: List[Tuple[int, int]]) -> Iterable[List[int, int]]:
    size = len(coords)
    cs = array([hypot(x1 - x2, y1 - y2) for (x1, y1), (x2, y2) in product(coords, coords)]).reshape(size, size)
    return sorted(sorted(map(int, z)) for z in zip(*mst(cs).nonzero()))
