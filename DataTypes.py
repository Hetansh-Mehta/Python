'''
    Author: Hetansh Mehta
    Date: Jan 9, 2019
    References: Computer Science with Python by Sumita Arora
    Note: The theory and the examples have been referenced from the above mentioned book. 
'''

# Data Types 
''' Data types are means to identify the type of data and associated operations of handling it.
Python Data Types:
    1) Numbers      2) Strings      3) Lists        4) Tuples       5) Dictionary
'''

# 1) Numbers 
''' The number data types are used to store numeric values in Python. 
This data type can store: integers, long integers, booleans, floating point numbers and complex numbers ''' 

# 2) Strings
''' Strings in Python are stored as individual characters in contiguous location, with two-way index 
    for each location. 
In the example below, name = "Python" is a string variable.      Accessing characters can be done by: 
       0  1  2  3  4  5       ==> forward indexing               name[0] = name [-6] = "P"      
name = P  Y  T  H  O  N                                          name[1] = name [-5] = "Y"
      -6 -5 -4 -3 -2 -1       <== backward indexing              . . . 
                                                                 name[5] = name[-1] = "N"
''' 
print ("String Index")
str1 = "PYTHON" 
print (str1)
print (str1[-1]," ", str1[5])           # All of these outputs should be the same
print (str1[-3]," ", str1[3]) 
print (str1[-5]," ", str1[1]) 
print ("----------------------------")

''' Length of a string variable can be determined using function len(<string>) 
    This returns a numerical value (length of the entire string including spaces)
'''
print ("Length of a string")
len1 = len(str1)
print ("Length of str1: ", len1) 
print ("----------------------------")

# Strings are immutable :- Item assignment not supported
''' We cannot change the individual letters of a string by assignment because strings are immutable. 
    Immutable implies non-modifiable types. '''
# Example: 
str2 = "Hello"
#str2[0] = "p"  # This will casue a TypeError which will say: 'str' object does not support item assignment

# Traversing a String
''' Traversing refers to iterating through the elements of a string, one character at a time.
This can be done through a loop." '''
# Example
print ("Traversing a string")
str3 = "Hetansh"
for ch in str3:
    print (ch, '#', end="")     # end="" ensures that the characters are printed in the same line. 
print ("\n----------------------------")

# String Operators 

# 1) String Concatenation Operator (+) 
''' The + operator creates a new string by joining the two operand strings, eg, 
"power" + "ful" will result into "powerful" 
''' 
# !!!! CAUTION !!!! 
''' The + operator HAS to have BOTH OPERANDS OF THE SAME TYPE - either of number types (for addition)
    or of string type (for concatenation). 
It cannot work with one operand as string and one as a number. ''' 

# ERROR: variables of different types cannot be combined
#print ("string type " + 123)           THIS WILL GIVE ERROR. 
print ("String operators")
print ("string type " + str(123))
print ("----------------------------")

# 2) String Replication Operator (*)
''' To use a * operator with strings, we need two types of operands - 1) String     2) Number, ie, 
    number * string     or      string * number, where the string operand tells the string to be
    replicated and the number operand tells the number of times it has to be repeated.
The * operator will not work with both operands of string types. '''
# Example
''' 3 * "Ha"    will return:    "HaHaHa" '''

# 3) Membership Operators 
''' There are two membership operators for strings:
1) in           returns True is a character or a substring exists in the fiven string; False otherwise
2) not in       returns True is a character or a substring does not exist in the given string; False otherwise 

Syntax:
<string> in <string>
<string> not in <string>
'''
print ("Membership Operators")
str4 = "Hello"
p = "a" in str4 
q = "Hel" in str4
print (p)               # False
print (q)               # True
print ("----------------------------")

# 4) Comparison Operators 
''' Comparision Operators include <, >, <=, >=, ==, != or <>) apply to strings also.
The comparisons using these operators are based on the standard character-by-character comparison
rules for ASCII. '''

print ("Comparison Operators")
print ("a" == "a")          # True 
print ("abc" == "abc")      # True
print ("a" != "abc")        # True
print ("ABC" == "abc")      # False    - remember, Python is a case sensitive language
print ("----------------------------")

''' 
=> Strings are compared on the basis of lexicographical ordering (ordering in dictionary)
=> Upper-case letters are considered smaller than the lower-case letters
Refer to the ASCII Table for further clarification.
''' 

# Determining ASCII Value of a Single Character
''' Python offers a built-in function ord() that takes a single character and returns the corresponding
    ASCII value: 
Syntax: ord(<single-character>) '''
print ("ASCII Value of a char")
print ("Order of h: ", ord('h'))
print ("Order of A: ", ord('A'), "and the order of a: ", ord('a')) 
print ("----------------------------")

''' Another built-in function chr() takes the ASCII Value in integer form and returns the character
    corresponding to that ASCII Value.
Syntax: chr(<int>)  '''
print ("Char of an ASCII Value")
print ("chr(97): ", chr(97))
print ("chr(65): ", chr(65))
print ("----------------------------")

