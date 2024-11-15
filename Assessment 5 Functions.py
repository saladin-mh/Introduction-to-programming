scale = input("Enter scale. C or F : ".lower())
num = float(int(input("Enter grades: ")))
convert_f = (num*9/5)+32
convert_c = num-32*(5/9)
if scale == 'c':
    print(convert_f,"F")
elif scale == 'f':
    print(convert_c,"C")
else:
    print("Wrong scales or degrees")





