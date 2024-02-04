#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.cli import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def ask_question():
    random_number = randint(1, 1000)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_number}')
    return random_number


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def is_even(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def check_answer(user_answer, question_number, user_name):
    correct_answer = is_even(question_number)
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
            question_number = ask_question()
            user_answer = get_answer()
            is_game = check_answer(user_answer, question_number, user_name)
        else:
            is_game = False
        count += 1


if __name__ == '__main__':
    main()
