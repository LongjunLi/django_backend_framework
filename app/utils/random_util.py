import random
import string


def generate_random_string(length):
    letters = string.ascii_uppercase + string.digits
    return "".join(random.choice(letters) for _ in range(length))


def generate_random_string_separately(length, sep_number):
    result = ""
    for _ in range (sep_number):
        result = result + generate_random_string(length) + "-"
    return result[:-1]


def generate_random_string_with_category(length, category):
    return category + "-" + generate_random_string(length)


def generate_random_string_separately_with_category(length, category, sep_number):
    result = category + "-"
    for _ in range (sep_number):
        result = result + generate_random_string(length) + "-"
    return result[:-1]
