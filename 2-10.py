def lensort(s):
    lst = s.split(" ")
    lst.sort(key=len)
    return " ".join (lst)


if __name__ == '__main__':
    string = str(raw_input("Enter a string:"))
    print lensort(string)
