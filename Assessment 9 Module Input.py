def get_numbers():
    x = float(input("First number: "))
    y = float(input("Second number: "))
    return x, y
def get_operation():
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    return operation
