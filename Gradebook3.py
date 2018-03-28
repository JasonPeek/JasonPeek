grade_list = []

math_grade = int(input("what is your math grade?: "))
science_grade = int(input("what is your science grade?: "))
english_grade = int(input("what is your english grade?: "))
computer_grade = int(input("what is your computer grade?: "))
extra_grade = int(input("what is your extra class grade?: "))

grades = math_grade, science_grade, english_grade, computer_grade, extra_grade

grade_list.append(grades)
print (grade_list)
average = (sum)(grades)/5
print ("Your average grade is:")
print (average)

if average >= 90:
    print ("Great job")
elif average >= 80:
    print ("doing good")
elif average >= 70:
    print ("try harder")
elif average >= 60:
    print ("You can do better")
else:
    print ("YOU FAIL")
