//Write a program that asks the user for weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram.

kg = float(input("Please enter the kilogram: "))
kg *= 2.2
print(round(kg,1))


//Write a program that asks the user to enter two numbers, x, and y, and computes | x − y | /  x+y.

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

result = (abs(x-y))/x+y

print(round(result,2))



'''Write a program that asks the user to enter three numbers (use three separate input statements).
Create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average.'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

sum_ = num1 + num2 + num3
average = (num1 + num2 + num3) / 3
print("The sum of this 3 numbers is",sum_, "\nThe average of this 3 numbers is",round(average,2))



//Print a triangle like the one below.

for i in range(0,4):
    for j in range(0,i+1):
        i+=1
        print("*", end="")
    print()


















