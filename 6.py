def add_numbers_to_zero_sum(array):
    element = sum(array)
    array.append((0 - element))
    return array

if __name__ == '__main__':
        print add_numbers_to_zero_sum([9, -9, 8, 1])
