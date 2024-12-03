from puzzleinput import get_puzzle_input
import re

def find_all_occurrences(substring, string):
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        yield start
        start += len(substring)


def is_mult_enabled(index: int, indexes_of_dont_token: int, indexes_of_do_token: int) -> bool:
    do_token_indices = [idx for idx in indexes_of_do_token if idx < index]
    dont_token_indices = [idx for idx in indexes_of_dont_token if idx < index]
    most_recent_do = max(do_token_indices) if do_token_indices else -1
    most_recent_dont = max(dont_token_indices) if dont_token_indices else -1
    if most_recent_do > 0 and most_recent_dont > 0:
        return most_recent_do > most_recent_dont
    elif most_recent_do > 0:
        return True
    elif most_recent_dont > 0:
        return False
    return True

def run_process(input: str) -> int:
    mult_regex = r"mul\(\d{1,3},\d{1,3}\)"

    dont_token = "don't()"
    do_token = "do()"

    indexes_of_dont_token = list(find_all_occurrences(dont_token, input))
    index_of_do_token = list(find_all_occurrences(do_token, input))
    
    total = 0

    # fetch all the places that input matches mult_regex and include their index
    matches = re.finditer(mult_regex, input)
    for match in matches:
        index = match.start()
        match_text = match.group()
        if is_mult_enabled(index, indexes_of_dont_token, index_of_do_token):
            before_comma, after_comma = match_text[4:-1].split(",")
            total += int(before_comma) * int(after_comma)
    
    return total

print(run_process(get_puzzle_input(2, False)))
