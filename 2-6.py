def definepersents(sentence):
    l = 0 # letters
    d = 0 # digits
    s = 0 # special symbols
    for i in range(len(sentence)):
        if sentence[i].isalpha():
            l += 1
        elif sentence[i].isdigit():
            d += 1
        else:
            s += 1
    l = round((l*100.00) / len(sentence), 2)
    d = round((d*100.00) / len(sentence), 2)
    s = round((s*100.00) / len(sentence), 2)
    return "String contains {0}% letters, {1}% digits and {2}% special symbols".format(l, d, s)


if __name__ == '__main__':
    string = str(raw_input("Enter sentence:"))
    print definepersents(string)