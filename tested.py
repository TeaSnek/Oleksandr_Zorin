def ifint(x):
    return isinstance(x, int)


def task1_filter(filter_list):
    return list(filter(ifint, filter_list))


def task2_letter(string):
    for letter in string:
        if string.upper().find(letter.upper()) == string.upper().rfind(letter.upper()):
            return letter


def task3_numbers(number):
    if len(str(number)) == 1:
        return number
    else:
        return task3_numbers(sum([int(x) for x in str(number)]))


def task4_pairs(nlist, target):
    count = 0
    buf = nlist.copy()
    buf.sort()
    x = buf.pop(0)
    while x < target:
        for y in buf:
            if x + y == target:
                count += 1
        x = buf.pop(0)
    return count


def task5_names(names):
    list_of_names=[]
    for one in names.upper().split(';'):
        list_of_names.append(tuple(one.split(':')[::-1]))
    list_of_names.sort()
    result = ''
    for item in list_of_names:
        result += f'({item[0]}, {item[1]})'
    return result



if __name__ == '__main__':
    a = [1, 2, 'a', 'b', 33, 4]
    b = 'stresS'
    s = "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(task1_filter(a))
    print(task2_letter(b))
    print(task3_numbers(493193))
    print(task4_pairs([1, 3, 6, 2, 2, 0, 4, 5], 5))
    print(task5_names(s))
