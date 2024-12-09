from enum import Enum

from puzzleinput import get_puzzle_input


def is_antinode_in_valid_location(antinode: tuple, width: int, height: int) -> bool:
    x = antinode[0]
    y = antinode[1]
    return 0 <= x < width and 0 <= y < height


def run_process(input: str) -> int:
    attenae_dict = {}
    row_index = 0
    for line in input.splitlines():
        # split line into characters
        for idx, character in enumerate(line):
            if character.isalpha() or character.isdigit():
                if character not in attenae_dict:
                    attenae_dict[character] = []
                attenae_dict[character].append((idx, row_index))
            elif character == ".":
                pass  # expected
            else:
                raise Exception(
                    f"Unexpected character in input: {character} on line {row_index}"
                )
        row_index += 1

    height = row_index
    width = len(line)

    antinode_locations = []
    for node_type in attenae_dict.keys():
        if len(attenae_dict[node_type]) >= 1:
            # iterate through all pairs of nodes
            for idx, node1 in enumerate(attenae_dict[node_type]):
                for node2 in attenae_dict[node_type][idx + 1 :]:
                    x1 = node1[0]
                    y1 = node1[1]
                    x2 = node2[0]
                    y2 = node2[1]
                    rise = y2 - y1
                    run = x2 - x1
                    antinode_1 = (x1 - run, y1 - rise)
                    antinode_2 = (x2 + run, y2 + rise)
                    if is_antinode_in_valid_location(antinode_1, width, height):
                        antinode_locations.append(antinode_1)
                    if is_antinode_in_valid_location(antinode_2, width, height):
                        antinode_locations.append(antinode_2)

    return len(set(antinode_locations))


print(run_process(get_puzzle_input(False)))
