from puzzleinput import get_puzzle_input


def is_rule_violated(rule, update):
    before, after = rule
    if before in update and after in update:
        before_index = update.index(before)
        after_index = update.index(after)
        return before_index > after_index

    return False


def run_process(input):
    order_rules = []
    updates = []
    for line in input.splitlines():
        if line.strip() == "":
            continue
        if "|" in line:
            before, after = line.split("|")
            order_rules.append((before, after))
        elif "," in line:
            updates_array = line.split(",")
            assert len(updates_array) % 2 == 1, "Expected an odd number of updates"
            updates.append(updates_array)
        else:
            raise Exception("Unexpected line: " + line)

    total = 0
    for update in updates:
        rule_violated = False
        for rule in order_rules:
            if rule_violated == False and is_rule_violated(rule, update):
                rule_violated = True
                break
        if rule_violated == False:
            middle_number_of_update = int(update[len(update) // 2])
            total += middle_number_of_update

    return total


print(run_process(get_puzzle_input(False)))
