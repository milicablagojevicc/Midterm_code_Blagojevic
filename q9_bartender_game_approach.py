def days_between_whole_years():
    """
    Ask the user for their birthday and calculate the number of days
    passed in whole years since birth.
    :return: The number of days between whole years since birth.
    """
    while True:
        birthday = input("Enter your birthday (DD-MM-YYYY): ")

        # Validate input format
        if len(birthday) == 10 and birthday[2] == "-" and birthday[5] == "-":
            try:
                day, month, year = map(int, birthday.split("-"))
                if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                    break
                else:
                    print("Invalid date. Please enter a valid birthdate.")
            except ValueError:
                print("Invalid format. Please use DD-MM-YYYY.")
        else:
            print("Invalid format. Please use DD-MM-YYYY.")

    current_year = 2025
    days = 0
    for y in range(year + 1, current_year):
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):  # Leap year check
            days += 366
        else:
            days += 365
    print(f"Total days in whole years since your birth: {days}")

days_between_whole_years()