def is_palindrom(string):
    lst = list(string)
    lst.reverse()
    if string == "".join(lst):
        return True
    else:
        return False

if __name__ == '__main__':
    print is_palindrom("qwertyuiopoiuytrewq")
    print is_palindrom('404')
    print is_palindrom('304')
