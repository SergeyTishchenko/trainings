def convert_rows_to_columns(array):
    return zip(*array)


if __name__ == '__main__':
    print convert_rows_to_columns([[1, 2, 3], [4, 5, 6]])
