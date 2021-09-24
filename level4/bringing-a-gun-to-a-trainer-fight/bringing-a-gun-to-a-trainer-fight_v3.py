# Generate all possible directions, follow them, break if repeated path
import sys

def solution(dimensions, your_position, trainer_position, distance):

    width = dimensions[0]
    height = dimensions[1]

    me = (your_position[0], your_position[1])
    trainer = (trainer_position[0], trainer_position[1])

    p = generate_possibilities(width, height)
    total = 0
    directions = []
    max_distance = distance * distance
    distance = 0

    for direction in p:
        passed = {}
        first_step, new_distance = step(me, direction, width, height)
        found = follow_path(first_step, me, trainer, width, height, direction, distance + new_distance, max_distance, passed)
        if found is True:
            total += 1
            directions.append(direction)

    #for d in directions:
     #  print("(" + str(d.x) + ", " + str(d.y) + ")")
    return total


class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def generate_possibilities(width, height):
    """
    Given an scenario, creates an array of possibilities where the trainer can shot
    """
    p = []
    p.append(Direction(0, 1))
    p.append(Direction(1, 0))
    for i in range(1, width+1):
        for j in range(1, height+1):
            if check_repeated(i, j) is True:
                p.append(Direction(i, j))
                p.append(Direction(-i, j))
                p.append(Direction(i, -j))
                p.append(Direction(-i, -j))
    return p


def check_repeated(x, y):
    return x == 1 or y == 1 or (x % y != 0 and y % x != 0)


def follow_path(start_point, me, goal, width, height, direction, distance, max_distance, passed, found=False):
    """
    Follow the path of a bullet
    """
    if distance > max_distance:  # more distance than possible
        return False
    #if str(start_point) in passed:  # repeated step
    #    return False
    if start_point == goal:
        return True
    if start_point == me:  # we should skip first iteration of this outside of this function
        return False
    ####
    #passed[str(start_point)] = True
    point, new_distance = step(start_point, direction, width, height)
    return follow_path(point, me, goal, width, height, direction, distance + new_distance, max_distance, passed, found)


def step(a, direction, width, height, distance=0):
    """
    Makes a move on tuples, using walls or not
    :param a: start point
    :param direction: direction
    :param width: max width
    :param height: max height
    :param distance: distance in this step
    :return: tuple with new location and number of walls used
    """
    x = a[0] + direction.x
    y = a[1] + direction.y
    if x > width:
        tmp = x - width
        x = width - tmp + 1
        distance = distance + 2
        direction.x = direction.x * -1
    if y > height:
        tmp = y - height
        y = height - tmp + 1
        distance = distance + 2
        direction.y = direction.y * -1
    if x < 1:
        x = abs(x)
        distance = distance + 2
        direction.x = direction.x * -1
    if y < 1:
        y = abs(y)
        distance = distance + 2
        direction.y = direction.y * -1

    tmp = (x, y)
    distance = distance + abs(direction.x) + abs(direction.y)
    return tmp, distance

sys.setrecursionlimit(1500)
print(solution([3, 2], [1, 1], [2, 1], 4))  # 7
print(solution([3, 2], [1, 1], [2, 2], 8))  # 3
print(solution([3, 2], [1, 1], [2, 2], 1))  # 0
print(solution([3, 3], [1, 1], [3, 3], 1))  # 0
print(solution([3, 3], [1, 1], [3, 3], 2))  # ?
print(solution([3, 3], [1, 1], [3, 3], 3))  # 5?
print(solution([300, 275], [150, 150], [185, 100], 500))  # 9
#print(solution([1250, 1250], [150, 150], [185, 100], 500))  # 9