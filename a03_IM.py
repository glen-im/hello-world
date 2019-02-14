# Name: Im, Heung Yong (Glen)
# RedID: 823395723
# Date: Feb 13
# PyCharm debugging tools

#Q1
# Wtire a program that will evaluate 3 numeric exam grades
# Return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

exam_one = int(input('Input exam grade one: '))
exam_two = int(input('Input exam grade two: '))
exam_three = int(input('Input exam grade three: ')) # '3 -> three' to synchronize with the name of the variable down.

grades = [exam_one, exam_two, exam_three] # list should be divided by comma
sum = 0

for grade in grades: # indicating the list 'grades'
     sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70: #
    letter_grade = 'C'
elif avg >= 65:
    letter_grade = 'D'
else:
    letter_grade = 'F'

for grade in grades:
    print('Exam: ' + str(grade))

print('Avergage: ' + str(avg))
print('Grade: ' + str(letter_grade))

if letter_grade is 'F':
    print('Student is failing.')
else:
    print('Student is passing.')

#Q2
patients = [[175.8, 73.4], [180.2, 59.5], [165.4, 70.2], [193.5, 70.0]]
#height = [patients[0][0], patients[1][0], patients[2][0]]
#weight = [patients[0][1], patients[1][1], patients[2][1]]
bmi = 0

def calculate_bmi(height, weight): #index from the list
    return weight / ((height / 100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 25.0:
        return 'normal weight'
    elif bmi < 30:
        return 'overweighting'
    else:
        return 'obesity'

for patient in patients:
    height = patient[0]
    weight = patient[1]
    bmi = calculate_bmi(height, weight)
    bmi_category = get_bmi_category(bmi)
    print("Patient's BMI is : {} ({})".format(bmi, bmi_category))

#Q3
num3 = input('Numeric Value: ')
    try:
        float(num3)
    except Exception as e:
        print('{} is not a numeric value.'.format(e))

#Q4
def divide(dividend, divisor):
    try:
        print(int(dividend) / int(divisor))
    except ZeroDivisionError:
        print('Divided by zero error')

dividend = input('input dividend:')
divisor = input('input divisor:')
divide(dividend, divisor)

#Q5
