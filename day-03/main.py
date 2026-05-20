with open("day-03/my_input.txt", "r") as file:
    banks_list = [line.rstrip() for line in file]


def first_puzzle():
    output_joltage = 0
    bank_length = len(banks_list[0])

    for bank in banks_list:
        max_battery = max(bank)
        max_battery_id = bank.index(max_battery)

        if max_battery_id == bank_length - 1:
            next_max = max(bank[:-1])
            output_joltage += int(next_max)*10+int(max_battery)
        else:
            next_max = max(bank[max_battery_id+1:])
            output_joltage += int(max_battery)*10+int(next_max)

    print(output_joltage)

first_puzzle()