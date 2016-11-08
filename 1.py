def is_natural(n):
    if n % 3 == 0 and n % 10 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print is_natural(10)
    print is_natural(100)
    print is_natural(66)
    print is_natural(55)
    print is_natural(600)
    print is_natural(-60)





