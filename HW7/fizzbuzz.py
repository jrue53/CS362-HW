  def fb():
    fizzbuzz = ''
    for i in range (1, 101):
        if i % 3 == 0:
            fizzbuzz += 'fizz'
        elif i % 3 != 0:
            fizzbuzz += str(i)
        if i != 100:
            fizzbuzz += ', '
    
    print(fizzbuzz)
    return fizzbuzz

fb()