limit = 1000
counter = 1

while counter <= limit:
    if counter % 15 == 0:
        print("Fizzbuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    
    counter += 1
    