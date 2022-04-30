def task4_pairs(num_list, target):
    count = 0
    buf = sorted(num_list.copy())
    while buf[0] < target:
        count += len([y for y in buf if y == target - buf[0]])
        buf.pop(0)
    return count