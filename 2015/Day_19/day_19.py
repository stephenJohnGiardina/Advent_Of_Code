import os
from datetime import datetime


def challenge_1():
    molecule_operations, starting_molecule = obtain_input()
    distinct_molecules = find_distinct_molecules(molecule_operations, starting_molecule)
    print("Number of distinct molecules =", len(distinct_molecules))

def convert_molecule_string_to_list(molecule_string):
    molecule_list = []
    current_element = ""
    for char_index, char in enumerate(molecule_string):
        if char_index < len(molecule_string) - 1:
            if molecule_string[char_index + 1].isupper():
                molecule_list.append(current_element + char)
                current_element = ""
            else:
                current_element += char
        else:
            molecule_list.append(current_element + char)
    return molecule_list

def obtain_input():
    molecule_operations = {}
    with open(os.path.join("2015", "Day_19", "input.txt"), "r+") as input:
        all_operations_found = False
        for line in input.readlines():
            if not all_operations_found:
                if line.strip() == "":
                    all_operations_found = True
                else:
                    molecule_operation = line.strip().split(" => ")
                    if molecule_operation[0] in molecule_operations:
                        molecule_operations[molecule_operation[0]].append(convert_molecule_string_to_list(molecule_operation[1]))
                    else:
                        molecule_operations[molecule_operation[0]] = [convert_molecule_string_to_list(molecule_operation[1])]
            else:
                starting_molecule = convert_molecule_string_to_list(line.strip())
    return molecule_operations, starting_molecule

def find_distinct_molecules(molecule_operations, starting_molecule):
    distinct_molecules = set()
    for element_index, element in enumerate(starting_molecule):
        for input_molecule in molecule_operations.keys():
            for replacement_molecule in molecule_operations[input_molecule]:
                if input_molecule == element:
                    distinct_molecules.add("".join(starting_molecule[:element_index] + replacement_molecule + starting_molecule[element_index + 1:]))
    return distinct_molecules

def challenge_2():
    molecule_operations, starting_molecule = obtain_input()
    reverse_molecule_operations = get_reverse_molecule_operations(molecule_operations)
    starting_molecule_string = "".join(starting_molecule)
    min_number_of_steps_to_reverse_molecule = find_min_number_of_steps_to_reverse_molecule(reverse_molecule_operations, starting_molecule_string)
    print("Minimum number of replacments needed to go from e to medicine molecule =", min_number_of_steps_to_reverse_molecule)

def get_reverse_molecule_operations(molecule_operations):
    reverse_molecule_operations = {}
    for element, replacement_molecules in molecule_operations.items():
        for replacement_molecule in replacement_molecules:
            reverse_molecule_operations["".join(replacement_molecule)] = element
    return reverse_molecule_operations

def find_min_number_of_steps_to_reverse_molecule(reverse_molecule_operations, molecule_string):
    if molecule_string == "e":
        return 0
    for reverse_molecule, element in reverse_molecule_operations.items():
        if reverse_molecule in molecule_string:
            reverse_molecule_index = molecule_string.index(reverse_molecule)
            new_molecule_string = molecule_string[:reverse_molecule_index] + element + molecule_string[reverse_molecule_index + len(reverse_molecule):]
            return find_min_number_of_steps_to_reverse_molecule(
                reverse_molecule_operations,
                new_molecule_string
                ) + 1

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 19")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
