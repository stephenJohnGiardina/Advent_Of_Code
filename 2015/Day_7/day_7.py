from datetime import datetime


def challenge_1():
    circuit = obtain_circuit()
    print("Signal provided to wire a =", obtain_signal(circuit, "a"))

def obtain_circuit():
    circuit = {}
    with open("2015/Day_7/input.txt", "r+") as input:
        for line in input.readlines():
            wire = line.strip().split("->")[-1].strip()
            operation = line.strip().split("->")[0].strip()
            circuit[wire] = operation
    return circuit

def obtain_signal(circuit, wire):
    try:
        return int(wire)
    except ValueError:
        pass
    operation = circuit[wire]
    if isinstance(operation, int):
        return operation
    if "NOT" in operation:
        circuit[wire] = obtain_signal(circuit, operation.split(" ")[1]) ^ 65535
    elif "AND" in operation:
        circuit[wire] = obtain_signal(circuit, operation.split(" ")[0]) & obtain_signal(circuit, operation.split(" ")[2])
    elif "OR" in operation:
        circuit[wire] = obtain_signal(circuit, operation.split(" ")[0]) | obtain_signal(circuit, operation.split(" ")[2])
    elif "LSHIFT" in operation:
        circuit[wire] = obtain_signal(circuit, operation.split(" ")[0]) << obtain_signal(circuit, operation.split(" ")[2])
    elif "RSHIFT" in operation:
        circuit[wire] = obtain_signal(circuit, operation.split(" ")[0]) >> obtain_signal(circuit, operation.split(" ")[2])
    else:
        circuit[wire] = obtain_signal(circuit, operation)
    return circuit[wire]

def challenge_2():
    circuit = obtain_circuit()
    wire_a_value = obtain_signal(circuit, "a")
    circuit = obtain_circuit()
    circuit["b"] = wire_a_value
    print("Signal provided to wire a when wire b value is set to value of wire a =", obtain_signal(circuit, "a"))

if __name__ == "__main__":
    print("Starting Challenges for Year 2015 Day 7")

    print("Starting Challenge 1")
    challenge_1_start_time = datetime.now()
    challenge_1()
    print("Challenge 1 complete in " + str(datetime.now() - challenge_1_start_time))

    print("Starting Challenge 2")
    challenge_2_start_time = datetime.now()
    challenge_2()
    print("Challenge 2 complete in " + str(datetime.now() - challenge_2_start_time))
