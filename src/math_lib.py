def max_fun(digits):
    if not digits:
        return None

    result = digits[0]

    for number in digits:
        if number > result:
            result = number

    return result


def is_perfect(digit):
    if not digit:
        return False

    if digit <= 0:
        return False

    d = []

    for num in range(1, digit):
        if digit % num == 0:
            d.append(num)

    return sum(d) == digit

