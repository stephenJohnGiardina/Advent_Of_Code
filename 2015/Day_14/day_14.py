import os
from datetime import datetime


def challenge_1():
    all_reindeer = obtain_all_reindeer()
    for reindeer in all_reindeer:
        reindeer.travel_distance(2503)
    fastest_reindeer = max(all_reindeer, key = lambda reindeer: reindeer.current_distance)
    print(
        "The reindeer that traveled the furthest after 2053 seconds was",
        fastest_reindeer.name,
        "with a distance of",
        fastest_reindeer.current_distance
        )

class Reindeer:
    def __init__(self, name, speed, endurance, rest_required):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.rest_required = rest_required
        self.traveling = True
        self.current_endurance = endurance
        self.current_rest_required = 0
        self.current_distance = 0
        self.points = 0

    def travel_distance(self, time_traveled):
        for second in range(time_traveled):
            if self.traveling:
                self.current_distance += self.speed
                self.current_endurance -= 1
                if self.current_endurance == 0:
                    self.current_rest_required = self.rest_required
                    self.traveling = False
            else:
                self.current_rest_required -= 1
                if self.current_rest_required == 0:
                    self.current_endurance = self.endurance
                    self.traveling = True

def obtain_all_reindeer():
    all_reindeer = []
    with open(os.path.join("2015", "Day_14", "input.txt"), "r+") as input:
        for line in input.readlines():
            name = line.split(" ")[0]
            speed = int(line.split(" ")[3])
            endurance = int(line.split(" ")[6])
            rest_required = int(line.split(" ")[-2])
            all_reindeer.append(Reindeer(name, speed, endurance, rest_required))
    return all_reindeer

def challenge_2():
    all_reindeer = obtain_all_reindeer()
    for second in range(2503):
        for reindeer in all_reindeer:
            reindeer.travel_distance(1)
        for winning_reindeer in obtain_winning_reindeer(all_reindeer):
            winning_reindeer.points += 1
    winning_reindeer = max(all_reindeer, key = lambda reindeer: reindeer.points)
    print(
        "The reindeer that obtained the most points after 2053 seconds was",
        winning_reindeer.name,
        "with a score of",
        winning_reindeer.points
        )

def obtain_winning_reindeer(all_reindeer):
    winning_reindeer = []
    max_distance = max(all_reindeer, key = lambda reindeer: reindeer.current_distance).current_distance
    for reindeer in all_reindeer:
        if reindeer.current_distance == max_distance:
            winning_reindeer.append(reindeer)
    return winning_reindeer

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 14")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
