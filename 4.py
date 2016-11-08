def delete_spaces(source):
    string = source.split(' ')
    targer_string = ''
    double_space = False
    for word in string:
        if word == '' and double_space == True:
            continue
        if word == '':
            targer_string = targer_string + ' '
            double_space = True
            continue

        targer_string = targer_string + word
        double_space = False
    return targer_string


if __name__ == '__main__':
    source = ' rwrwr   543  gfdfgdf    '
    print delete_spaces(source)

