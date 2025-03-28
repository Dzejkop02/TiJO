def find_repeated_elements(numbers, lottery):
    if numbers is None or lottery is None:
        return []

    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    result = []

    for key, value in counts.items():
        if value == lottery:
            result.append(key)

    return sorted(result)


print(find_repeated_elements([1, 1, 3, 2, 2, 2, 4, 5], 2))
