import os
from datetime import datetime


def challenge_1():
    syntaxes = load_syntaxes()

    syntax_scores = []

    for syntax in syntaxes:
        syntax_scores.append(get_syntax_score(syntax))

    print(sum(syntax_scores))

def load_syntaxes():
    syntax = []

    with open(os.path.join("2021", "Day_10", "input.txt"), "r+") as input:
        for line in input:
            syntax.append(line.strip())
        
    return syntax

def get_syntax_score(syntax):
    first_illegal_character = get_first_illegal_character(syntax)

    if first_illegal_character == ")":
        return 3
    if first_illegal_character == "]":
        return 57
    if first_illegal_character == "}":
        return 1197
    if first_illegal_character == ">":
        return 25137
    return 0

def get_first_illegal_character(syntax):
    stack = []

    for char in syntax:
        if char in ("(", "[", "{", "<"):
            stack.append(char)
        else:
            if char == ")":
                if stack[-1] != "(":
                    return ")"
            if char == "]":
                if stack[-1] != "[":
                    return "]"
            if char == "}":
                if stack[-1] != "{":
                    return "}"
            if char == ">":
                if stack[-1] != "<":
                    return ">"
            stack.pop()

def challenge_2():
    syntaxes = load_syntaxes()

    incomplete_syntaxes = []

    for syntax in syntaxes:
        if get_syntax_score(syntax) == 0:
            incomplete_syntaxes.append(syntax)

    incomplete_scores = []

    for incomplete_syntax in incomplete_syntaxes:
        incomplete_scores.append(get_incomplete_score(incomplete_syntax))

    incomplete_scores.sort()

    print(incomplete_scores[len(incomplete_scores) // 2])

def get_incomplete_score(incomplete_syntax):
    completion_string = get_completion_string(incomplete_syntax)

    completion_score = 0

    for char in completion_string:
        completion_score *= 5
        if char == ")":
            completion_score += 1
        if char == "]":
            completion_score += 2
        if char == "}":
            completion_score += 3
        if char == ">":
            completion_score += 4

    return completion_score
    
def get_completion_string(incomplete_syntax):
    stack = []

    for char in incomplete_syntax:
        if char in ("(", "[", "{", "<"):
            stack.append(char)
        else:
            stack.pop()
    
    completion_string = ""

    for char in list(reversed(stack)):
        if char == "(":
            completion_string += ")"
        if char == "[":
            completion_string += "]"
        if char == "{":
            completion_string += "}"
        if char == "<":
            completion_string += ">"
    
    return completion_string

if __name__ == "__main__":
    print("Starting Challenges for Year 2021 Day 10")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
