def print_fibonacci(length):

    fibonacci_list = []
    a, b = 0, 1

    for _ in range (length):
        fibonacci_list.append(a)
        a, b = b, a + b
    
    print(fibonacci_list)


        # method 2

        # Generating the Fibonacci sequence
    # for i in range(length):
    #     if i == 0:
    #         fibonacci_list.append(0)
    #     elif i == 1:
    #         fibonacci_list.append(1)
    #     else:
    #         fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    
    # # Printing the Fibonacci sequence
