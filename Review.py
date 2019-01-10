'''
 Author: Hetansh Mehta
 Date: Jan 8, 2019
 References: Computer Science with Python - Sumita Arora
 Note: The theory and the examples have been referenced from the above mentioned book.
       Please use this file only for learning purposes. 
''' 

# Tokens: 
''' Tokens are the smallest individual unit in a program. They are also called Lexical Unit.
    1) Keywords     2) Identifiers (Names)      3) Literals
    4) Operators    3) Punctuators 
are a few tokens in Python. ''' 

# Keywords 
''' Keywords are the words that convey a special meaning to the language compiler/interpreter. 
    These are reserved for special purpose and cannot be used as normal identifier names.
Example: False, None, True, and, as, except, finally, import, for, while, ... etc. '''

# Identifiers (Names)
''' Identifiers are user defined names which are given to different parts of the program viz.
    variables, objects, classes, functions, lists, dictionaries, etc. 
The Identifier MUST: (rules of defining identifiers)
    1) Start with a letter (A to Z or a to z) or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).
    2) Punctuation Characters cannot be used within identifiers. '''

# Python is a case sensitive programming language.

# Literals
''' Literals (constant-values) are the data items that have fixed value.
    1) String Literals      2) Numeric Value        3) Boolean Literals
    4) None (special literal)                     
are a few literals in python. '''

# String Literals
''' A string literal is a sequence of characters surrounded by quotes (single or double).
Example: "hello", 'hi', "Python" '''



# Numeric Literals
''' The numeric literals can be of the following four types:
 1) int     : integers with are whole numbers (no decimal points)       Eg: 4, 10
 2) long    : are integers of inlimited size                            Eg: 9834478416901973516325
 3) float   : represents real numbers - contains decimal numbers        Eg: 852.8813
 4) complex : are of the form a ± bj, where a and b are floats and j represents the imaginary number. '''

# Boolean Literals
''' It is used to represent one of the two Boolean values, i.e., 
    True (Boolean true or 1) or False (Boolean false or 0) '''

# Operators
''' Tokens that perform special computation when applied to variables and other objects in an expression.
    Variables and objects to which the computation is applied, are called operands.
    Operators + Operands = Expression
Arithmetic Operators:
    Addition(+), Subtraction (-),       Multiplication (*),         Division (/)
    Remainder/Modulus (%),              Exponent (**),              Floor Division (//)
Logical Operators
    Logical AND (and), Logical OR (or) 
Relational Operators:
    Less than (<),          Greater than (>),           Less than or equal to (<=),         Greater than or equal to (>=)
    Equal to (==),          Not equal to (!=) or (<>),  
Assignment Operator:
    Assignment (=),         Assign Quotient (/=),       Assign sum (+=),                    Assign product (*=),
    Assign remainder (%=),  Assign difference (-=),     Assign exponent (**=),              Assign Floor Division (//=)          
'''

# 1) Variables 2) FUnctions , user defined 3) scope of variables 4) modules 5) loops and conditionals 

# ==============================================================================================================
# Variables 
# Declare a variable and initialize it
a = 10
print ("a = ", a)
print ("------------------------------")
stu = "Hetansh"
print (stu)
print ("------------------------------")
# Dynamic Typing: A variable pointing to a value of a certain type, can be made to point to a value/object
#                 of different type. 
x = 20
print ("x = ", x)
x = "Hello World"
print ("x after dynamic typing = ", x)
print ("------------------------------")
# Run and check output.

# Multiple Assignment of Variables
e = f = g = 10
print ("e,f,g = ", e,f,g)
h,i,j = 10, 20, 30
print ("h,i,j = ", h,i,j)
print ("------------------------------")
# Swapping two variables
a,e = i,j 
print ("a after swap: ", a)
print ("e after swap: ", e)
print ("------------------------------")
# ERROR: variables of different types cannot be combined
#print ("string  " + 123)
print ("string  " + str(123))
print ("------------------------------")

del a,x,e,f,g,h,i,j 

# Asking the user for integer input
number1 = int(input("Enter a number: "))
print ("number1: ", number1)
print ("------------------------------")
# Asking the user for float input
number2 = float(input("Enter a float: "))
print ("number2: ", number2)
print ("------------------------------")
# Asking the user for string input
string1 = input ("Enter a string: ")
print ("string1: ", string1)
print ("------------------------------")
# ==============================================================================================================

# Functions 
''' Functions are little self-contained programs that perform a specific task, which one can incorporate
    into larger programs by invoking them when needed.
Functions are broadly used for breaking down a problem into smaller parts. Functions also beautify the code. '''

#1) Built-in Functions:
''' These are pre-defined functions and are always available for use.
Example: int(), len(), type() '''
#example: 
length_string1 = len(string1)   #variable holding the lenght
print ("Length of entered string1 is: ", length_string1)

# Functions defined in modules:
''' These functions are pre-defined in particular modules and can only be used when the corresponding module
    is imported.'''

# User defined functions; 
''' A function in Python is defined as per the following Syntax:'''
#Synatx: 
'''
def <function name> ([parameters]):
    <statement>
    [<statements>]

*) A function may or may not return a value, A function returning value are also known as fruitful functions. 
   And a function that does not return a value is known as void function or a non-fruitful function.
*) A function that returns a value must be printed when called : print (function_name) 
'''

# Arguments and Parameters
''' Arguments are the values that are being passed in the function call statement.
    Parameters are the values being reveived in the function header. 
    (More clear in the examples that follow) '''

# EXAMPLES
# define a basic function
def func1():
  print ("Function1")

