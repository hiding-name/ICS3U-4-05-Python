#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program adds only positive numbers

import random


def main():
    # funciton adds positive numbers

    # variables
    repeater = 0
    addNumber = 0
    answer = 0
    exception = False

    # Welcome statement
    print("Welcome, I will add all positive integers you enter.")
    input("Press Enter to continue.")

    try:
        number = int(input("\nHow many numbers to add: "))
        # process
        for repeater in range(number):
            # input
            addNumber = int(input("\nEnter a number: "))
            if addNumber < 0:
                continue
            else:
                answer = answer + addNumber
    except ValueError:
        exception = True
        print("Invalid input.")

    if exception is False:
        print("\nThe answer is " + str(answer) + ".")


if __name__ == "__main__":
    main()
