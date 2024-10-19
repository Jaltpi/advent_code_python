#!/usr/bin/python3


def instructions_converter(instructions: str) -> int:
    floor = 0

    if instructions:
        for i in instructions:
            if i == "(":
                floor += 1

            if i == ")":
                floor -= 1
    return floor


def quisp_to_lisp(instruction_direction: int, next_direction: int):
    if instruction_direction == next_direction:
        return instruction_direction

    return instruction_direction + next_direction


instructions_01 = "(())"
instructions_02 = "()()"

instructions_03 = "((("
instructions_04 = "(()(()("

instructions_05 = "))((((("
instructions_06 = ""

instructions_07 = "())"
instructions_08 = "))("

instructions_09 = ")))"
instructions_10 = ")())())"

instructions_01_results = instructions_converter(instructions_01)
instructions_02_results = instructions_converter(instructions_02)

instructions_03_results = instructions_converter(instructions_03)
instructions_04_results = instructions_converter(instructions_04)

instructions_05_results = instructions_converter(instructions_05)
instructions_06_results = instructions_converter(instructions_06)

instructions_07_results = instructions_converter(instructions_07)
instructions_08_results = instructions_converter(instructions_08)

instructions_09_results = instructions_converter(instructions_09)
instructions_10_results = instructions_converter(instructions_10)

first_floor_results = quisp_to_lisp(instructions_01_results, instructions_02_results)
second_floor_results = quisp_to_lisp(instructions_03_results, instructions_04_results)
third_floor_results = quisp_to_lisp(instructions_05_results, instructions_06_results)
fourth_floor_results = quisp_to_lisp(instructions_07_results, instructions_08_results)
fifth_floor_results = quisp_to_lisp(instructions_09_results, instructions_10_results)

print(f"first floor to visit:{first_floor_results}")
print(f"second floor to visit:{second_floor_results}")
print(f"third floor to visit:{third_floor_results}")
print(f"fourth floor to visit:{fourth_floor_results}")
print(f"fifth floor to visit:{fifth_floor_results}")
