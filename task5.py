def task5_names(names):
    list_of_names = sorted([tuple(one.split(':')[::-1]) for one in names.upper().split(';')])
    result = ''
    for item in list_of_names:
        result += f'({item[0]}, {item[1]})'
    return result