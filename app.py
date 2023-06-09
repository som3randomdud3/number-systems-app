class BibleNumber:
    base = 10
    digit_symbols = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
    }

    def __init__(self, value):
        self.value = value % self.base

    def __repr__(self):
        return self.digit_symbols[self.value]

    def __add__(self, other):
        if isinstance(other, BibleNumber):
            return BibleNumber(self.value + other.value)
        elif isinstance(other, int):
            return BibleNumber(self.value + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, BibleNumber):
            return BibleNumber(self.value - other.value)
        elif isinstance(other, int):
            return BibleNumber(self.value - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, BibleNumber):
            return BibleNumber(self.value * other.value)
        elif isinstance(other, int):
            return BibleNumber(self.value * other)
        else:
            return NotImplemented


class QuranNumber:
    base = 7
    digit_symbols = {
        0: "٠",
        1: "١",
        2: "٢",
        3: "٣",
        4: "٤",
        5: "٥",
        6: "٦",
    }

    def __init__(self, value):
        self.value = value % self.base

    def __repr__(self):
        return self.digit_symbols[self.value]

    def __add__(self, other):
        if isinstance(other, QuranNumber):
            return QuranNumber(self.value + other.value)
        elif isinstance(other, int):
            return QuranNumber(self.value + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, QuranNumber):
            return QuranNumber(self.value - other.value)
        elif isinstance(other, int):
            return QuranNumber(self.value - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, QuranNumber):
            return QuranNumber(self.value * other.value)
        elif isinstance(other, int):
            return QuranNumber(self.value * other)
        else:
            return NotImplemented


class GitaNumber:
    base = 18
    digit_symbols = {
        0: "०",
        1: "१",
        2: "२",
        3: "३",
        4: "४",
        5: "५",
        6: "६",
        7: "७",
        8: "८",
        9: "९",
        10: "१०",
        11: "११",
        12: "१२",
        13: "१३",
        14: "१४",
        15: "१५",
        16: "१६",
        17: "१७",
    }

    def __init__(self, value):
        self.value = value % self.base

    def __repr__(self):
        return self.digit_symbols[self.value]

    def __add__(self, other):
        if isinstance(other, GitaNumber):
            return GitaNumber(self.value + other.value)
        elif isinstance(other, int):
            return GitaNumber(self.value + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, GitaNumber):
            return GitaNumber(self.value - other.value)
        elif isinstance(other, int):
            return GitaNumber(self.value - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, GitaNumber):
            return GitaNumber(self.value * other.value)
        elif isinstance(other, int):
            return GitaNumber(self.value * other)
        else:
            return NotImplemented


def run_interactive_program():
    print("Welcome to the Number Systems Interactive Program!")

    while True:
        print("\nSelect a number system:")
        print("1. Bible Number")
        print("2. Quran Number")
        print("3. Gita Number")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Thank you for using the Number Systems Interactive Program!")
            break

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            continue

        if choice == 1:
            number_system = BibleNumber
        elif choice == 2:
            number_system = QuranNumber
        elif choice == 3:
            number_system = GitaNumber
        else:
            print("Invalid choice. Please enter a valid number.")
            continue

        value1 = input("Enter the first number: ")
        try:
            value1 = int(value1)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        value2 = input("Enter the second number: ")
        try:
            value2 = int(value2)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        num1 = number_system(value1)
        num2 = number_system(value2)

        print("Result:")
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")


run_interactive_program()
