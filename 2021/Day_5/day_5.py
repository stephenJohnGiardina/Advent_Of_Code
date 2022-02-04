from datetime import datetime


def challenge_1():
    coordinate_map = make_coordinate_map(1000)
    coordinates = load_coordinates()
    for coordinate_pair in coordinates:
        update_coordinate_map(coordinate_pair, coordinate_map)
     
    overlapping_lines = find_overlapping_lines(coordinate_map)

    print(overlapping_lines)

def make_coordinate_map(side_length):
    coordinate_map = []
    for row in range(side_length):
        row = []
        for coordinate in range(side_length):
            row.append(0)
        coordinate_map.append(row)
    return coordinate_map

def load_coordinates():
    coordinates = []
    with open("2021/Day_5/input.txt", "r+") as input:
        for line in input.readlines():
            coordinate_pair = list(map(lambda x: x.strip(), line.split("->")))
            coordinate_pair = list(map(lambda x: x.split(","), coordinate_pair))
            coordinate_pair = list(map(lambda x: list(map(lambda y: int(y), x)), coordinate_pair))
            coordinates.append(coordinate_pair)

    return coordinates

def update_coordinate_map(coordinate_pair, coordinate_map):
    if coordinate_pair[0][0] !=  coordinate_pair[1][0] and coordinate_pair[0][1] !=  coordinate_pair[1][1]:
        return
    if coordinate_pair[0][0] !=  coordinate_pair[1][0]:
        update_coordinate_map_horizontal(coordinate_pair, coordinate_map)
    elif coordinate_pair[0][1] !=  coordinate_pair[1][1]:
        update_coordinate_map_vertical(coordinate_pair, coordinate_map)

def update_coordinate_map_horizontal(coordinate_pair, coordinate_map):
    if coordinate_pair[0][0] > coordinate_pair[1][0]:
        larger_value = coordinate_pair[0][0]
        smaller_value = coordinate_pair[1][0]
    elif coordinate_pair[1][0] > coordinate_pair[0][0]:
        larger_value = coordinate_pair[1][0]
        smaller_value = coordinate_pair[0][0]
    for coordinate in range(smaller_value, larger_value + 1):
        coordinate_map[coordinate_pair[0][1]][coordinate] += 1

def update_coordinate_map_vertical(coordinate_pair, coordinate_map):
    if coordinate_pair[0][1] > coordinate_pair[1][1]:
        larger_value = coordinate_pair[0][1]
        smaller_value = coordinate_pair[1][1]
    elif coordinate_pair[1][1] > coordinate_pair[0][1]:
        larger_value = coordinate_pair[1][1]
        smaller_value = coordinate_pair[0][1]
    for coordinate in range(smaller_value, larger_value + 1):
        coordinate_map[coordinate][coordinate_pair[0][0]] += 1

def find_overlapping_lines(coordinate_map):
    number_of_overlapping_lines = 0
    for row in coordinate_map:
        for number in row:
            if number > 1:
                number_of_overlapping_lines += 1
    return number_of_overlapping_lines

def display_map(coordinate_map):
    for row in coordinate_map:
        print("".join(list(map(lambda x: str(x), row))))

def challenge_2():
    coordinate_map = make_coordinate_map(1000)
    coordinates = load_coordinates()
    for coordinate_pair in coordinates:
        update_coordinate_map_include_diagonal(coordinate_pair, coordinate_map)
     
    overlapping_lines = find_overlapping_lines(coordinate_map)

    print(overlapping_lines)

def update_coordinate_map_include_diagonal(coordinate_pair, coordinate_map):
    if coordinate_pair[0][0] !=  coordinate_pair[1][0] and coordinate_pair[0][1] !=  coordinate_pair[1][1]:
        update_coordinate_map_diagonal(coordinate_pair, coordinate_map)
    elif coordinate_pair[0][0] !=  coordinate_pair[1][0]:
        update_coordinate_map_horizontal(coordinate_pair, coordinate_map)
    elif coordinate_pair[0][1] !=  coordinate_pair[1][1]:
        update_coordinate_map_vertical(coordinate_pair, coordinate_map)

def update_coordinate_map_diagonal(coordinate_pair, coordinate_map):
    start_point = coordinate_pair[0]
    end_point = coordinate_pair[1]
    if end_point[0] > start_point[0]:
        temp = start_point
        start_point = end_point
        end_point = temp
    if start_point[1] > end_point[1]:
        update_coordinate_map_diagonal_down(start_point, end_point, coordinate_map)
    if start_point[1] < end_point[1]:
        update_coordinate_map_diagonal_up(start_point, end_point, coordinate_map)

def update_coordinate_map_diagonal_up(start_point, end_point, coordinate_map):
    start_x = start_point[0]
    start_y = start_point[1]
    end_x = end_point[0]
    end_y = end_point[1]
    while start_x >= end_x and start_y <= end_y:
        coordinate_map[start_y][start_x] += 1
        start_x -= 1
        start_y += 1

def update_coordinate_map_diagonal_down(start_point, end_point, coordinate_map):
    start_x = start_point[0]
    start_y = start_point[1]
    end_x = end_point[0]
    end_y = end_point[1]
    while start_x >= end_x and start_y >= end_y:
        coordinate_map[start_y][start_x] += 1
        start_x -= 1
        start_y -= 1

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 5")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
