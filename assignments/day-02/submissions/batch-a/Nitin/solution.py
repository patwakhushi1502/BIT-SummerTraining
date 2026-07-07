
# 1. Check whether a number is positive, negative, or zero

number = float(input("Enter a number: "))

if number > 0:
    print("The number is Positive.")
elif number < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


# 2. Check whether a number is even or odd

num = int(input("\nEnter an integer: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


# 3. Create a list of 10 numbers and print each number using a loop

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("\nNumbers in the list:")
for number in numbers:
    print(number)


# 4. Function to calculate average of 3 marks

def calculate_average(mark1, mark2, mark3):
    average = (mark1 + mark2 + mark3) / 3
    return average


# Example
avg = calculate_average(85, 90, 95)
print("\nAverage Marks:", avg)


# 5. Function to print grade based on marks

def grade_student(marks):
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")


# Example
grade_student(avg)