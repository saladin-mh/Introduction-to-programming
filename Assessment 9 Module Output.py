def print_result(operation, x, y, result):
    if operation == 'add':
        operation_str = "sum"
    elif operation == 'subtract':
        operation_str = "difference"
    elif operation == 'multiply':
        operation_str = "product"
    elif operation == 'divide':
        operation_str = "quotient"
    else:
        operation_str = "result"
    print("The {operation_str} of {x} and {y} is {result}".format)
def append_to_file(operation, x, y, result, file_path='calculations.txt'):
    if operation == 'add':
        operation_str = "sum"
    elif operation == 'subtract':
        operation_str = "difference"
    elif operation == 'multiply':
        operation_str = "product"
    elif operation == 'divide':
        operation_str = "quotient"
    else:
        operation_str = "result"
    with open(file_path, 'a') as file:
        file.write("The {operation_str} of {x} and {y} is {result}\n".format)
