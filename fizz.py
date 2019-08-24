def fizzbuzz():
    fizz = []
    buzz = []
    fizbuzz = []
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            fizbuzz.append(i)
            print(str(i) + " FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            fizz.append(i)
            print(str(i) + " Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            buzz.append(i)
            print(str(i) + " Buzz")
        else:
            pass
    print(fizz)
    print(buzz)
    print(fizbuzz)


fizzbuzz()

def extended_fizz_buzz(number):
    fizz = []
    buzz = []
    fizbuzz = []
    for i in range(1, number+1):
        if i % 3 == 0 and i % 5 == 0:
            fizbuzz.append(i)
            print(str(i) + " FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            fizz.append(i)
            print(str(i) + " Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            buzz.append(i)
            print(str(i) + " Buzz")
        else:
            pass
    print(fizz)
    print(buzz)
    print(fizbuzz)

extended_fizz_buzz(10000)