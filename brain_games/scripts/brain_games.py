#!/usr/bin/env python3
from brain_games.cli import welcome_user


def greet():
    print("Welcome to the Brain Games!")


def main():
    greet()
    name = welcome_user()
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
