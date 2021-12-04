import sys

def count_increases(nums):
    total = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            total += 1

    return total

def main():
    with open("input", 'r') as f:
        data = [int(x) for x in f.readlines()]

    part1 = count_increases(data) 
    print(f"Part 1: {anwser1}")

    windows = [sum(data[i:i + 3]) for i in range(len(data) - 2)]
    part2 = count_increases(windows)
    print(f"Part 2: {answer2}")

if __name__ == '__main__':
    sys.exit(main())