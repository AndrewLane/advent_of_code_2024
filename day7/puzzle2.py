from puzzleinput import get_puzzle_input


def can_multiplication_or_addition_or_concat_operations_work(result, numbers):
    if len(numbers) == 1:
        return numbers[0] == result

    first_number = numbers[0]
    can_multiplication_work = result % first_number == 0
    if can_multiplication_or_addition_or_concat_operations_work(
        result - first_number, numbers[1:]
    ):
        return True
    if (
        can_multiplication_work
        and can_multiplication_or_addition_or_concat_operations_work(
            int(result / first_number), numbers[1:]
        )
    ):
        return True

    chars_in_first_number = len(str(first_number))
    chars_in_result = len(str(result))
    can_concat_work = False
    if chars_in_result > chars_in_first_number:
        last_part_of_result = int(str(result)[-chars_in_first_number:])
        can_concat_work = last_part_of_result == first_number

    return can_concat_work and can_multiplication_or_addition_or_concat_operations_work(
        int(str(result)[:-chars_in_first_number]), numbers[1:]
    )


def run_process(input: str) -> int:
    total = 0
    for line in input.splitlines():
        if line.strip() == "":
            continue

        result, numbers = line.split(":")
        result = int(result)
        numbers = list(reversed(list(map(int, numbers.split()))))

        if can_multiplication_or_addition_or_concat_operations_work(result, numbers):
            total += result

    return total


print(run_process(get_puzzle_input(False)))
