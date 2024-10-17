import string


def check_uppercase(password):
    return any(char in string.ascii_uppercase for char in password)


def check_length(password, min_len=8):
    return len(password) > min_len


def check_lowercase(password):
    return any(char in string.ascii_lowercase for char in password)


def check_number(password):
    return any(char in string.digits for char in password)


def check_underscore(password):
    return "_" in password


def validate_1(password):
    return all([
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_number(password),
        check_underscore(password),
    ])


def validate_2(password):
    return all([
        check_length(password, 6),
        check_uppercase(password),
        check_lowercase(password),
        check_number(password),
    ])


def validate_3(password):
    return all([
        check_length(password, 16),
        check_uppercase(password),
        check_lowercase(password),
        check_underscore(password),
    ])


def validate_4(password):
    result = []
    if not check_length(password, 8):
        result.append("Too short")
    if not check_uppercase(password):
        result.append("No uppercase letter")
    if not check_lowercase(password):
        result.append("No lowercase letter")
    if not check_number(password):
        result.append("No number")
    if not check_underscore(password):
        result.append("No underscore")

    if result:
        return result
    return True


def validation_array(password):
    return [
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_number(password),
        check_underscore(password),
    ]


def validate_5(password):
    array = validation_array(password)
    count = 0

    for x in array:
        if not x:
            count += 1

    return count <= 1
