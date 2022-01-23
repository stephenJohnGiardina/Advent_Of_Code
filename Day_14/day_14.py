def challenge_1():
    polymer_template, pair_insertion = load_polymer_data()

    for step in range(10):
        polymer_template = insert_into_pairs(polymer_template, pair_insertion)

    amounts_of_each_element = get_amounts_of_each_element(polymer_template)

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

def get_amounts_of_each_element(polymer_template):
    element_data = {}

    for element in polymer_template:
        if element not in element_data:
            element_data[element] = 1
        else:
            element_data[element] += 1
    
    element_amounts = []

    for amount in element_data.values():
        element_amounts.append(amount)
    
    return element_amounts

def challenge_2():
    pass

if __name__ == "__main__":
    challenge_1()
    challenge_2()