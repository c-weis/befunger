import sys
from typing import List, Tuple
from collections import deque
from random import randint
from time import sleep


class Stack:
    def __init__(self):
        self.val = deque()

    def pop(self):
        if self.val:
            return self.val.pop()
        else:
            return 0

    def append(self, var: int):
        self.val.append(var)

    def __str__(self):
        return str(list(self.val))


def clear_screen():
    print("\x1b[2J", "\x1b[H")  # clear screen


def pretty_print(arr: List[List[chr]], cursor_pos: Tuple[int] = (0, 0)):
    clear_screen()
    x = cursor_pos[0]
    y = cursor_pos[1]
    for idx, row in enumerate(arr):
        if idx != y:
            print(*row, sep=' ')
        else:
            if x > 0:
                print(*row[:x], sep=' ', end=' ')
            print("\x1b[103m"+row[x]+"\x1b[0m", end=' ')
            if x < len(row)-1:
                print(*row[x+1:], sep=' ', end='')
            print()


def interpret(code: List[List[chr]],
              step_time: float = 0):
    height = len(code)
    width = len(code[0])
    PC_x = 0
    PC_y = 0

    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    directions = [RIGHT, LEFT, UP, DOWN]
    direction_string = "><^v"

    PC_dir = RIGHT

    PC_stack = Stack()

    output = ""
    output_changed = True

    running = True
    string_mode = False
    visual = (step_time > 0)

    if visual:
        pretty_print(code, (PC_x, PC_y))
        print("Stack:")
        print(PC_stack)
        sleep(step_time)

    while running:

        c = code[PC_y][PC_x]
        is_on_bridge = False

        if not string_mode:
            if c == "+":
                a = PC_stack.pop()
                b = PC_stack.pop()
                PC_stack.append(a+b)
            elif c == "-":
                a = PC_stack.pop()
                b = PC_stack.pop()
                PC_stack.append(b-a)
            elif c == "*":
                a = PC_stack.pop()
                b = PC_stack.pop()
                PC_stack.append(a*b)
            elif c == "/":
                a = PC_stack.pop()
                b = PC_stack.pop()
                PC_stack.append(b//a)
            elif c == "%":
                a = PC_stack.pop()
                b = PC_stack.pop()
                PC_stack.append(b % a)
            elif c == "!":
                if PC_stack.pop():
                    PC_stack.append(0)
                else:
                    PC_stack.append(1)
            elif c == "`":
                a = PC_stack.pop()
                b = PC_stack.pop()
                if b > a:
                    PC_stack.append(1)
                else:
                    PC_stack.append(0)
            elif c in direction_string:
                PC_dir = directions[direction_string.find(c)]
            elif c == "?":
                rand = randint(0, len(directions)-1)
                PC_dir = directions[rand]
            elif c == "_":
                if PC_stack.pop():
                    PC_dir = LEFT
                else:
                    PC_dir = RIGHT
            elif c == "|":
                if PC_stack.pop():
                    PC_dir = UP
                else:
                    PC_dir = DOWN
            elif c == "\"":
                string_mode = True
            elif c == ":":
                a = PC_stack.pop()
                PC_stack.append(a)
                PC_stack.append(a)
            elif c == "\\":
                a = PC_stack.pop()
                b = PC_stack.pop()
                PC_stack.append(a)
                PC_stack.append(b)
            elif c == "$":
                PC_stack.pop()
            elif c == ".":
                a = PC_stack.pop()
                output += str(a) + " "
                output_changed = True
                # print(a, end="")
            elif c == ",":
                a = PC_stack.pop()
                output += chr(a)
                output_changed = True
                # print(chr(a), end="")
            elif c == "#":
                is_on_bridge = True
            elif c == "g":
                y = PC_stack.pop()
                x = PC_stack.pop()
                if 0 <= y and y < height and 0 <= x and x < width:
                    PC_stack.append(ord(code[y][x]))
                else:
                    PC_stack.append(0)
            elif c == "p":
                y = PC_stack.pop()
                x = PC_stack.pop()
                v = PC_stack.pop()
                code[y][x] = chr(v)
            elif c == "&":
                a = int(input("Input integer: "))
                PC_stack.append(a)
            elif c == "~":
                a = input("Input a character (further characters ignored):")
                PC_stack.append(ord(a[0]))
            elif c == "@":
                running = False
                quit()
            else:
                number = "0123456789".find(c)
                if number != -1:
                    PC_stack.append(number)

        else:  # string_mode == True
            if c == "\"":
                string_mode = False
            else:
                PC_stack.append(ord(c))  # add value to stack as ASCII

        # Move in direction PC_dir
        step = 1
        if is_on_bridge:
            step = 2
        if PC_dir == UP:
            PC_y = (PC_y - step) % height
        elif PC_dir == DOWN:
            PC_y = (PC_y + step) % height
        elif PC_dir == RIGHT:
            PC_x = (PC_x + step) % width
        elif PC_dir == LEFT:
            PC_x = (PC_x - step) % width

        if visual:
            pretty_print(code, (PC_x, PC_y))
            print("Stack:")
            print(PC_stack)
            print("Output:")
            print(output)
        elif output_changed:
            clear_screen()
            print("Output:")
            print(output)
            output_changed = False

        if visual:
            sleep(step_time)


def code_array_from_file(filename: str) -> List[List[chr]]:
    with open(filename) as code_file:
        string = code_file.read()
    unpadded_code_array = [list(s) for s in string.splitlines()]
    max_len = max([len(row) for row in unpadded_code_array])
    return [row + [' '] * (max_len - len(row)) for row in unpadded_code_array]


def execute(filename: str = "more_or_less.bf",
            step_size: float = -1):
    step_size = float(step_size)
    code_array = code_array_from_file(filename)
    clear_screen()
    if step_size < 0:
        interpret(code_array)
    else:
        interpret(code_array, step_size)


if __name__ == "__main__":
    execute(*sys.argv[1:min(3, len(sys.argv))])
