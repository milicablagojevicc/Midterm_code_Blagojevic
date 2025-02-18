def count_c_to_jeb(text):
    """
    Count occurrences of patterns that start with 'C',
    have unlimited letters in between, and end with 'jeb'.

    :param text: The input text to search within.
    :return: The number of matches found.
    """
    count = 0
    words = text.split()
    """ 
    The for iteration in this case is used to set the conditions of the question
    Those are:
    :start = "C"
    :end = "jeb"
     """
    for word in words:
        if word.startswith('C') and word.endswith('jeb'):
            count += 1
    return count

text_example = "Chello jeb Cworldjeb Cexample jeb Ctest"
matches = count_c_to_jeb(text_example)
print(f"Number of matches: {matches}")