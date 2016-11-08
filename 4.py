def delete_spases(without_spases):
    result = []
    lst = without_spases.split(" ")
    for _ in range(len(lst) - 1):
        if len(lst[_]) != 0:
            result.append(lst[_])
    return " ".join(result)

if __name__ == '__main__':
    print delete_spases('   qweqwew weqweq    weqweqw qweqweqeqw       ')
