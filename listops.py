num = [333, 854, 23, 105, 98, 123, 50, 1, 7, 13]

def print_list(lst):
    print("List:", lst)
    
def print_sum(lst):
    elm = sum(lst)
    print("Sum of all num:", elm)

def print_largest(lst):
    large = max(lst)
    print("Largest num:", large)

def print_smallest(lst):
    small = min(lst)
    print("Smallest num:", small)

def print_reverse_list(lst):
    reverse = lst[::-1]
    print("Num in reverse order:", reverse)
    

print_list(num)

print_sum(num)

print_largest(num)

print_smallest(num)

print_reverse_list(num)
