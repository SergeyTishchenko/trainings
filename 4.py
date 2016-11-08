def delete_spases(without_spases):
    result = []
    lst = without_spases.split(" ")
    for i in range(len(lst) - 1):
        if len(lst[i]) != 0:
            result.append(lst[i])
    return " ".join(result)

if __name__ == '__main__':
    print delete_spases('   qweqwew weqweq    weqweqw qweqweqeqw       ')
