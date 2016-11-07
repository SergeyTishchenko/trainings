def summ(s):
    sum = 0
    mult = 1
    for i in range(len(s)):
        sum += int(s[i])
        mult *= int(s[i])
    return "Sum = {0} and multiplication = {1}".format(sum, mult)


if __name__ == '__main__':
    number = str(raw_input("Enter a number:"))
    print summ(number)