# String Slices 
''' The term 'string slice' refers to a part of the string, where strings are sliced using a range 
    of indices. i.e, for a string say str11 we give str11[n:m] where n amd m are integers and legal indices.
    Python will return a slice of the string from n till m-1. '''
# Example
print ("String Slices")
helloStr = "Hello World"
print (helloStr[6:])
print (helloStr[4:8])
print (helloStr[:-3])
print (helloStr[3:-2])
print ("----------------------------")

# String Functions 
''' Python has many built-in functions and methods for string manipulation.
Syntax: <stringObject>.<method name>()
'''
print ("String Functions")
print ("----------------------------")
# i) string.capitalize()    returns a copy of the string with its first character capitalized.
print ("string.capitalize()")
str5 = "computer science with python"
print (str5.capitalize())
print ("----------------------------")

# ii) string.find(sub[,start[,end]])    returns the lowest indes in the string where the substring sub 
#                                       is found within the slice range or start and end.
#                                       returns -1 if sub is not found.
print ("string.find()")
string = "I love playing Soccer !"
sub1 = "playing"
print(string.find(sub1, 11, 22))              # -1 ; sub1 not in the indices provided   
print(string.find(sub1, 7, 23))
print ("----------------------------")

# iii) string.isalnum()        returns True is the characters in the string are alphanumeric (alphabets or numbers)
#                              and if there is at least one character; False otherwise
str6 = "abc123"
str7 = "123"
str8 = ""
print ("string.isalnum()")
print (str6.isalnum())      # True
print (str7.isalnum())      # True
print (str8.isalnum())      # False
print ("----------------------------")

# iv) string.isalpha()      returns True is all characters in the string are alphabetic and there is at least 
#                           one character; False otherwise
print ("string.isalpha()")
print (str6.isalpha())     # False
print (str7.isalpha())     # False
print (str8.isalpha())     # False
print ("----------------------------")

# v) string.isdigit()       returns True if all the characters in the string are digits. There must be at least 
#                           one character; False otherwise
print ("string.isdigit()")
print (str6.isdigit())  # False
print (str7.isdigit())  # True
print (str8.isdigit())  # False
print ("----------------------------")

# vi) string.isspace()     returns True if there are only whitespace characters in the string. There must be at least 
#                          one character; False otherwise
print ("string.isspace()")
str_space = " "
print (str6.isspace())          # False
print (str7.isspace())          # False
print (str8.isspace())          # False
print (str_space.isspace())     # True
print ("----------------------------")

# vii) string.islower()     returns True if all cased characters in the string are lowercase. There must be at least 
#                           one cased character; False otherwise
str9 = "ABCD"
print ("string.islower()")
print (str6.islower())      # True
print (str7.islower())      # False
print (str8.islower())      # False
print (str9.islower())      # False
print ("----------------------------")

# viii) string.isupper()    returns True if all cased characters in the string are uppercase. There must be at least 
#                           one cased character; False otherwise
print ("string.isupper()")
print (str6.isupper())      # False
print (str7.isupper())      # False
print (str8.isupper())      # False
print (str9.isupper())      # True
print ("----------------------------")

# ix) string.lower()       returns a copy of the string converted to lowercase
print ("string.lower()")
print (str6.lower())        # abc123
print (str7.lower())        # 123
print (str8.lower())        # 
print (str9.lower())        # abcd
print ("----------------------------")

# x) string.upper()        returns a copy of the string converted to upperrcase
print ("string.upper()")
print (str6.upper())        # ABC123
print (str7.upper())        # 123
print (str8.upper())        # 
print (str9.upper())        # ABCD
print ("----------------------------")

# Program that reads a line and prints the number of uppercase, lowercase, alphabets and digits 
def Line_Stats():
    print ("Inside Line_Stats()")
    line = input("Enter a line: ")
    lower_count = upper_count = 0
    digit_count = alpha_count = 0
    for a in line:
        if a.islower():
            lower_count += 1
        elif a.isupper():
            upper_count += 1
        elif a.isdigit():
            digit_count += 1
        if a.isalpha() :
            alpha_count += 1
    print ("Number of uppercase letters: ", upper_count)
    print ("Number of lowercase letters: ", lower_count)
    print ("Number of alphabets: ", alpha_count)
    print ("Number of digits: ", digit_count)
Line_Stats()
print ("----------------------------")

# Program that reads a line and a substring. It should then display the number of occurrences of the 
# given substring in the line
def Substr_Occurances():
    print ("Inside Substr_Occurances()")
    line = input("Enter a line: ")
    sub = input ("Enter substring: ")
    len_line = len(line)
    len_sub = len(sub)
    start = count = 0
    end = len_line
    while True:
        pos = line.find(sub, start, end)
        if pos != -1:
            count += 1
            start = pos + len_sub
        else:
            break 
        if start >= len_line:
            break 
    print ("Number of occurances of ", sub, " is: ", count)
Substr_Occurances()
print ("----------------------------")

# ========================================================================================================