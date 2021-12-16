import os

def main():
    with open("sonar_sweep.txt", "r+") as ss:
        greater_than_count = 0
        previous = False
        for line in ss.readlines():
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
