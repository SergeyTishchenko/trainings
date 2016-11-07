def lenth(s):
    lst = s.split(" ")
    arr = []
    for i in range(len(lst)):
        arr.append(len(lst[i]))
    return " ".format(min(arr))


if __name__ == '__main__':
    string = str(raw_input("Enter text:"))
    print lenth(string)