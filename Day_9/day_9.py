def challenge_1():
    height_map = load_height_map()
    low_points = find_low_points(height_map)

    risk_level = 0
    
    for row, col in low_points:
        risk_level += height_map[row][col] + 1

    print(risk_level)

def load_height_map():
    height_map = []

    with open("Day_9/input1.txt", "r+") as input:
        for line in input.readlines():

            height_map.append(list(map(lambda x: int(x), line.strip())))
    
    return height_map

def find_low_points(height_map):
    low_points = []

    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            lowest = True
            point = height_map[row][col]
            if point == 9:
                continue
            if row > 0:
                if point >= height_map[row - 1][col]:
                    lowest = False
            if row < len(height_map) - 1:
                if point >= height_map[row + 1][col]:
                    lowest = False
            if col > 0:
                if point >= height_map[row][col - 1]:
                    lowest = False
            if col < len(height_map[row]) - 1:
                if point >= height_map[row][col + 1]:
                    lowest = False
            if lowest:
                low_points.append((row, col))
    return low_points

def challenge_2():
    height_map = load_height_map()
    low_points = find_low_points(height_map)

    basin_sizes = []

    for low_point in low_points:
        basin_sizes.append(find_size_of_basin(low_point, height_map))

    print(basin_sizes)
    basin_sizes.sort()
    print(basin_sizes)
    print(basin_sizes[-3], basin_sizes[-2], basin_sizes[-1])
    print(basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1])

def find_size_of_basin(low_point, height_map):
    adjacent_points = obtain_adjacent_points(low_point, height_map)

    basin_points = set(adjacent_points)

    return len(basin_points)

def obtain_adjacent_points(low_point, height_map):
    adjacent_points = [low_point]

    row = low_point[0]
    col = low_point[1]

    point = height_map[row][col]
    if point == 8:
        return adjacent_points

    if row > 0:
        if point + 1 == height_map[row - 1][col]:
            adjacent_points += obtain_adjacent_points((row - 1, col), height_map)
    if row < len(height_map) - 1:
        if point + 1 == height_map[row + 1][col]:
            adjacent_points += obtain_adjacent_points((row + 1, col), height_map)
    if col > 0:
        if point + 1 == height_map[row][col - 1]:
            adjacent_points += obtain_adjacent_points((row, col - 1), height_map)
    if col < len(height_map[row]) - 1:
        if point + 1 == height_map[row][col + 1]:
            adjacent_points += obtain_adjacent_points((row, col + 1), height_map)

    return adjacent_points

if __name__ == "__main__":
    challenge_1()
    challenge_2()
