diagram = []

with open("day-07/my_input.txt", "r") as file:
    for line in file:
        diagram.append(list(line.strip()))

def second_puzzle():
    current_line = 0
    current_beams = {diagram[0].index("S"): 1}

    while True:
        new_current_beams = {}
        next_line = current_line + 2
        for coord, count in current_beams.items():

            if diagram[next_line][coord] == "^":
                coord_l = coord - 1
                coord_r = coord + 1

                if coord_l in new_current_beams:
                    new_current_beams[coord_l] = new_current_beams[coord_l] + count
                else:
                    new_current_beams[coord_l] = count

                if coord_r in new_current_beams:
                    new_current_beams[coord_r] = new_current_beams[coord_r] + count
                else:
                    new_current_beams[coord_r] = count
            else:
                if coord in new_current_beams:
                    new_current_beams[coord] = new_current_beams[coord] + count
                else:
                    new_current_beams[coord] = count

        current_beams = new_current_beams
        current_line = next_line

        if current_line +2 >= len(diagram):
            break

    print(sum(current_beams.values()))


def first_puzzle():
    beam_origin = (0, diagram[0].index("S"))
    beam_split = 0

    current_beams = [beam_origin]
    while True:
        new_current_beams = []
        beams_to_remove = []
        for beam in current_beams:

            if diagram[beam[0]+2][beam[1]] == "^":
                new_current_beams.extend([(beam[0]+2, beam[1]-1),
                                          (beam[0]+2, beam[1]+1)])
                beams_to_remove.append(beam)
                beam_split += 1
            else:
                new_current_beams.append((beam[0]+2, beam[1]))
                beams_to_remove.append(beam)
        for beam in new_current_beams:
            current_beams.append(beam)
        for beam in beams_to_remove:
            current_beams.remove(beam)

        current_beams = list(dict.fromkeys(current_beams))

        if current_beams[0][0]+2 >= len(diagram):
            break

    print(beam_split)

first_puzzle()
second_puzzle()