import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode= "r") as json_file:
        data = json.load(json_file)
    if field in data:
        return data[field]


def linear_search(unoordered_numbers, searched_number):
    positions = []
    count = 0
    for position, number in enumerate(unoordered_numbers):
        if number == searched_number:
            count += 1
            positions.append(position)

    output = dict()
    output['positions'] = positions
    output['count'] = count
    return output
"""
number_of_number = 0
for value in file_name.values():
    if value == number:
        number_of_number += 1

return  dict(zip(positions, number_of_number))
"""
def pattern_search(dna_sequence, vzor):
    """def split(ATA):
        return [char for char in ATA]
        """
    positions = []
    for i, pismeno in enumerate(dna_sequence):
        if vzor == dna_sequence[i:i+len(vzor)]:
            positions.append(i)
    return set(positions)




def main():
    unorsered_nums = read_data("sequential.json", "unordered_numbers" )
    lo = linear_search(unorsered_nums, 9)
    print(lo)
    dna_sequence = read_data("sequential.json", "dna_sequence")
    fg = pattern_search(dna_sequence, "ATA")
    print(fg)

if __name__ == '__main__':
    main()
