def sum_of_numbers_is_7():
    result = []
    for _ in range(100, 1000):
        summ = 0
        for n in str(_):
            summ += int(n)
        if summ == 7:
            result.append(_)
    return result


if __name__ == '__main__':
    print sum_of_numbers_is_7()

