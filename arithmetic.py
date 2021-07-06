# Stage 2/4: Task generator
import random


class Calculator:

    def __init__(self):
        self.a = 0
        self.b = 0
        self.sign = None

    def operation(self):
        if self.sign == '+':
            return self.a + self.b
        if self.sign == '-':
            return self.a - self.b
        if self.sign == '*':
            return self.a * self.b

    def operation_square(self):
        return self.a * self.a

    def create_operation(self):
        type_operation = ['+', '-', '*']
        self.sign = random.choice(type_operation)
        self.a = random.randint(2, 9)
        self.b = random.randint(2, 9)
        return f'{self.a} {self.sign} {self.b}'

    def create_operation_square(self):
        self.a = random.randint(11, 29)
        return f'{self.a}'


def first_menu():
    while True:
        try:
            print("Which level do you want? Enter a number:")
            print("1 - simple operations with numbers 2-9")
            print("2 - integral squares of 11-29")
            option = int(input())
            if option > 2:
                print("Incorrect format.")
            else:
                break
        except ValueError:
            print("Incorrect format.")

    return option

def save_results(points, student, level):
    if level == 1:
        description = "simple operations with numbers 2-9"
    else:
        description = "integral squares 11-29"

    result_to_file = f'{student}: {points}/5 in level {level} ({description}).'

    with open("results.txt", "a") as file:
        file.write(result_to_file)


data_calc = Calculator()
mark = 0
counter = 0

op_type = first_menu()


while counter < 5:
    if op_type == 1:
        op_to_do = data_calc.create_operation()
        result = data_calc.operation()
    if op_type == 2:
        op_to_do = data_calc.create_operation_square()
        result = data_calc.operation_square()

    while True:
        print(op_to_do)
        try:
            solution = int(input())
            # result = data_calc.operation()
            if solution == result:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')

            counter += 1
            break
        except ValueError:
            print('Wrong format! Try again.')


print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')
save = input()
list_save = ['yes', 'Yes', 'y', 'YES']
if save in list_save:
    print("What is your name?")
    name = input()
    save_results(mark, name, op_type)
    print('The results are saved in "results.txt".')


