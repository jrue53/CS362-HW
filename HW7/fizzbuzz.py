def fb():
    fizzbuzz = ''
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz += 'fizzbuzz'
        elif i % 3 == 0 and i % 5 != 0:
            fizzbuzz += 'fizz'
        elif i % 5 == 0 and i % 3 != 0:
            fizzbuzz += 'buzz'
        else:
            fizzbuzz += str(i)

        if i != 100:
            fizzbuzz += ', '

    return fizzbuzz