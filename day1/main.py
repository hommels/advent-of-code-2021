import sys

def get_increases(nums):
    total = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            total += 1

    return total
    

def main():
    with open("input", 'r') as f:
        measurements = [int(x) for x in f.readlines()]

    anwser1 = get_increases(measurements) 
    print(f"Part 1: {anwser1}")

    windows = [sum(measurements[i:i + 3]) for i in range(len(measurements) - 2)]
    answer2 = get_increases(windows)
    print(f"Part 2: {answer2}")

if __name__ == '__main__':
    sys.exit(main())