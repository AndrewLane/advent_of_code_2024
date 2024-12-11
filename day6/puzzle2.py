from enum import Enum

from puzzleinput import get_puzzle_input


# create an enum of directions
class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


def iterate(rows, start_location, new_obstacle):
    direction = Direction.UP
    location = start_location

    already_visited = []
    already_visited.append(location)

    loop_found = False
    done = False
    total_steps = 0
    while done == False:
        total_steps += 1
        if total_steps > len(rows) * len(rows[0]):
            loop_found = True
            done = True
            break
        # print("i'm at ", location, "facing", direction)
        is_next_step_off_grid = (
            (direction == Direction.UP and location[1] == 0)
            or (direction == Direction.LEFT and location[0] == 0)
            or (direction == Direction.DOWN and location[1] == len(rows) - 1)
            or (direction == Direction.RIGHT and location[0] == len(rows[0]) - 1)
        )
        if is_next_step_off_grid:
            done = True
            break
        else:
            next_location = (
                (location[0], location[1] - 1)
                if direction == Direction.UP
                else (
                    (location[0] + 1, location[1])
                    if direction == Direction.RIGHT
                    else (
                        (location[0], location[1] + 1)
                        if direction == Direction.DOWN
                        else (location[0] - 1, location[1])
                    )
                )
            )
            # print("next location is ", next_location)
            if (
                rows[next_location[1]][next_location[0]] == "#"
                or next_location == new_obstacle
            ):
                # blocked, so turn right
                direction = Direction((direction.value % 4) + 1)
            else:
                # not blocked, so move forward
                location = next_location
                if location not in already_visited:
                    already_visited.append(location)

    return loop_found


def run_process(input: str) -> int:
    rows = []
    start_location = (0, 0)
    row_index = 0
    for line in input.splitlines():
        if line.strip() == "":
            continue
        periods = line.count(".")
        carets = line.count("^")
        hashes = line.count("#")
        if periods + carets + hashes != len(line):
            raise ValueError(f"Invalid line: {line}")
        if carets > 0:
            start_location = (line.index("^"), row_index)

        # split line into characters
        row = [character for character in line]
        rows.append(row)
        row_index += 1

    total = 0
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if (x, y) != start_location:
                print("obstacle at (", x, y, "), start_location at ", start_location)
                if iterate(rows, start_location, (x, y)):
                    total += 1
    return total


print(run_process(get_puzzle_input(False)))