def while_fun(z,a):

    i=0
    numbers = []

    while i < z:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + a
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

        print("The numbers: ")

        for num in numbers:
            print(num)



while_fun(7,2)
