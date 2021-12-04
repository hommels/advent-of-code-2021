import sys

def get_increases(nums):
    sum = 0
    for i in range(1, len(nums)):
        if int(nums[i]) > int(nums[i-1]):
            sum += 1

    return sum
    
def get_windows(nums):
    return [nums[i] + nums[i+1] + nums[i+2] for i in range(len(nums) - 2)]

def main():
    f = open("input", 'r')
    measurements = f.readlines() # [int(x) for x in f.readlines()]

    anwser1 = get_increases(measurements) 
    print(f"Part 1: {anwser1}")

    windows = get_windows(measurements)
    answer2 = get_increases(windows)
    print(f"Part 2: {answer2}")

if __name__ == '__main__':
    sys.exit(main())