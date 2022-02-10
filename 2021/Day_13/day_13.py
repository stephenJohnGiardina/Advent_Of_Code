import os
from datetime import datetime


def challenge_1():
    coordinates, instructions = load_paper()
    coordinates = fold_vertically(coordinates, instructions[0][1])

    print(len(coordinates))

def load_paper():
    coordinates = []
    instructions = []
    all_coordinates_found = False
    with open(os.path.join("2021", "Day_13", "input.txt"), "r+") as input:
        for line in input.readlines():
            if line.strip() == "":
                all_coordinates_found = True
                continue
            if not all_coordinates_found:
                coordinates.append(tuple(map(lambda x: int(x), line.strip().split(","))))
            else:
                instruction = line.strip().split("=")
                direction = instruction[0][-1]
                location = int(instruction[1])
                instructions.append((direction, location))

    return coordinates, instructions

def fold_vertically(coordinates, location):
    new_coordinates = []

    for coordinate in coordinates:
        if coordinate[0] > location:
            new_x = location - (coordinate[0] - location)
            new_y = coordinate[1]
            new_coordinate = (new_x, new_y)
            new_coordinates.append(new_coordinate)
        else:
            new_coordinates.append(coordinate)
    
    return list(set(new_coordinates))

def challenge_2():
    coordinates, instructions = load_paper()

    for instruction in instructions:
        if instruction[0] == "x":
            coordinates = fold_vertically(coordinates, instruction[1])
        if instruction[0] == "y":
            coordinates = fold_horizontally(coordinates, instruction[1])

    print_paper(coordinates)

def fold_horizontally(coordinates, location):
    new_coordinates = []

    for coordinate in coordinates:
        if coordinate[1] > location:
            new_x = coordinate[0]
            new_y = location - (coordinate[1] - location)
            new_coordinate = (new_x, new_y)
            new_coordinates.append(new_coordinate)
        else:
            new_coordinates.append(coordinate)
    
    return list(set(new_coordinates))

def print_paper(coordinates):
    max_x = 0
    max_y = 0

    paper = []

    for coordinate in coordinates:
        if coordinate[0] > max_x:
            max_x = coordinate[0]
        if coordinate[1] > max_y:
            max_y = coordinate[1]

    for row in range(max_y + 1):
        paper_row = []
        for col in range(max_x + 1):
            if (col, row) in coordinates:
                paper_row.append("#")
            else:
                paper_row.append(" ")
        paper.append("".join(paper_row))
    
    for line in paper:
        print(line)

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 13")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
