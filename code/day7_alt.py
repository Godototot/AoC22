import sys
from helperfunc import *
from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, parent, name, size):
        self.parent = parent
        self.name = name
        self.size = size

    def __str__(self):
        return self.str_helper(0)

    @abstractmethod
    def str_helper(self, depth):
        pass


class Directory(Node):
    def __init__(self, parent, name):
        super().__init__(parent, name, 0)
        self._nodelist = []

    def get_nodes(self):
        return self._nodelist

    def add_dir(self, name):
        if not any(n.name == name and isinstance(n, Directory) for n in self._nodelist):
            self._nodelist.append(Directory(self, name))

    def add_file(self, name, size):
        if not any(n.name == name and isinstance(n, File) for n in self._nodelist):
            self._nodelist.append(File(self, name, size))
            self.increase_size(size)

    def increase_size(self, size):
        self.size += size
        if self.parent:
            self.parent.increase_size(size)

    def move(self, next_dir):
        n = next((n for n in self._nodelist if n.name == next_dir and isinstance(n, Directory)), False)
        if n is False:
            raise Exception("Directory \'"+next_dir+"\' does not exist")
        return n

    def get_size_under(self, bar):
        res = sum(d.get_size_under(bar) for d in filter(lambda n: isinstance(n, Directory), self._nodelist))
        if self.size <= bar:
            res += self.size
        return res

    def str_helper(self, depth):
        pre = "  "*depth
        return pre+'> '+self.name+'\n'+'\n'.join((n.str_helper(depth+1) for n in self._nodelist))


class File(Node):
    def __init__(self, parent, name, size):
        super().__init__(parent, name, size)

    def str_helper(self, depth):
        pre = "  "*depth
        return pre+'- '+self.name+' ('+str(self.size)+')'


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    root = Directory(None, '/')
    current_dir = root
    for l in lines[1:]:
        l_split = l.split(' ')
        if l[0] == '$':
            if 'cd' in l:
                if l_split[2] == '..':
                    current_dir = current_dir.parent
                elif l_split[2] == '/':
                    current_dir = root
                else:
                    current_dir = current_dir.move(l_split[2])
        elif l[0] == 'd':
            current_dir.add_dir(l_split[1])
        else:
            current_dir.add_file(l_split[1], int(l_split[0]))
    return root


def part1(root):
    print(root)
    return root.get_size_under(100000)


def find_smallest_dir_bigger_n(r_d, size, n):
    smallest = size
    for d in filter(lambda x: isinstance(x, Directory), r_d.get_nodes()):
        new_size = d.size
        if n < new_size:
            new_small = find_smallest_dir_bigger_n(d, new_size, n)
            if new_small < smallest:
                smallest = new_small
    return smallest


def part2(root):
    root_size = root.size
    needed_space = 30000000 - (70000000-root_size)
    return find_smallest_dir_bigger_n(root, root_size, needed_space)


def main() -> None:
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = '../input/'+'day.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
