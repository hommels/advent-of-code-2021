def part1(data):
    h_pos = 0
    depth = 0
    for command, str_units in lines:
        units = int(str_units)
        if command == "forward":
            h_pos += units
        elif command == "up":
            depth -= units
        elif command == "down":
            depth += units

    return h_pos * depth

def part2(data):
    aim = 0
    h_pos = 0
    depth = 0
    for command, str_units in lines:
        units = int(str_units)
        if command == "forward":
            h_pos += units
            depth += aim * units
        elif command == "up":
            aim -= units
        elif command == "down":
            aim += units

    return h_pos * depth


with open("input", 'r') as f:
    lines = [x.split() for x in f]

print(f"Part 1: {part1(lines)}")
print(f"Part 2: {part2(lines)}")
