import random
def generate_random_numbers(count=10, lower_bound=1, upper_bound=100):
    """
    Generate a list of random integers in a range
    :param count: The number of random integers to generate (default is 10)
    :param lower_bound: The minimum value for the random integers (inclusive)
    :param upper_bound: The maximum value for the random integers (inclusive)
    :return: A list of randomly generated integers.
    """
    random_numbers = []
    for i in range(count):
        random_numbers.append(random.randint(lower_bound, upper_bound))
    return random_numbers
def modify_numbers(numbers):
    """
    Modify a list of numbers by replacing those > 50 with
    a random number btwn 20, 30, and replacing those >= 50 with 'XX'
    :param numbers: A list of integers to modify
    :return: A modified list where numbers greater than 50 are replaced
             with a random number between 20 and 30, and others are replaced with 'XX'
    """
    for i in range(len(numbers)):
        if numbers[i] > 50:
            numbers[i] = random.randint(20, 30)
        else:
            numbers[i] = "XX"
    return numbers
def main():
    """
    Main function to execute prog
    This function generates a list of random numbers, modifies them according
    to specified rules, and prints both the original and modified lists
    """
    original_numbers = generate_random_numbers()
    print("Original list:", original_numbers)
    modified_numbers = modify_numbers(original_numbers)
    print("Modified list:", modified_numbers)
if __name__ == "__main__":
    main()