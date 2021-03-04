def fb():
    fizzbuzz = ''
    for i in range (1, 101):
        fizzbuzz += str(i)
        if i != 100:
            fizzbuzz += ', '

    return fizzbuzz
