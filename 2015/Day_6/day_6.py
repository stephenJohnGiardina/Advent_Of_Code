import os
from datetime import datetime


def challenge_1():
    light_grid = []
    for light_row in range(1000):
        light_grid.append([False] * 1000)
    instructions = obtain_instructions()
    for instruction in instructions:
        if instruction[0] == "turn on":
            turn_on_lights(light_grid, instruction[1], instruction[2])
        if instruction[0] == "turn off":
            turn_off_lights(light_grid, instruction[1], instruction[2])
        if instruction[0] == "toggle":
            toggle_lights(light_grid, instruction[1], instruction[2])

    number_of_lit_lights = 0
    for light_row in light_grid:
        for light in light_row:
            if light:
                number_of_lit_lights += 1
    print("Number of lit lights after instructions =", number_of_lit_lights)

def obtain_instructions():
    instructions = []
    with open(os.path.join("2015", "Day_6", "input.txt"), "r+") as input:
        for line in input.readlines():
            start_coordinate = tuple(map(lambda x: int(x), line.strip().split(" ")[-3].split(",")))
            end_coordinate = tuple(map(lambda x: int(x), line.strip().split(" ")[-1].split(",")))
            if "turn on" in line:
                instructions.append(("turn on", start_coordinate, end_coordinate))
            if "turn off" in line:
                instructions.append(("turn off", start_coordinate, end_coordinate))
            if "toggle" in line:
                instructions.append(("toggle", start_coordinate, end_coordinate))
    return instructions

def turn_on_lights(light_grid, start_coordinate, end_coordinate):
    for row in range(start_coordinate[0], end_coordinate[0] + 1):
        for col in range(start_coordinate[1], end_coordinate[1] + 1):
            light_grid[row][col] = True

def turn_off_lights(light_grid, start_coordinate, end_coordinate):
    for row in range(start_coordinate[0], end_coordinate[0] + 1):
        for col in range(start_coordinate[1], end_coordinate[1] + 1):
            light_grid[row][col] = False

def toggle_lights(light_grid, start_coordinate, end_coordinate):
    for row in range(start_coordinate[0], end_coordinate[0] + 1):
        for col in range(start_coordinate[1], end_coordinate[1] + 1):
            light_grid[row][col] = not light_grid[row][col]

def challenge_2():
    light_grid = []
    for light_row in range(1000):
        light_grid.append([0] * 1000)
    instructions = obtain_instructions()
    for instruction in instructions:
        if instruction[0] == "turn on":
            turn_on_lights_nordic_elvish(light_grid, instruction[1], instruction[2])
        if instruction[0] == "turn off":
            turn_off_lights_nordic_elvish(light_grid, instruction[1], instruction[2])
        if instruction[0] == "toggle":
            toggle_lights_nordic_elvish(light_grid, instruction[1], instruction[2])

    total_brightness = 0
    for light_row in light_grid:
        for light in light_row:
            total_brightness += light
    print("Total brightness of lit lights after instructions =", total_brightness)

def turn_on_lights_nordic_elvish(light_grid, start_coordinate, end_coordinate):
    for row in range(start_coordinate[0], end_coordinate[0] + 1):
        for col in range(start_coordinate[1], end_coordinate[1] + 1):
            light_grid[row][col] += 1

def turn_off_lights_nordic_elvish(light_grid, start_coordinate, end_coordinate):
    for row in range(start_coordinate[0], end_coordinate[0] + 1):
        for col in range(start_coordinate[1], end_coordinate[1] + 1):
            if light_grid[row][col] != 0:
                light_grid[row][col] = light_grid[row][col] - 1

def toggle_lights_nordic_elvish(light_grid, start_coordinate, end_coordinate):
    for row in range(start_coordinate[0], end_coordinate[0] + 1):
        for col in range(start_coordinate[1], end_coordinate[1] + 1):
            light_grid[row][col] += 2

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 6")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
