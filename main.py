# romans kucerenko 211RDB275 4.grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            print("Success")
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            print("Success")
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(i)


if __name__ == "__main__":
    main()
