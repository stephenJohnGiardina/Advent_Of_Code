def challenge_1():
    cave_system = load_cave_system()

    all_paths = []

    find_paths(cave_system, "start", [], all_paths)

    print(len(all_paths))

def load_cave_system():
    cave_system = {}
    with open("Day_12/input.txt", "r+") as input:
        for line in input.readlines():
            cave_1, cave_2 = line.strip().split("-")
            if cave_1 not in cave_system:
                cave_system[cave_1] = []
            if cave_2 not in cave_system:
                cave_system[cave_2] = []

            cave_system[cave_1].append(cave_2)
            cave_system[cave_2].append(cave_1)
    return cave_system

def find_paths(cave_system, cave, current_path, all_paths):
    if cave == "end":
        current_path.append(cave)
        all_paths.append(",".join(current_path))
        current_path.pop()
        return

    elif cave == cave.lower():
        if cave in current_path:
            return
    
    current_path.append(cave)
    
    for next_cave in cave_system[cave]:
        find_paths(cave_system, next_cave, current_path, all_paths)

    current_path.pop()

def challenge_2():
    cave_system = load_cave_system()

    all_paths = []

    find_paths_revisit_small_caves(cave_system, "start", [], all_paths)

    paths_only_one_small_cave_revisited = get_paths_only_one_small_cave_revisited(all_paths)

    print(len(paths_only_one_small_cave_revisited))

def find_paths_revisit_small_caves(cave_system, cave, current_path, all_paths):
    if cave == "end":
        current_path.append(cave)
        all_paths.append(",".join(current_path))
        current_path.pop()
        return

    elif cave == cave.lower():
        if cave in current_path:
            if cave == "start":
                return
            if current_path.count(cave) == 2:
                return
    
    current_path.append(cave)
    
    for next_cave in cave_system[cave]:
        find_paths_revisit_small_caves(cave_system, next_cave, current_path, all_paths)

    current_path.pop()

def get_paths_only_one_small_cave_revisited(all_paths):
    paths_only_one_small_cave_revisited = []

    for path in all_paths:
        if only_one_small_path_revisited(path):
            paths_only_one_small_cave_revisited.append(path)

    return paths_only_one_small_cave_revisited

def only_one_small_path_revisited(path):
    caves = path.split(",")
    
    visited_small_caves = []

    cave_revisited = False

    for cave in caves:
        if cave in ("start", "end") or cave != cave.lower():
            continue
        
        if cave in visited_small_caves:
            if cave_revisited:
                return False
            cave_revisited = True
        visited_small_caves.append(cave)
    
    return True

if __name__ == "__main__":
    challenge_1()
    challenge_2()