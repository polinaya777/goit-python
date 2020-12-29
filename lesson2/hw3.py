flag = True
while (flag):
    num_1 = input('Enter number 1: ')
    try:
        num_1 = int(num_1)
    except ValueError:
        print(f"Number {num_1} is not a number")
    else:
        flag = False

flag = True
while (flag):
    num_2 = input('Enter number 2: ')
    try:
        num_2 = int(num_2)
    except ValueError:
        print(f"Number {num_2} is not a number")
    else:
        flag = False

result = 0
flag = True
while (flag):
    oper = input('Enter operand: ')
    if oper == '+':
        result = num_1 + num_2
        print(f'Result is {result}')
        flag = False
    elif oper == '-':
        result = num_1 - num_2
        print(f'Result is {result}')
        flag = False
    elif oper == '*':
        result = num_1 * num_2
        print(f'Result is {result}')
        flag = False
    elif oper == '/':
        try:
            result = num_1 / num_2
            print(f'Result is {result}')
        except ZeroDivisionError:
            print('Number 2 could not be zero')
        flag = False
    else:
        print('This is not an operand!')
