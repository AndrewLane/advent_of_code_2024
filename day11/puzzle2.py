from functools import lru_cache

from puzzleinput import get_puzzle_input


@lru_cache(maxsize=None)
def count_stones_after_iterations(stones: tuple, iterations: int):
    if len(stones) > 1:
        return sum(
            [
                count_stones_after_iterations((stones[i],), iterations)
                for i in range(len(stones))
            ]
        )
    # we have a single stone
    stone: int = stones[0]
    transformed_stones = []
    if stone == 0:
        transformed_stones = [1]
    else:
        num_digits_on_stone = len(str(stone))
        if num_digits_on_stone % 2 == 0:
            # split the digits in half
            left, right = (
                str(stone)[: num_digits_on_stone // 2],
                str(stone)[num_digits_on_stone // 2 :],
            )
            transformed_stones = [int(left), int(right)]
        else:
            transformed_stones = [stone * 2024]
    if iterations == 1:
        return len(transformed_stones)
    return count_stones_after_iterations(tuple(transformed_stones), iterations - 1)


def run_process(input):
    stones = [int(stone) for stone in input.split(" ")]
    return count_stones_after_iterations(tuple(stones), 75)


print(run_process(get_puzzle_input(False)))
