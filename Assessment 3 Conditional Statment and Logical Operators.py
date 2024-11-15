note = int(input("Enter the student notes: "))
if note >= 70 and note <= 100:
    grade = "A"
elif note >= 60 and note <=70:
    grade = "B"
elif note >= 50 and note <=60:
    grade = "C"
elif note >= 40 and note <=50:
    grade = "D"
elif note >= 30 and note<=40:
    grade = "E"
elif note >= 20 and note <=30:
    grade = "F"
else:
    grade = "Please, enter a valid notes (from 0 up to 100)"
print("This notes intitle you to grade:", grade)



