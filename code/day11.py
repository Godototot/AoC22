import sys
import math

from helperfunc import *


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.nr_of_inspections = 0

    def take_item(self, item):
        self.items.append(item)

    def lower_worry_levels(self, threshold):
        for i in range(len(self.items)):
            self.items[i] = self.items[i] % threshold

    def inspect_items(self, sinking_worry_level=True):
        for i in range(len(self.items)):
            self.items[i] = interpret_op(self.operation, self.items[i])
            if sinking_worry_level:
                self.items[i] = math.trunc(self.items[i]/3)
            self.nr_of_inspections += 1

    def throw_items(self, monkey_list):
        while not len(self.items) == 0:
            i = self.items.pop()
            if i % self.test[0] == 0:
                monkey_list[self.test[1]].take_item(i)
            else:
                monkey_list[self.test[2]].take_item(i)


def interpret_op(operation, old):
    return eval(operation.replace('old', str(old)))


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    monkeys_strings = [lines[i:i+7] for i in range(0, (len(lines)+1), 7)]
    monkeys = []
    for m in monkeys_strings:
        items = [int(i) for i in m[1].split(': ')[1].split(', ')]
        op = m[2].split('= ')[1]
        test = (int(m[3].split(' ')[-1]), int(m[4].split(' ')[-1]), int(m[5].split(' ')[-1]))
        monkeys.append(Monkey(items, op, test))
    return monkeys


def part1(monkeys):
    for i in range(20):
        for m in range(len(monkeys)):
            monkeys[m].inspect_items()
            monkeys[m].throw_items(monkeys)
    inspections = [m.nr_of_inspections for m in monkeys]
    inspections.sort(reverse=True)
    return inspections[0]*inspections[1]


def part2(monkeys):
    threshold = math.prod([m.test[0] for m in monkeys])
    for i in range(10000):
        for m in range(len(monkeys)):
            monkeys[m].lower_worry_levels(threshold)
            monkeys[m].inspect_items(False)
            monkeys[m].throw_items(monkeys)
    inspections = [m.nr_of_inspections for m in monkeys]
    inspections.sort(reverse=True)
    return inspections[0]*inspections[1]


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
