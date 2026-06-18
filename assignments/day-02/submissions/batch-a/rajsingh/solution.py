#1 Write a program to check whether a number is positive, negative, or zero.

number = float(input("Enter a number: "))     #input a number from user
if number > 0:    #check if the number is greater than zero
    print("The number is positive.")
elif number < 0:  #check if the number is less than zero
    print("The number is negative.")
else:
    print("The number is zero.")


#2 Write a program to check whether a number is even or odd.

number = int(input("Enter a number: "))         #input a number from user
if number % 2 == 0:   #check if the number is divisible by 2
    print("The number is even.")
else:
    print("The number is odd.")


#3. Create a list of 10 numbers and print each number using a loop.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     #list of 10 numbers
for n in numbers:
    print(n)

#4. Write a function named `calculate_average` that takes 3 marks and returns the average.

def calculate_average():
    #input marks of subjects from user
    hindi=int(input("Enter Hindi Marks :"))        
    english=int(input("Enter English Marks :"))
    maths=int(input("Enter Maths marks:"))
    #calculating total marks and average of the marks
    total_makrs=hindi+english+maths
    average=total_makrs/3
    return total_makrs,average    #returning total marks and average of the marks

#calling the function and storing the returnes values
average=calculate_average()
print(average)  #print the returned values
print("_"*45)


#5 Write a function named `grade_student` that prints a grade based on marks.

def grade_student():
    #input name age and marks
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    maths=float(input("Enter your maths: "))
    physics=float(input("Enter your physics: "))
    chemistry=float(input("Enter your chemistry: "))
    english=float(input("Enter your english: "))
    hindi=float(input("Enter your hindi: "))
    print("_"*45)

    #calcutating the total, average, percentage of marks
    total=maths+physics+chemistry+english+hindi
    average=total/3
    percentage=(total*100)/500

    #printing the informations
    print(name)
    print("age:=",age)
    print("maths:=",maths)
    print("total marks:",total)
    print("average marks:",average)
    print("percentage marks:",percentage)
    print("__"*45)

    ##checking the marks based on condition for printing grades
    if percentage>=90:
        print("grade a")
    elif percentage>=75:
        print("grade b")
    elif percentage>=40:
        print("grade c")
    elif percentage<40:
     print("grade f")
    if percentage>=40:
        print("pass")
    else:
        print("fail")
    print("="*45)
#callling the function
grade_student()