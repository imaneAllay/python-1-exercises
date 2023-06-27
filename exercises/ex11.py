def diagonal_printer(string):
    n = len(string)
    in_space=False
    for i in range (n):
        print(' ' * i + string[i])
        

diagonal_printer("This is a test")