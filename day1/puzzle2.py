from puzzleinput import get_puzzle_input


def run_process(input):
    list1 = []
    list2 = []
    for line in input.splitlines():
        if line.strip() == "":
            continue
        list1entry, list2entry = line.split()
        list1.append(int(list1entry))
        list2.append(int(list2entry))

    total = 0
    for list1entry in list1:
        number_of_times_in_second_list = list2.count(list1entry)
        total += number_of_times_in_second_list * list1entry

    return total


print(run_process(get_puzzle_input(False)))
