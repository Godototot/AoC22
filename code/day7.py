import sys
from helperfunc import *


class Dir:
    def __init__(self, outer_dir, name):
        self.outer_dir = outer_dir
        self.name = name
        self._dir_list = []
        self._files = []
        self.size = 0

    def get_inner_dir(self):
        return self._dir_list

    def add_dir(self, name):
        if not any(d.name == name for d in self._dir_list):
            self._dir_list.append(Dir(self, name))

    def add_file(self, name, size):
        if not any(f[0] == name for f in self._files):
            self._files.append((name, size))
        self.increase_size(size)

    def increase_size(self, file_size):
        self.size += file_size
        if self.outer_dir:
            self.outer_dir.increase_size(file_size)

    def move(self, next_dir):
        n = next((d for d in self._dir_list if d.name == next_dir), False)
        if n is False:
            raise Exception("Directory \'"+next_dir+"\' does not exist")
        return n

    def get_size_under(self, bar):
        res = sum(d.get_size_under(bar) for d in self._dir_list)
        if self.size <= bar:
            res += self.size
        return res

    def __str__(self):
        return self.str_helper(0)

    def str_helper(self, depth):
        pre = "  "*depth
        out = pre+"> "+self.name+'\n'
        for d in self._dir_list:
            out += d.str_helper(depth+1)
        for f in self._files:
            out += pre+'  - '+f[0]+' ('+str(f[1])+')\n'
        return out


def prepare_input(input_file):
    lines = read_input_lines(input_file)
    root = Dir(None, '/')
    current_dir = root
    for l in lines[1:]:
        l_split = l.split(' ')
        if l[0] == '$':
            if 'cd' in l:
                if l_split[2] == '..':
                    current_dir = current_dir.outer_dir
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
    return root.get_size_under(100000)


def find_smallest_dir_bigger_n(r_d, size, n):
    smallest = size
    for d in r_d.get_inner_dir():
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
        input_file = '../input/'+sys.argv[0][:-3]+'.txt'
    if sys.argv[1] == '1':
        print(part1(prepare_input(input_file)))
    elif sys.argv[1] == '2':
        print(part2(prepare_input(input_file)))
    else:
        raise Exception("Please clarify, which part you wanna execute.")


if __name__ == '__main__':
    main()
