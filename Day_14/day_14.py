from datetime import datetime


def challenge_1():
    polymer_template, pair_insertion = load_polymer_data()

    polymer_template = insert_elements(polymer_template, pair_insertion, 10)

    amounts_of_each_element_object = get_amounts_of_each_element_object(polymer_template)

    amounts_of_each_element = get_amounts_of_each_element(amounts_of_each_element_object)

    print(max(amounts_of_each_element) - min(amounts_of_each_element))

def load_polymer_data():
    pair_insertion = {}
    polymer_template_obtained = False
    with open("Day_14/input.txt", "r+") as input:
        for line in input.readlines():
            if line.strip() == "":
                polymer_template_obtained = True
                continue
            if not polymer_template_obtained:
                polymer_template = line.strip()
                continue
            else:
                pair, insertion = line.strip().split(" -> ")
                pair_insertion[pair] = insertion

    return polymer_template, pair_insertion

def insert_elements(polymer_template, pair_insertion, number_of_steps):
    for step in range(number_of_steps):
        polymer_template = insert_into_pairs(polymer_template, pair_insertion)
    return polymer_template

def insert_into_pairs(polymer_template, pair_insertion):
    new_polymer_template = ""
    first = True
    for element in range(len(polymer_template) - 1):
        if first:
            new_polymer_template += polymer_template[element]
            first = False
        next_element = polymer_template[element + 1]
        insertion_element = pair_insertion[polymer_template[element] + next_element]
        new_polymer_template += insertion_element + next_element

    return new_polymer_template

def get_amounts_of_each_element_object(polymer_template):
    element_data = {}

    for element in polymer_template:
        if element not in element_data:
            element_data[element] = 1
        else:
            element_data[element] += 1
    
    return element_data

def get_amounts_of_each_element(element_data):
    element_amounts = []

    for amount in element_data.values():
        element_amounts.append(amount)

    return element_amounts

def challenge_2():
    polymer_template, pair_insertion = load_polymer_data()
    pair_data = {}

    for pair in pair_insertion.keys():
        pair_data[pair] = get_amounts_of_each_element_object(insert_elements(pair, pair_insertion, 20))
        pair_data[pair][pair[1]] -= 1

    polymer_template = insert_elements(polymer_template, pair_insertion, 20)

    amounts_of_each_element_object = {}

    for element_index in range(len(polymer_template) - 1):
        pair = polymer_template[element_index:element_index + 2]
        for element in pair_data[pair].keys():
            if element not in amounts_of_each_element_object:
                amounts_of_each_element_object[element] = pair_data[pair][element]
            else:
                amounts_of_each_element_object[element] += pair_data[pair][element]
    
    amounts_of_each_element_object[polymer_template[-1]] += 1

    amounts_of_each_element = get_amounts_of_each_element(amounts_of_each_element_object)

    print(max(amounts_of_each_element) - min(amounts_of_each_element))

if __name__ == "__main__":
    print("Starting Challenges for Day 14")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
