length = int(input("Enter the size of the pattern: "))
iteration_count = length

while iteration_count:

    for _ in range(length):
        print("*", end="")

    print()
    iteration_count -= 1
