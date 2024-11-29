from modules.module_input import get_numbers, get_operation
from modules.module_processing import add, subtract, multiply, divide
from modules.module_output import print_result, append_to_file
def main():
    x, y = get_numbers()
    operation = get_operation()
    if operation == 'add':
        result = add(x, y)
    elif operation == 'subtract':
        result = subtract(x, y)
    elif operation == 'multiply':
        result = multiply(x, y)
    elif operation == 'divide':
        result = divide(x, y)
    else:
        result = "Invalid operation"
    print_result(operation, x, y, result)
    append_to_file(operation, x, y, result)
if __name__ == "__main__":
    main()
