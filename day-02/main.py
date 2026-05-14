import time

start_time = time.time()

with open("day-02/my_input.txt", "r") as file:
    raw = file.readline().strip().split(",")

range_list = [[int(id) for id in pair.split("-")] for pair in raw]


def first_puzzle():
    total = 0
    for id_range in range_list:
        first_id, last_id = id_range
        for id in range(first_id, last_id+1):
            str_id = str(id)
            id_len = len(str_id)
            if id_len % 2 != 0:
                continue
            else:
                first_half, sec_half = str_id[:id_len//2], str_id[id_len//2:]
                if first_half == sec_half:
                    total += id
    print(total)


def second_puzzle():
    total = 0
    for id_range in range_list:
        first_id, last_id = id_range
        for id in range(first_id, last_id+1):
            str_id = str(id)
            id_len = len(str_id)
            max_index = id_len//2

            for i in range(1, max_index+1):
                if str_id.count(str_id[:i]) * i == id_len:
                    total += id
                    break
    print(total)


def elapsed():
    print("--- %s seconds ---" % (time.time() - start_time))


elapsed()
first_puzzle()
elapsed()
second_puzzle()
elapsed()
