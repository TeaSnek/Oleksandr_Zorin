def task3_numbers(number):
    if len(str(number)) == 1:
        return number
    else:
        return task3_numbers(sum([int(x) for x in str(number)]))