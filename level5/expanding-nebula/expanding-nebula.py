import math
import itertools

def solution(g):
    rows = len(g)
    cols = len(g[0])
    final_rows = []
    possible_rows = generate_possible_rows(cols)
    # access with possible_rows[0][0] - row - field
    for i in range(0, cols + 1):
        possible_rows = generate_possible_rows(cols)




def generate_possible_rows(columns):
    return list(itertools.product([True, False], repeat=columns + 1))


def merge_rows(main_rows, new_rows, expected):
    """Given a 2 list of possible rows and the expected evolution, returns the valid rows that meet that criteria"""
    final = []
    for a in main_rows:
        for b in new_rows:
            # check valid or not row
            valid_combination(a, b, expected)
            ???

def valid_combination(row1, row2, expected):
    """Given 2 rows and a expected evolution, returns True or False if the given rows meet the expected"""


def get_evolution(cell):
    """Given a cell (2x2), returns True or False following the evolution of the gases"""
    total = 0
    if cell[0][0] is True:
        total += 1
    if cell[0][0] is True:
        total += 1
    if cell[0][0] is True:
        total += 1
    if cell[0][0] is True:
        total += 1
    if total == 1:
        return True
    else:  # thinking that 3 or 4 return false too
        return False





print(solution([[True, False, True],
                [False, True, False],
                [True, False, True]]))  # 4


print(solution([[True, False, True, False, False, True, True, True],
                [True, False, True, False, False, False, True, False],
                [True, True, True, False, False, False, True, False],
                [True, False, True, False, False, False, True, False],
                [True, False, True, False, False, True, True, True]]))  # 254

print(solution([[True, True, False, True, False, True, False, True, True, False],
                [True, True, False, False, False, False, True, True, True, False],
                [True, True, False, False, False, False, False, False, False, True],
                [False, True, False, False, False, False, True, True, False, False]]))  # 11567

