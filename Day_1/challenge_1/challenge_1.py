def main():
    with open("input.txt", "r+") as input:
        greater_than_count = 0
        previous = False
        for line in input.readlines():
            if previous == False:
                previous = int(line)
                continue
            current = int(line)
            if current > previous:
                greater_than_count += 1
            previous = current
    print(greater_than_count)

if __name__ == "__main__":
    main()