# function that takes arguments
def func2(arg1, arg2):                          # arg1, arg2 are called parameters (passed in function header)
  print (arg1, " ", arg2)

# function that returns a value
def square(x):
  return x*x                                    # Remember: function returning a value must be printed when it is called 

# Invoking functions
''' A function is called (or invoked, or executed) by providing the function name, followed by the 
    values being sent enclosed in parentheses (arguments - passed in function call)
When a function that does not return anything is printed, it returns "None". 
'''

func1()     #calling func1
print (func1)   #should return None as it does not return anything in the function definition 
func2(10,2)
print (square(4))   #prints the returned value after calculating the sqauare
print ("------------------------------")
# ==============================================================================================================
# Scope of a Variable
''' A variable declared in the top level segment of a program is said to have a global scope and is 
    usable inside the whole program and all blocks (functions, other blocks) contained within the program.
A variable declared in a function-body is said to have local scope i.e, it can be used only within this
function and the other blocks contained under it. It cannot be used outside the block in which it is defined.'''
# Example: 
def calSum(x,y):
    z = x+y                 # x, y are only defined inside the calSum function. Local variables which cannot be used outside
    return z 
num1 = float(input("Enter first number: "))         # num1, num2 are global variables and can be used anywhere inside the code
num2 = float(input("Enter second number: "))
sum = calSum(num1, num2)
print ("Sum of given numbers is: ", sum)
print ("------------------------------")
# ==============================================================================================================
 
# Conditionals 
''' A conditional is a statement set which is executed on the basis of result of a condition.'''

# The if statement
# Syntax:
''' if <conditional expression1>:
        statement
        [statements]
    elif <conditional expression2>:
        statement
        [statements]
    .
    .
    .
    else:
        statement
        [statements]
'''
# Write a program to read a number. If the number is even, print half the number otherwise print the next number.
def OddEven(n):
    if (n%2==0):
        print ("The given number is even")
        print ("The half-number is: ", (n/2))
    else:
        print ("The number is odd")
        print ("The next number is: ", n+1)
n = int(input("Enter a number: "))
OddEven(n)
print ("------------------------------")

# Write a progrom to compute tax payable by a person according to his salary. 
def Tax_Calculator():
    salary = int(input("Enter salary: "))
    if (salary < 10000):
        tax = 0.00 * salary
    elif (salary < 20000):
        tax = 0.05 * salary
    elif (salary <40000):
        tax = 0.10 * salary
    else:
        tax = 0.12 * salary
    print ("You must pay: ", tax, " as taxes")
Tax_Calculator()
print ("------------------------------")

# Write a function that prints "Buzz" if the number is divisible by 3, "Fizz" if the number is divisible
# by 5 and "FizzBuzz" if the number is divisible by both. The entered number should be a positive number
# less than 100.
def Divisible(n):
    if (n>0 and n<100):
        if (n%3==0 and n%5==0):
            print ("FizzBuzz")
        else:
            if (n%3==0):
                print ("Buzz")
            elif (n%5==0):
                print ("Fizz")
            else:
                print ("Number not divisible by 3 or 5 or both!")
    else:
        print ("Error: Please enter a number between 0 and 100")

num = int(input("Enter a number: "))
Divisible(n)
print ("------------------------------")
# ==============================================================================================================

# Loops
''' Python provides two kinds of loops: 
1) for loop: to represent a counting loop
2) while loop: tp represent a conditional loop 
    The block of code under these loop run again and again until a condition is met. '''

# 1) The for loop
''' Primirarily designed to process the items of any sequence, such as a list or a string, one by one.'''

# Syntax:
''' for <variable> in <sequence>:
        statements_to_repeat
    
    OR                          

    for <variable> in range(start, stop, step):
        statements_to_repeat 
'''
# Example
for x in range(5,10):           # x = variable and sequence is the list of numbers 5 <= num < 10. 
    print (x)                   # Notice that the loop runs till x=9 and terminates when x=10. 
print ("------------------------------")

# Program to print out even numbers till 10
for i in range(0,10,2):
    print (i)
print ("------------------------------")

# Program to print cubes of numbers in the range 15 to 20
for i in range(15,21):
    print("Cube of number: ", i, "is: ", i**3)
print ("------------------------------")

# use a for loop over a collection
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days:
    print (d)
print ("------------------------------")


# 2) The while loop
''' A while loop is a conditional loop that will repeat the instructions within itself as long
    as a conditional remains true (Boolean True or truth value true).'''
# Syntax:
''' while <logicalExpression>:
        loop-body
'''
# Example
while (x < 5):                  # The loop will run until the condition x<5 remains true.
    print (x)
    x = x + 1
print ("------------------------------")
# ==============================================================================================================

# Jump Statements - break and continue
''' The jump statements - break and continue can be used within the loop to jump out of loop iterations. '''

# The break statement
''' A break statement terminates the rest of the loop and jumps over to the statement following the loop.'''

# Example
a = b = c = 0
for i in range(1,21):
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    if b==0:
        print ("Division by zero error! Aborting")
        break 
    else:
        c = a/b 
    print ("Quotient: ", c) 
print ("------------------------------")

# The continue statement
''' The continue statement skips the rest of the loop statements and causes the next iteration of 
    the loop to take place. '''

# Example
for i in "PYTHON":
    if i== "T":             # When i=T, it skips the loop and jumps to the next iteration and the loop runs
        continue            # Try this with a break statement and compare the output
    else:           
        print (i)
print ("------------------------------")

# Example of break and continue 
for x in range(5,20):
    if (x == 17):                       
        break
    if (x % 2 == 0): 
        continue
    print (x)
print ("------------------------------")
# ==============================================================================================================

