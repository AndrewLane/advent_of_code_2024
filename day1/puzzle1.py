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

    list1 = sorted(list1)
    list2 = sorted(list2)

    total = 0
    for list1entry, list2entry in zip(list1, list2):
        total += abs(list1entry - list2entry)
    return total


print(run_process(get_puzzle_input(False)))
