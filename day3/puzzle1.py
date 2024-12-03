from puzzleinput import get_puzzle_input
import re


def run_process(input: str) -> int:
    mult_regex = r"mul\(\d{1,3},\d{1,3}\)"

    total = 0

    # fetch all the places that input matches mult_regex
    matches = re.findall(mult_regex, input)
    for match in matches:
        before_comma, after_comma = match[4:-1].split(",")
        total += int(before_comma) * int(after_comma)

    return total


print(run_process(get_puzzle_input(False)))
