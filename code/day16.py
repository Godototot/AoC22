import sys
import re
from collections import deque
from helperfunc import *


class Valve:
    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = connections
        self.paths = {}


def get_paths(source, valve_list):
    visited = set()
    visited.add(source.name)
    for c in source.connections:
        visited.add(c)
        source.paths.update({c: 1})
    next_nodes = deque(source.connections)
    while not len(next_nodes) == 0:
        current_node = next_nodes.pop()
        for c in valve_list[current_node].connections:
            if c not in visited:
                visited.add(c)
                source.paths.update({c: source.paths[current_node]+1})
                next_nodes.appendleft(c)


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    valve_list = {}
    for l in lines:
        flow_rate = int(re.search(r"\d+", l).group())
        names = re.findall(r"[A-Z][A-Z]", l)
        valve_list.update({names[0]: Valve(names[0], flow_rate, names[1:])})
    for v in valve_list:
        get_paths(valve_list[v], valve_list)
    return valve_list


def recursive_calc_pressure(start, valve_list, time):
    start_pressure_release = start.flow_rate*time
    if len(valve_list) == 0 or time <= 0:
        return start_pressure_release
    pressure = []
    for c in valve_list:
        if time-(start.paths[c]+1) >= 0:
            remaining_valve_list = {v: valve_list[v] for v in valve_list if v != c}
            pressure.append(recursive_calc_pressure(valve_list[c], remaining_valve_list, time-(start.paths[c]+1)))
    if len(pressure) == 0:
        return start_pressure_release
    return start_pressure_release+max(pressure)


def part1(valve_list):
    cleaned_valve_list = {v: valve_list[v] for v in valve_list if valve_list[v].flow_rate > 0}
    return recursive_calc_pressure(valve_list['AA'], cleaned_valve_list, 30)


def part2(input_data):
    return ''


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
