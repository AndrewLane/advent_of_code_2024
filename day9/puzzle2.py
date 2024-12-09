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


def can_file_fit_here(file_ids, file_length, index):

    if index >= len(file_ids):
        return False

    for i in range(file_length):
        if file_ids[index + i] != -1:
            return False
    return True


def run_process(input):
    total_blocks = get_total_blocks(input)
    file_ids = [-1] * total_blocks

    file_id = 0
    empty_space_mode = False
    current_block_index = 0
    max_file_id = 0
    file_pointers_dict = {}
    file_length_dict = {}
    for i in range(len(input)):
        this_value = int(input[i])

        if not empty_space_mode:
            file_pointers_dict[file_id] = current_block_index
            file_length_dict[file_id] = this_value

        for _ in range(this_value):
            if not empty_space_mode:
                file_ids[current_block_index] = file_id
                max_file_id = file_id
            current_block_index += 1

        if not empty_space_mode:
            file_id += 1

        empty_space_mode = not empty_space_mode

    # print("max file id", max_file_id)
    # print(file_pointers_dict)
    # print(file_length_dict)
    # print(file_ids)

    file_id_to_be_moved = max_file_id
    while file_id_to_be_moved >= 0:
        # print("looking at file id", file_id_to_be_moved)
        left_pointer = 0
        this_file_length = file_length_dict[file_id_to_be_moved]
        this_file_pointer = file_pointers_dict[file_id_to_be_moved]

        for left_pointer in range(0, this_file_pointer - 1):
            if can_file_fit_here(file_ids, this_file_length, left_pointer):
                # print(
                #     "file id to be moved",
                #     file_id_to_be_moved,
                #     "can be moved to left_pointer",
                #     left_pointer,
                # )
                for i in range(this_file_length):
                    file_ids[left_pointer + i] = file_id_to_be_moved
                    file_ids[this_file_pointer + i] = -1
                # print(file_ids)
                break

        file_id_to_be_moved -= 1

    return calculate_checksum(file_ids)


print(run_process(get_puzzle_input(False)))
