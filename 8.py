def find_max_value(array):
    lst = str(array).translate(None, "[] ").split(",")
    lst = map(lambda x: int(x), lst)
    return max(lst)

if __name__ == '__main__':
    print(find_max_value([[433, 231, 543], [323, 534, 577], [0, 4678, -6], [1, 5, 7]]))