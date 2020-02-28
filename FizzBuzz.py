for b in range (1,101):
    if b % 3==0 and b % 5==0:
        print(str(b)+": FizzBuzz")
    elif b % 3==0:
        print(str(b)+": Fizz")
    elif b % 5==0:
        print(str(b)+": Buzz")
    else:
        print(str(b)+": None")
