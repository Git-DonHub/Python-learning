i = input("Enter a number: ")
i = int(i)
for number in range(1, i):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Buzz")
    elif number % 5 == 0:
        print("Fizz")
    else:
        print(number)


