# Write a program that displays a numbers 1 to 50 inside a list.
num=list(range(1,51))
print(num)
# From 1 above display the ones divisible by 7 or 5 inside a list.
num1=[]
for i in num:
    if i%7==0 or i%5==0:
        num1.append(i)
print(num1)
# Find sum and average of values in the range between 10 to 40.
sum=0
my_list=list(range(10,41))
for i in my_list:
    sum=sum+i
print(f"Sum: {sum}")
average=sum/len(my_list)
print(f"Average: {average}")


# Put in a list the first 10 odd numbers between 10 to 50.
odd_numbers=[]
count=0
for i in range(10,51):
    if i%2!=0:
        odd_numbers.append(i)
        count += 1
        if count == 10:
            break
print(odd_numbers)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num = int(input("Enter a number: "))
lst=list(range(1,11))
for i in lst:
    print(f"{num} x {i} = {num * i}")
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop.
even_count = 0
numbers = list(range(1, 51))
for i in numbers:
    if i % 2 == 0:
        even_count += 1
print(f"Number of even numbers between 1 and 50: {even_count}")
# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above
ls1 = [("Jay", '20'), ("Mo", '30'), ("Mya", '32')]
sum = 0
for i in ls1:
    sum=sum+int(i[1])
print(f"Total quantity: {sum}")