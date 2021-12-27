if __name__ == "__main__":
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    ]
    while True:
        num = input("Please enter a number: ")
        if num in numbers:
            num = numbers.index(num)
        else:
            try:
                num = int(num)
            except ValueError:
                print("Invalid input, please enter valid input")
                continue
        if num == 0:
            print("Thank you for using this program")
            break
        elif num < 0 or num > 10:
            print("This is an invalid number, please enter a valid number.")
