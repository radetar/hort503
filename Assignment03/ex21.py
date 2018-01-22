def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLY {a} * {b}")
    return a*b

def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a /b

print("Let's do some math with numbers")

age = add(30, 5)

hieght = subtract(78, 4)

wieght = multiply(90, 2)

iq = divide (100, 2)

print(f"Age: {age}, Height: {hieght}, Weight: {wieght}, IQ: {iq}")

# a puzzle

print ("Here is a puzzle")

what = add(age, subtract(hieght, multiply(wieght, divide(iq, 2))))

print("That becomes:", what)
