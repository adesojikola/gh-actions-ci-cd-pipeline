import ops


def main():
    """
    This is the main entry point of the program.
    It calls the add function from the ops module and prints the result.
    """
    try:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        print(f"The sum of {n1} and {n2} is {ops.sum(n1, n2)}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
