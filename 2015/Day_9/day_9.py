from datetime import datetime

def challenge_1():
    cities = obtain_cities()
    shortest_path_through_all_cities = min(obtain_all_distances_through_all_cities(cities))
    print("Shortest path through all cities = ", shortest_path_through_all_cities)

class City:
    def __init__(self, name) -> None:
        self.name = name
        self.adjacent_cities = {}

    def add_adjacent_city(self, adjacent_city, distance):
        self.adjacent_cities[adjacent_city.name] = (adjacent_city, distance)

def obtain_cities():
    cities = {}
    with open("2015/Day_9/input.txt", "r+") as input:
        for line in input.readlines():
            distance = int(line.split("=")[-1].strip())
            city_1, city_2 = list(map(lambda x : x.strip(), line.split("=")[0].split("to")))
            if city_1 not in cities:
                cities[city_1] = City(city_1)
            if city_2 not in cities:
                cities[city_2] = City(city_2)
            cities[city_1].add_adjacent_city(cities[city_2], distance)
            cities[city_2].add_adjacent_city(cities[city_1], distance)
    return cities

def obtain_all_distances_through_all_cities(cities):
    all_paths = obtain_all_paths(list(cities.keys()))
    all_distances = list(map(lambda path: find_distance_of_path(cities, path), all_paths))
    return all_distances

def obtain_all_paths(city_list, current_path=[]):
    if len(city_list) == 0:
        return [current_path]
    all_paths = []
    for city_index in range(len(city_list)):
        all_paths += obtain_all_paths(city_list[0:city_index] + city_list[city_index + 1:len(city_list)], current_path + [city_list[city_index]])
    return all_paths

def find_distance_of_path(cities, path):
    total_distance = 0
    for city_index in range(len(path) - 1):
        total_distance += cities[path[city_index]].adjacent_cities[path[city_index + 1]][1]
    return total_distance

def challenge_2():
    cities = obtain_cities()
    shortest_path_through_all_cities = max(obtain_all_distances_through_all_cities(cities))
    print("Shortest path through all cities = ", shortest_path_through_all_cities)

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 9")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
                    