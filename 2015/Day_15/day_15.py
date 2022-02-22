import os
from datetime import datetime


def challenge_1():
    ingredients = obtain_ingredients()
    total_score = 0
    all_quantities = obtain_all_quantities(0)
    for quantities in all_quantities:
        ingredients_and_quantities = (
            (ingredients[0], quantities[0]),
            (ingredients[1], quantities[1]),
            (ingredients[2], quantities[2]),
            (ingredients[3], quantities[3]),
            )
        current_score = obtain_total_score_of_cookie(ingredients_and_quantities)
        if current_score > total_score:
            total_score = current_score
    print("The total score of the cookie with the highest possible total score =", total_score)

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

def obtain_ingredients():
    ingredients = []
    with open(os.path.join("2015", "Day_15", "input.txt"), "r+") as input:
        for line in input.readlines():
            name = line.split(" ")[0][:-1]
            capacity = int(line.split(" ")[2][:-1])
            durability = int(line.split(" ")[4][:-1])
            flavor = int(line.split(" ")[6][:-1])
            texture = int(line.split(" ")[8][:-1])
            calories = int(line.split(" ")[10])
            ingredients.append(Ingredient(name, capacity, durability, flavor, texture, calories))
    return ingredients

def obtain_all_quantities(current_sum, current_quantities=[]):
    if len(current_quantities) == 4:
        if sum(current_quantities) == 100:
            return [current_quantities]
        return []
    quantities = []
    for quantity in range(1, 100):
        if current_sum + quantity > 100:
            break
        quantities += obtain_all_quantities(current_sum + quantity, current_quantities + [quantity])
    return quantities

def obtain_total_score_of_cookie(ingredients_and_quantities):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    for ingredient, quantity in ingredients_and_quantities:
        capacity += quantity * ingredient.capacity
        durability += quantity * ingredient.durability
        flavor += quantity * ingredient.flavor
        texture += quantity * ingredient.texture
    if capacity < 0:
        capacity = 0
    if durability < 0:
        durability = 0
    if flavor < 0:
        flavor = 0
    if texture < 0:
        texture = 0
    total_score = capacity * durability * flavor * texture
    if total_score < 0:
        return 0
    return total_score

def challenge_2():
    ingredients = obtain_ingredients()
    total_score = 0
    all_quantities = obtain_all_quantities(0)
    for quantities in all_quantities:
        ingredients_and_quantities = (
            (ingredients[0], quantities[0]),
            (ingredients[1], quantities[1]),
            (ingredients[2], quantities[2]),
            (ingredients[3], quantities[3]),
            )
        current_score = obtain_total_score_of_cookie(ingredients_and_quantities)
        if obtain_calories_of_cookie(ingredients_and_quantities) == 500:
            if current_score > total_score:
                total_score = current_score
    print(
        "Of the cookies that are 500 calories, the total score of the cookie with the highest possible total score =",
        total_score
        )

def obtain_calories_of_cookie(ingredients_and_quantities):
    total_calories = 0
    for ingredient, quantity in ingredients_and_quantities:
        total_calories += quantity * ingredient.calories
    return total_calories

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 15")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
