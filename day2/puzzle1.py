from puzzleinput import get_puzzle_input


def is_valid(nums: list[int]) -> bool:
    if nums[0] > nums[-1]:
        nums = list(reversed(nums))

    return is_ascending_gently(nums)


def is_ascending_gently(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1] or nums[i] > nums[i - 1] + 3:
            return False
    return True


def run_process(input: str) -> int:
    total = 0
    for line in input.splitlines():
        if line.strip() == "":
            continue
        nums = [int(item) for item in line.split()]
        if is_valid(nums):
            total += 1

    return total


print(run_process(get_puzzle_input(False)))
