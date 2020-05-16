"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

from random import randint
from my_solution import connect_stars
from math import hypot


def random_vertices(v):
    while True:
        coords = set()
        while len(coords) < v:
            coords.add((randint(0, 999), randint(0, 999)))
        coords = list(coords)
        combin = [(a, b) for a in range(v) for b in range(a + 1, v)]
        edges = [hypot(*(a - b for a, b in zip(coords[c1], coords[c2]))) for c1, c2 in combin]
        if len(edges) == len(set(edges)):
            return coords


def make_random_tests(*nums):
    random_tests = []
    for n in nums:
        inp = random_vertices(n)
        random_tests.append({
            'input': inp,
            'answer': connect_stars(inp),
        })
    return random_tests


TESTS = {
    "Basics": [
        {
            "input": [(1, 1), (4, 4)],
            "answer": [[0, 1]],
        },
        {
            "input": [(1, 1), (4, 1), (4, 4)],
            "answer": [[0, 1], [1, 2]],
        },
        {
            "input": [(6, 6), (6, 8), (8, 4), (3, 2)],
            "answer": [[0, 1], [0, 2], [0, 3]],
        },
        {
            "input": [(5, 4), (5, 1), (2, 6), (7, 2), (6, 9)],
            "answer": [[0, 2], [0, 3], [1, 3], [2, 4]],
        },
        {
            "input": [(5, 8), (5, 1), (4, 2), (7, 6), (8, 6), (2, 2)],
            "answer": [[0, 3], [1, 2], [2, 3], [2, 5], [3, 4]],
        },
        {
            "input": [(2, 7), (9, 9), (4, 9), (9, 6), (3, 3), (1, 6), (9, 7)],
            "answer": [[0, 2], [0, 5], [1, 2], [1, 6], [3, 6], [4, 5]],
        },
    ],
    "Constellations": [
        {
            "input": [(122, 250), (23, 94), (93, 125), (155, 190), (232, 243), (258, 319), (278, 340), (212, 128),
                      (276, 50)],
            "answer": [[0, 3], [1, 2], [2, 3], [3, 4], [3, 7], [4, 5], [5, 6], [7, 8]],
            "explanation": 'cygnus'
        },
        {
            "input": [(18, 129), (33, 100), (56, 99), (70, 70), (96, 88)],
            "answer": [[0, 1], [1, 2], [2, 3], [3, 4]],
            "explanation": 'cassiopeia'
        },
        {
            "input": [(56, 162), (107, 155), (80, 100), (89, 108), (95, 113), (70, 50), (123, 59)],
            "answer": [[0, 1], [1, 4], [2, 3], [2, 5], [3, 4], [5, 6]],
            "explanation": 'orion'
        },
        {
            "input": [(73, 49), (68, 50), (57, 37), (52, 28), (69, 10), (100, 11), (120, 18), (122, 47), (125, 72),
                      (145, 112), (155, 124), (168, 128), (195, 165), (202, 146), (201, 122)],
            "answer": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],
                       [11, 14], [12, 13], [13, 14]],
            "explanation": 'scorpius'
        },
        {
            "input": [(118, 210), (100, 181), (88, 142), (99, 101), (80, 87), (105, 50), (123, 69)],
            "answer": [[0, 1], [1, 2], [2, 3], [3, 4], [3, 6], [5, 6]],
            "explanation": 'ursa_minor'
        },
        {
            "input": [(15, 159), (55, 172), (95, 193), (175, 156), (191, 166), (231, 227), (252, 223), (268, 238), (274, 235), (285, 229), (311, 251), (303, 279), (329, 291), (350, 302), (358, 301), (361, 290), (367, 289), (368, 298), (359, 301)],
            "answer": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 18], [15, 16], [16, 17], [17, 18]],
            "explanation": 'hydra',
        },
        {
            "input": [(86, 189), (77, 177), (82, 163), (84, 146), (60, 119), (40, 91), (18, 60), (29, 61), (44, 71), (58, 72), (78, 82), (91, 82), (108, 78), (166, 74), (191, 71), (205, 75), (220, 62), (235, 63), (205, 50), (190, 54)],
            "answer": [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 8], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [14, 19], [16, 17], [16, 18], [18, 19]],
            "explanation": 'pisces',
        },
    ],
    'Randoms': make_random_tests(10, 15, 20, 30, 40, 50),
}
