#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: June 2021
# This program calculates the average of inputted marks

def average_of_marks(marks):
    # this function finds the average of the marks
    total = 0
    for counter in marks:
        total += counter
    average = int(total / len(marks))

    return average


def main():
    # this function receives input and calls a function

    # declaration
    marks = []

    print("Enter one mark at a time (in %). Enter '-1' to stop.")  # output
    try:
        # input
        temp_mark = int(input("Enter a mark (in %): "))
        if temp_mark != -1:
            marks.append(temp_mark)
            while temp_mark != -1:
                temp_mark = int(input("Enter a mark (in %): "))
                if temp_mark == -1:
                    break
                marks.append(temp_mark)
            # output and function call
            average = average_of_marks(marks)
            print("The average is {0}\nDone.".format(average))
        else:
            print("No marks were entered\nDone.")
    except(Exception):
        print("Invalid Input\nDone.")


if __name__ == "__main__":
    main()
