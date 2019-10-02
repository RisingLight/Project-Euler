def sum_multiples_of_3_and_5(limit):
    result = 0

    for number in range(3, limit):
        if ((number % 3 == 0) or (number % 5 == 0)):
            result += number

    return result

print(sum_multiples_of_3_and_5(1000))