# ake three inputs from a user, separately. Print the largest of the numbers.
num1=input('enter the first number:')
num1=int(num1)
num2=input('enter the first number:')
num2=int(num2)
num3=input('enter the first number:')
num3=int(num3)


if num1>num2 and num1>num3:
    print(num1)

elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)

# take  three inputs from a user, separately. Print the largest of the numbers.
num1=input('enter the first number:')
num1=int(num1)
num2=input('enter the first number:')
num2=int(num2)
num3=input('enter the first number:')
num3=int(num3)
num4=input('enter the first number:')
num4=int(num4)



if num1>num2 and num1>num3:
    print(num1)

elif num2>num1 and num2>num3:
    print(num2)
elif num3>num2 and num3>num1:
    print(num3)
else:
    print(num4)

#     Hint: Determine what type of data is taken in as input.
# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=input('enter the tempreture:')
temp=float(temp)
if temp>30:
    print('The tenperature is too high')
elif temp>15 and temp<=30:
    print('Normal temperature')
else:
    print('cold temperature')

# create a program that checks a users balance:
# 'insufficient  funds' if <100
# 'Moderate balance' if 100-1000
# 'High balance' if >1000
balance=input('Enter balance:')
balance=int(balance)
if balance<100:
    print('insufficient funds')
elif balance>100 and balance<1000:
    print('Moderate balance')
else:
    print('High balance')



# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=13
y=456
if x>=10 and x<=20 and y<100:
    print('conditions met')
else:
    print('conditions not met')

    # write a program that chechs
    # 'small' if number <10
    # Medium" if 10-50
    # 'large" if above 50

    c=80
    if c<10:
        print('small')
    elif c>=10 and c<=50:
        print('Medium')
    else:
        print('large')

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password='secret123'
if password == "secret123":
   print('Access granted')
else:
  print('Access denied')

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=200
attendance=90
if student_score>90 and attendance>80:
    print('Excellent student')
else:
    print("Good score, but attendance needs improvement")
    

    
