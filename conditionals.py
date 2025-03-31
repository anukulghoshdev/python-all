"""age = 21
if (age>=18):
    print("Eligible to Vote")
elif(age==19)"""


"""
light = "yellow"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("Look")
else:
    print("Light broken")
"""

"""
marks = int(input("enter your marks: "))
if(marks >= 80):
    grade = "A+"
elif(marks <= 79 and marks >= 70):
    grade = "A"
elif(marks <= 69 and marks >= 60): 
    grade = "A-"
elif(marks <= 59 and marks >= 50): 
    grade = "B"
elif(marks <= 49 and marks >= 40): 
    grade = "C"
elif(marks <= 39 and marks >= 33): 
    grade = "D"
else:
    grade = "Fail"

print("your grage is: ", grade)
"""

"""
# short hand(Ternary Operators/Conditional Expressions) - one statement
a=343
b=143
if a>b: print("a is greater than b")
# short hand - one statement(if...else)
print("a is greater than b") if a>b else print("b is greater than a")
"""

"""
# and, or, not
if a>b and c>d:
    print("")
if a>b or c>d:
    print("")
if not c>d:
    print("")
"""

"""
# Nested if
if x>10:
    print()
    if x>20:
        print("")
    else:
        print("")

"""

"""
# Find number even or odd
number = int(input("Enter a number: "))
if(number%2 == 0):
    print("number is even")
else:
    print("Odd number")
"""

"""
def checkOddEven(x):
    if(x % 2 == 0):
      # Complete the statement below
      return "Even"
    else:
        # Complete the statement below
        return "Odd"

print(checkOddEven(1))
"""


"""
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix

n = 3 
matrix = create_matrix(n)

for row in matrix:
    print(" ".join(map(str, row)))  
"""

i = 5
print(f"{i}")
print("{}".format(i))
print("loop: ",i )

