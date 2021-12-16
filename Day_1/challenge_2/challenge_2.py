def obtain_sum_of_next_three(depths, index):
    if index + 3 > len(depths):
        return False
    else:
        return depths[index] + depths[index + 1] + depths[index + 2]

def main():
    with open("input.txt", "r+") as input:
        depths = []
        for line in input.readlines():
            depths.append(int(line))
        greater_than_count = 0
        previous = False
        for index in range(len(depths)):
            sum_of_next_three = obtain_sum_of_next_three(depths, index)
            if sum_of_next_three == False:
                break
            if previous == False:
                previous = sum_of_next_three
                continue
            current = sum_of_next_three
            if current > previous:
                greater_than_count += 1
            previous = current

    print(greater_than_count)

if __name__ == "__main__":
    main()
