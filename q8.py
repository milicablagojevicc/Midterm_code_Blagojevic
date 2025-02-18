def is_valid_url(url):
    """
    Check if the provided string is a valid URL
    A valid URL must start with 'http://' or 'https://',
    and must contain at least one dot
    :param url: The string to check for URL
    :return: True if the string is a valid URL, False otherwise
    """
    if url.startswith('http://'):
        if '.' in url[7:]:
            return True
        else:
            return False
    elif url.startswith('https://'):
        if '.' in url[8:]:
            return True
        else:
            return False
    else:
        return False

test_url_false = "vfguhjdkn"
test_url_true = "https://blackboard.ie.edu/ultra/course"
print(f"Is '{test_url_false}' a valid URL? {is_valid_url(test_url_false)}")
print(f"Is '{test_url_true}' a valid URL? {is_valid_url(test_url_true)}")