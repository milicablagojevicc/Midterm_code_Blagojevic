def days_between_whole_years(birthday):
    """
    Calculate the number of days passed in whole years since birth.
    :param birthday: A string in the format "DD-MM-YYYY"
    :return: The number of days between whole years since birth.
    """
    birth_year = int(birthday.split("-")[2])
    current_year = 2025
    days = 0
    for year in range(birth_year + 1, current_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days += 366
        else:
            days += 365
    return days
print(days_between_whole_years("31-07-2004"))