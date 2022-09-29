import os
from datetime import datetime


def challenge_1():
    light_matrix = get_light_matrix()
    for step in range(100):
        toggle_lights(light_matrix)
    number_of_on_lights = get_number_of_on_lights(light_matrix)
    print("Number of on lights after 100 steps =", number_of_on_lights)

def get_light_matrix():
    light_matrix = []
    with open(os.path.join("2015", "Day_18", "input.txt"), "r+") as input:
        for line in input.readlines():
            light_matrix.append(list(line.strip()))
    return light_matrix

def find_number_of_on_adjacent_lights(light_matrix, row_index, col_index):
    all_nieghbor_coordinates = [
        (row_index - 1, col_index - 1),
        (row_index, col_index - 1),
        (row_index + 1, col_index - 1),
        (row_index + 1, col_index),
        (row_index + 1, col_index + 1),
        (row_index, col_index + 1),
        (row_index - 1, col_index + 1),
        (row_index - 1, col_index),
    ]
    number_of_on_adjacent_lights = 0
    for nieghbor_coordinate in all_nieghbor_coordinates:
        if -1 not in nieghbor_coordinate and len(light_matrix) not in nieghbor_coordinate:
            if light_matrix[nieghbor_coordinate[0]][nieghbor_coordinate[1]] == "#":
                number_of_on_adjacent_lights += 1
    return number_of_on_adjacent_lights

def toggle_lights(light_matrix, leave_corner_lights_on=False):
    light_matrix_length = len(light_matrix)
    corner_coordinates = [
        (0, 0),
        (light_matrix_length - 1, 0),
        (0, light_matrix_length - 1),
        (light_matrix_length - 1, light_matrix_length - 1),
    ]
    toggle_coordinates = []
    for row_index, row in enumerate(light_matrix):
        for col_index, col in enumerate(row):
            number_of_on_adjacent_lights = find_number_of_on_adjacent_lights(light_matrix, row_index, col_index)
            if col == "#":
                if number_of_on_adjacent_lights not in (2, 3):
                    if not (leave_corner_lights_on and (row_index, col_index) in corner_coordinates):
                        toggle_coordinates.append((row_index, col_index))
            elif col == ".":
                if number_of_on_adjacent_lights == 3:
                    toggle_coordinates.append((row_index, col_index))
    for toggle_coordinate in toggle_coordinates:
        current_toggle = light_matrix[toggle_coordinate[0]][toggle_coordinate[1]]
        if current_toggle == "#":
            light_matrix[toggle_coordinate[0]][toggle_coordinate[1]] = "."
        elif current_toggle == ".":
            light_matrix[toggle_coordinate[0]][toggle_coordinate[1]] = "#"

def get_number_of_on_lights(light_matrix):
    number_of_on_lights = 0
    for row in light_matrix:
        for col in row:
            if col == "#":
                number_of_on_lights += 1
    return number_of_on_lights

def challenge_2():
    light_matrix = get_light_matrix()
    light_matrix_length = len(light_matrix)
    light_matrix[0][0] = "#"
    light_matrix[light_matrix_length - 1][0] = "#"
    light_matrix[0][light_matrix_length - 1] = "#"
    light_matrix[light_matrix_length - 1][light_matrix_length - 1] = "#"
    for step in range(100):
        toggle_lights(light_matrix, True)
    number_of_on_lights = get_number_of_on_lights(light_matrix)
    print("Number of on lights after 100 steps with corners left on =", number_of_on_lights)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 18")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
