def fizz_or_buzz(value):
    if value % 3 == 0:
        print("fizz")

    if value % 5 == 0:
        print("buzz")

    if value % 3 == 0 and value % 5 == 0:
        print("fizzbuzz")


for number in range(101):
    
    print(number)

    fizz_or_buzz(number)