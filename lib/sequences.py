def print_fibonacci(length):
    fibonacci_list = []
    
    if length <= 0:
        print([])
        return
    
    #  first two numbers in the sequence

    if length >= 1:
        fibonacci_list.append(0)
        print(fibonacci_list[0])
    
    # Generating the remaining numbers in the sequence
    