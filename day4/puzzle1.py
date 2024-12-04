from puzzleinput import get_puzzle_input


# get the count going both backwards and forwards
def get_xmas_count_in_string(input: str) -> int:
    # print("testing ", input)
    normal_way = input.count("XMAS")
    backwards = input[::-1].count("XMAS")
    return normal_way + backwards


def run_process(input):
    rows = []
    for line in input.splitlines():
        if line.strip() == "":
            continue

        # split each line into an array of characters
        rows.append(list(line))

    total = 0

    # horizontal left-to-right and right-to-left
    for row in rows:
        total += get_xmas_count_in_string("".join(row))
        print(total)

    # vertical top-to-bottom and bottom-to-top
    for i in range(len(rows[0])):
        total += get_xmas_count_in_string("".join([row[i] for row in rows]))
        print(total)

    # diagonal down-to-the-right and up-to-the-left, part 1
    for i in range(len(rows[0])):
        total += get_xmas_count_in_string(
            "".join([rows[j][j + i] for j in range(len(rows) - i)])
        )
        print(total)

    # diagonal down-to-the-right and up-to-the-left, part 2
    for j in range(1, len(rows)):
        total += get_xmas_count_in_string(
            "".join([rows[j + i][i] for i in range(len(rows) - j)])
        )
        print(total)

    # diagonal down-to-the-left and up-to-the-right, part 1
    for i in range(len(rows[0])):
        total += get_xmas_count_in_string(
            "".join([rows[j][i - j] for j in range(i + 1)])
        )
        print(total)

    # diagonal down-to-the-left and up-to-the-right, part 2
    for j in range(1, len(rows)):
        total += get_xmas_count_in_string(
            "".join([rows[j + i][len(rows) - i - 1] for i in range(len(rows) - j)])
        )
        print(total)

    return total


print(run_process(get_puzzle_input(False)))
