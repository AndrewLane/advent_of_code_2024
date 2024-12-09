from puzzleinput import get_puzzle_input


def is_rule_violated(rule, update):
    before, after = rule
    if before in update and after in update:
        before_index = update.index(before)
        after_index = update.index(after)
        return before_index > after_index

    return False


def does_update_pass_all_rules(update, rules):
    for rule in rules:
        if is_rule_violated(rule, update):
            return False

    return True


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

    updates_with_violations = []
    for update in updates:
        if does_update_pass_all_rules(update, order_rules) == False:
            updates_with_violations.append(update)

    total = 0
    for update in updates_with_violations:
        done = False
        while done == False:
            # just swap the elements with the violation continuously until we get a valid rule
            rule_violation_found = False
            for rule in order_rules:
                if is_rule_violated(rule, update):
                    before, after = rule
                    before_index = update.index(before)
                    after_index = update.index(after)
                    update[before_index], update[after_index] = (
                        update[after_index],
                        update[before_index],
                    )
                    rule_violation_found = True
                    break

            if rule_violation_found == False:
                # if we get this far, there's no rule violations
                total += int(update[len(update) // 2])
                done = True

    return total


print(run_process(get_puzzle_input(False)))
