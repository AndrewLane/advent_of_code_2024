from puzzleinput import get_puzzle_input


def can_multiplication_or_addition_operations_work(result, numbers):
    if len(numbers) == 1:
        return numbers[0] == result

    first_number = numbers[0]
    can_multiplication_work = result % first_number == 0
    return can_multiplication_or_addition_operations_work(
        result - first_number, numbers[1:]
    ) or (
        can_multiplication_work
        and can_multiplication_or_addition_operations_work(
            int(result / first_number), numbers[1:]
        )
    )


def run_process(input: str) -> int:
    total = 0
    for line in input.splitlines():
        if line.strip() == "":
            continue

        result, numbers = line.split(":")
        result = int(result)
        numbers = list(reversed(list(map(int, numbers.split()))))

        if can_multiplication_or_addition_operations_work(result, numbers):
            total += result

    return total


print(run_process(get_puzzle_input(False)))
