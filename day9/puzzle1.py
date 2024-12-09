from puzzleinput import get_puzzle_input


def get_total_blocks(input):
    return sum(int(value) for value in input)


def calculate_checksum(file_ids):
    total = 0
    for i in range(len(file_ids)):
        this_value = file_ids[i]
        if this_value == -1:
            continue
        total += i * this_value
    return total


def run_process(input):
    total_blocks = get_total_blocks(input)
    file_ids = [-1] * total_blocks

    file_id = 0
    empty_space_mode = False
    current_block_index = 0
    for i in range(len(input)):
        this_value = int(input[i])

        for j in range(this_value):
            if not empty_space_mode:
                file_ids[current_block_index] = file_id
            current_block_index += 1

        if not empty_space_mode:
            file_id += 1

        empty_space_mode = not empty_space_mode

    # print(file_ids)

    left_pointer = 0
    right_pointer = len(file_ids) - 1
    done = False
    while done == False:
        if file_ids[right_pointer] >= 0:
            while file_ids[left_pointer] >= 0:
                left_pointer += 1
            if right_pointer <= left_pointer:
                done = True
                break

            file_ids[left_pointer] = file_ids[right_pointer]
            file_ids[right_pointer] = -1
        right_pointer -= 1

    # print(file_ids)

    return calculate_checksum(file_ids)


print(run_process(get_puzzle_input(False)))
