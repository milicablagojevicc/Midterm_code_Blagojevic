def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

## adapted code:
def palindrome(word):
    """Checks if a given string is a palindrome.
    Args:
        word (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return word == word[::-1]
numbers = ["9847255590886266818998186626880955527489",
    "1414884937242655719669145562427394884141",
    "6892149109325320763773670235239019412986",
    "6800923757255865070000705685527573290086"]
non_palindromes = [num for num in numbers if not palindrome(num)]
print("Numbers that are NOT palindromes:", non_palindromes)