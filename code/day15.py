import sys
import re
from helperfunc import *


def get_manhattan_distance(a, b):
    return abs(int(a[0])-int(b[0]))+abs(int(a[1])-int(b[1]))


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    scanners = []
    beacons = []
    for l in lines:
        match = re.findall(r"x=(-?\d+), y=(-?\d+)", l)
        scanners.append((int(match[0][0]), int(match[0][1]), get_manhattan_distance(match[0], match[1])))
        beacons.append((int(match[1][0]), int(match[1][1])))
    min_x = min((sc[0]-sc[2] for sc in scanners))
    max_x = max((sc[0]+sc[2] for sc in scanners))
    return scanners, beacons, min_x, max_x


def part1(scanner_data):
    scanners, beacons, min_x, max_x = scanner_data
    scanner_coordinates = [(sc[0], sc[1]) for sc in scanners]
    y = 2000000
    counter = 0
    for i in range(min_x, max_x+1):
        if i % 1000 == 0:
            print(i)
        if (i, y) not in scanner_coordinates and (i, y) not in beacons:
            for sc in scanners:
                if get_manhattan_distance((i, y), sc) <= sc[2]:
                    counter += 1
                    break
    return counter


def get_max_in_line(scanner, y):
    return scanner[2]-abs(scanner[1]-y)+scanner[0]


def part2(scanner_data):
    scanners, beacons, min_x, max_x = scanner_data
    size = 4000000
    for y in range(0, size+1):
        x = 0
        while x <= size:
            for sc in scanners:
                if get_manhattan_distance((x, y), sc) <= sc[2]:
                    x = get_max_in_line(sc, y)+1
                    break
            else:
                return x*4000000+y
    return 'something went wrong'


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
