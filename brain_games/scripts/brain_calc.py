#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games')


def ask_question():
    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operation = randint(1, 3)
    if operation == 1:
        operation_sign = '+'
    elif operation == 2:
        operation_sign = '-'
    else:
        operation_sign = '*'
    expression_elements = [operand_1, operand_2, operation_sign]
    print('What is the result of the expression?')
    print(f'Question: {operand_1} {operation_sign} {operand_2}')
    return expression_elements


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def calculate(operand_1, operand_2, operation_sign):
    if operation_sign == '+':
        correct_answer = operand_1 + operand_2
    elif operation_sign == '-':
        correct_answer = operand_1 - operand_2
    else:
        correct_answer = operand_1 * operand_2
    return str(correct_answer)


def check_answer(user_answer, expression_elements, user_name):
    correct_answer = calculate(expression_elements[0],
                               expression_elements[1],
                               expression_elements[2])
    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'''"{user_answer}" is wrong answer ;(.
Correct answer was "{correct_answer}".''')
        print(f"Let's try again, {user_name}!")
        return False


def main():
    greet()
    user_name = welcome_user()
    print(f'Hello, {user_name}!')
    is_game = True
    max_count = 3
    count = 0
    while is_game:
        if count == max_count:
            print(f"Congratulations, {user_name}!")
            is_game = False
        elif count < max_count:
            expression_elements = ask_question()
            user_answer = get_answer()
            is_game = check_answer(user_answer, expression_elements, user_name)
        else:
            is_game = False
        count += 1


if __name__ == '__main__':
    main()
