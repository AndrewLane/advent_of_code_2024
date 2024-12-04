from puzzleinput import get_puzzle_input


def are_complimentary_pair(char1: str, char2: str) -> bool:
    return (char1 == "M" and char2 == "S") or (char1 == "S" and char2 == "M")


def run_process(input):
    rows = []
    for line in input.splitlines():
        if line.strip() == "":
            continue

        # split each line into an array of characters
        rows.append(list(line))

    total = 0
    for row_index in range(1, len(rows) - 1):
        for column_index in range(1, len(rows[0]) - 1):
            if rows[row_index][column_index] == "A":
                upper_left = rows[row_index - 1][column_index - 1]
                upper_right = rows[row_index - 1][column_index + 1]
                lower_left = rows[row_index + 1][column_index - 1]
                lower_right = rows[row_index + 1][column_index + 1]
                if are_complimentary_pair(
                    upper_left, lower_right
                ) and are_complimentary_pair(upper_right, lower_left):
                    total += 1

    return total


print(run_process(get_puzzle_input(False)))
