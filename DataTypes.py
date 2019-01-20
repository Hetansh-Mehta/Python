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

# Lists 
''' A list is a standard data type of Python which that can store sequence of values belonging to any type.
    The lists are depicted through square brackets, eg, L =[] is an empty list. 
=> Lists are mutable (modifiable) we can change the elements of a list in place.'''

L = [] # L = list() is an alternative     # This creates an emply list named L 

''' We can also create lists from sequences.
Syntax: L = list(<Sequence>) '''
print ("Lists")
l1 = list("hello")
print ("li: ",l1)
print ("----------------------------")

''' Similarities between Lists and Strings:
=> Function len(L) returns the number of items (count) in the list L    - Length
=> L[i] returns item at index i (the first item has index 0)            - Indexing
=> L[i:j] returns a new list, containing i <= objects < j               - Slicing
=> Concatenation (+) and Replication (*) is the same 
=> Individual elements can be accessed by printing L[i] where i = index (starting from 0)

    Differences between Lists and Strings:
=> Mutability: Strings are immutable where as, lists are mutable. We can change individual elements
               of a list in place. 
               L[i] = <element> 
''' 
# Example showing that Lists are mutable; This is also a way to update elements in a list
print ("Lists are mutable")
vowels = ['a', 'e', 'i', 'o', 'u']      # list of vowels 
print ("Original List: ", vowels)
vowels[0] = "A"     # Assigning "A" to index 0 of list vowel 
vowels[-4] = "E" 
print ("List Now: ", vowels)
print ("----------------------------")

# Traversing a List 
''' Traversing means accessing and processing each element of it. 
The for loop makes it easy to traverse or loop over the items in a list. '''
print ("Traversing a List")
print ("List: ", vowels)
print ("Starting traversal process:")
for i in vowels:
    print (i) 
print ("----------------------------")

# Joining Lists
''' The concatenation operator (+), when used with two lists, joins the two lists and returns
    the concatenated list. Note: Both operands must be of type List. 
Also note that when l1 + l2 is concatenated, l2 is being added to l1 and therefore all the elements 
of l2 in the new list will be AFTER the elements of l1. ''' 
print ("Joining Lists")
l2 = [1,2,3]
l3 = [4,5,6,7,8]
print ("l2+l3 = ", l2 + l3)
print ("----------------------------")

# Replicating Lists 
''' We can use * operator to replicate a list specified number of times. 
We can only use * operator when one operand is of type List and the other of type int. ''' 
print ("Replication of Lists")
print ("l2: ", l2)
print ("l2 * 3: ", l2*3)
print ("----------------------------")

# List Slicing 
''' Slices are the sub part of a list extracted out. We can use indexes of list elements to 
    create list slices.
Syntax: seq = L[start:stop:step] ''' 
# Example
print ("List Slicing")
l4 = [10,11,12,13,14,15,16,17,18,19,20]
print ("l4[0:10:2] = ", l4[0:10:2]) 
print ("l4[2:10:3] = ", l4[2:10:3])
print ("----------------------------")

# Using Slices for List Modification 
print ("Slicing used for Modification")
l5 = ["one", "two", "THREE"]
l5[0:2] = [0,1]
print ("l5[0:2] = [0,1] is : ", l5)
l5[0:2] = "a"
print ("l5[0:2] = \"a\" is : ", l5)
print ("----------------------------")

# List Manipulation 

# Appending elements to a List 
''' This is used to add elements to an existing list. The append() method adds a 
    single item to the end of the list.
Syntax: L.append(item) ''' 
print ("L.append()")
print ("l4: ", l4)
l4.append(21)

colours = ["red", "yellow", "green"]
print ("colours: ", colours)
colours.append("blue")
print ("blue is appended : ", colours)

''' We can also use a loop to append multiple items in a list: '''
l6 = []
for i in range (0,21,2):
    l6.append(i)
print ("l6: ", l6)
print ("----------------------------")

# Deleting Elements from a List
''' The del statement can be used to remove an individual item, or to remove all items identified
    by a slice 
Syntax: del List[index]              - to remove element at an index
        del List[<start> : <stop>]   - to remove elements in list slice 
''' 
print ("Deleting Elements from a List")
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print ("List1: ", list1)
del list1[10]
print ("List after deleting an element (10): ", list1)
del list1[10:15]
print ("List after deleting a slice [10:15]: ", list1)
print ("----------------------------")

# The insert method 
''' We can insert an element in between or at any position of our choice using insert().
Syntax: list.insert(<pos>, <item>)  ''' 
print ("list.insert()")
t1 = ["a", "e", "u"]
print ("Initial List: ", t1)
t1.insert(2, "i")       # inserting "i" at index = 2
print ("List after insert(): ", t1)
print ("----------------------------")

# The pop method 
''' The pop() method is used to remove an item from the list.
Syntax: list.pop(<index>) 
    index is an optional argument, if no index is specified, pop() removes and returnes 
    the last item in the list. 
'''
print ("list.pop()")
print ("list1: ", list1)
list1.pop()
print ("list1.pop() gives: ", list1)
list1.pop(0)
print ("list1.pop(0) gives: ", list1)
list1.pop(4) 
print ("list1.pop(4) gives: ", list1)
print ("----------------------------")

# The remove method 
''' The remove() method removes the first occurance of given item from the list.
Syntax: list.remove(<value>)
'''
print ("list.remove()")
list2 = [1,1,2,3,4,4,5,6,1,5,10]
print ("list2: ", list2)
list2.remove(1)
print ("list2.remove(1) gives: ", list2)
list2.remove(5) 
print ("list2.remove(5) gives: ", list2)

''' Trying to remove somehting which isn't in the list will obviously, give an error. ''' 
print ("----------------------------")

# The reverse method
''' The reverse() reverses the items in the list.
Syntax: list.reverse() ''' 

print ("list.reverse()")
print ("list1: ", list1)
list1.reverse()
print ("list1.reverse() gives: ", list1)
print ("list2: ", list2)
list2.reverse()
print ("list2.reverse() gives: ", list2)
print ("----------------------------")

# The sort method 
''' The sort() function sorts the items in a list, by default in increasing order.
Syntax: list.sort() '''

print ("list.sort()")
print ("list1: ", list1)
list1.sort()
print ("list1.sort() gives: ", list1)
''' To sort in descending order, we use: list.sort(reverse = True)
'''
print ("list2: ", list2)
list2.sort(reverse = True)
print ("list2.sort(reverse = True) gives: ", list2) 
print ("----------------------------")

# ========================================================================================================

# 4) Tuples 
''' The tuples are depicted through prentheses, ie, round brackets () 
Syntax: T = tuple() or T = () will initialize an empty tuple''' 

# Example
print ("Tuples")
t = () 
print ("t: ", t) 

''' To construct a tuple with one element, just add a comma after the single element as shown: ''' 
t1 = 3, 
print ("T1: ", t1)

''' Tuples can also be created from existing sequences. 
Syntax: T = (<sequence>)    where <Sequence> can be any kind of sequence object including strings,
                            lists and tuples. 
''' 
# Example
t2 = tuple("hello_world")       # creating a tuple from a string
print ("t2: ", t2)
l7 = ['t', 'u', 'p', 'l', 'e']  # creating a tuple from a list
t3 = tuple(l7)
print ("t3: ", t3)

''' We can also ask the user to input tuple elements: " 
'''
t4 = ()
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: ")) 
    t4 + (element,)
print ("t4: ", t4)
print ("----------------------------")

''' Tuples vs Lists: 

Similarities: 
    => len(T) returns the number of items (count) in the tuple T            - length 
    => T[i] returns the item at index i (index starting from 0)             - indexing
    => T[i:j] returns a sliced tuple containing objects between i and j     - slicing

Differences:
    => Tuples are immutable (just like strings) - their value cannot be change in place 
       whereas, lists are mutable
'''

# Traversing a Tuple 
''' Traversing a tuple means accessing and processing each element of it. The for loop makes it easy
    to traverse or loop over the items in a tuple.
Syntax: for <item> in <Tuple>:
            process each item here
'''
print ("Traversing a tuple")
print ("t3: ", t3)
print ("Starting to traverse")
for i in t3:
    print (i)

# Joining Tuples
''' We can use the + operator to concatenate two tuples. 
Again, both the operands need to be of type tuple. ''' 
tpl1 = (1,3,5)
print ("tpl1:", tpl1)
tpl2 = (6,7,8)
print ("tpl2: ", tpl2)
print ("tpl1 + tpl2 = :", tpl1 + tpl2)
print ("----------------------------")

# !!!! IMPORTANT !!!! 
''' Let's say we want to concatenate a tuple say (tpl1) with another tuple containing only one element.
    In that case, we need to write:
tpl1 + (3,)
    Or else,
    TypeError: can only concatenate tuple (not "int") to tuple
The reason for the error is: a single value is () is treated as single value not as tuple, ie, 
expressions (3) and ('a') are integer and strings respectively but (3,) and ('a',) are 
single elements typles. Thus, the expression will not give an error. 
''' 

# Repeating and Replication Tuples
''' Like strings and lists, we can use * operator to replicate a tuple specified number of times.
We can only use an integer with a * operator when trying to replicate. 
''' 
print ("Replicating Tuples (*)")
print ("tpl1 * 3 = ", tpl1 * 3)
print ("----------------------------")

# Slicing the Tuples 
''' Tuple slices, like list-slices or string slices are the sub part of the tuple extracted out.
Syntax: seq = T[start:stop:step]
''' 
print ("Tuple Slicing")
tpl3 = (10,12,14,20,22,24,30,32,34)
seq = tpl3[3:-3]
print ("seq = ", seq)
print ("----------------------------")


# Unpacking Tuples
''' Creating a tuple from a set of values is called packing and its reverse, ie, creating individual 
    values from a tuple's elements is called unpacking
Syntax: <variable1>,<variable2>,<variable3> ... = t

    where the number of variables in the left side of assignment must match the number of 
    elements in the tuple. 
'''
print ("unpacking tuples")
t5 = (1,2,'A','B')      # len(t5) = 4 and therefore, there MUST be 4 variables on the left to unpack it 
w,x,y,z = t5
print (w, "-", x, "-", y, "-", z)
print ("----------------------------")

# The len() method 
''' The len() method returns the length of the tuple, ie, the number of elements in the tuple. 
Syntax: len(<tuple>)
'''
print ("len(<tuple>)")
print ("len(t1): ", len(t1))
print ("len(t): ", len(t))
print ("----------------------------")

# The max() method 
''' This method returns the element from the tuple having maximum value. (the max value in the tuple)
Syntax: max(<tuple>)
'''
print ("The max() method")
print ("tpl3: ", tpl3)
print ("max(tpl3): ", max(tpl3))
print ("tpl1 + tpl2 = :", tpl1 + tpl2)
print ("max(tpl1+tpl2): ", max(tpl1+tpl2))
print ("----------------------------")

# The min() method 
''' This method returns the element from the tuple having minimum value (the min value in the tuple)
Syntax: min(<tuple>)
'''
print ("The min() method")
print ("tpl3: ", tpl3)
print ("max(tpl3): ", min(tpl3))
print ("tpl1 + tpl2 = :", tpl1 + tpl2)
print ("max(tpl1+tpl2): ", min(tpl1+tpl2))
print ("----------------------------")

# ========================================================================================================

# 5) Dictionaries in Python 
''' Python dictionaries are a collection of some key-value pairs. Dictonaries are:
=> mutable
=> unordered collections of elements in key:value pairs that associate keys to values. 
''' 

# Creating a Dictionary 
''' To create a dictionary, we need to include the key:value pairs in curly braces.
Syntax: <dictionary_name> = {<key>:<value>, <key>:<value>, .... , <key>:<value>}
'''
# Example 
teachers = {"Benjamin":"Physics", "Paul":"Chemistry", "Karen":"Mathematics", "Mohammed":"Legal Studies"}

''' Notice that: 
=> The curly brackets mark the beginnning and the end of the dictionary 
=> Each entry (key:value) consists of a pair separated by a comma 
=> The key and corresponding value is given by writing colon(:) between them
'''
# !!! Imp !!! => Dictionaries are indexed on the basis of keys 

# Accessing Elements of a Dictionary
''' In dictionaries, elements are accessed throught the keys defined in the key:value pairs.
Syntax: <dictionary_name> [<key>]
    Attempting to access a key that doesn't exist causes an error. 
The elements (key:value) pairs are unordered; one cannot access elements as per specific order. 
'''
print ("Accessing Elements of a Dictionary")
print ("teachers[\"Karen\"): ", teachers["Karen"])
print ("teachers[\"Paul\"): ", teachers["Paul"])
print ("----------------------------") 


# Accessing Keys or Values Simultaneously 
''' To see all the keys in a dictionary in one go, we may write: <dictionary>.keys()
    To see all the values in a dictionary in one go, we may write: <dictionary>.values() 
The keys() method returns a LIST of all the keys present in the dictionary. 
The values() method returns a LIST of all the values present in the dictionary.
'''
print ("Accessing Keys or Values Simultaneously")
vowel_dict = {"Vowel1":"a", "Vowel2":"e", "Vowel3":"i", "Vowel4":"o", "Vowel5":"u"}
print ("Vowel_dict: ", vowel_dict)
print ("vowel_dict.keys(): ", vowel_dict.keys())
print ("vowel_dict.values(): ", vowel_dict.values())
print ("teachers.keys(): ", teachers.keys())            # RETURNS A LIST OF ALL THE KEYS 
print ("teachers.values(): ", teachers.values())        # RETURNS A LIST OF ALL THE VALUES 
print ("----------------------------")

# Characteristics of a Dictionary 
''' 
=> Dictionaries are mutable : we can change the value of a certain key in place using the assignment statement
   Syntax: <dictionary>[<key>] = <value> 
=> Unordered set of key:value pairs
=> Unlike the string, list and tuple, a dictionary is not a sequence because it is unordered set of elements
=> Dictionaries are indexed by keys and its keys must be of any non-mutable type 
=> Each of the keys within a dictionary must be unique 
''' 

# Traversing a Dictionary
''' Traversal of a collection means accessing and processing each element of it. The for loop makes it easy 
    to traverse or loop over the items in a dictionary.
Syntax: for <item> in <dictionary>:
            process each item here
'''
print ("Traversing a Dictionary")
print ("teachers: ", teachers)
print ("traversing teachers: ")
for key in teachers:
    print (key, ":", teachers[key])         # print key : value 
print ("vowel_dict: ", vowel_dict)
print ("traversing vowel_dict")
for key in vowel_dict:
    print (key, ":", vowel_dict[key])
print ("----------------------------")

# Adding Elements in a Dictionary 
''' We can add new elements (key:value pairs) to a dictionary using assignment operator.
Syntax: <dictionary>[<key>] = <value> 
    BUT the key being added must not exist in dictionary and must be unique. 
    If the key already exists, then this statement will change the value of existing key and no new entry will be added.
'''
print ("Adding elements to a Dictionary")
employee_dict = {"name":"John", "salary":10000, "age":24}
print ("employee_dict: ", employee_dict)
employee_dict["dept"] = "Sales"
print ("employee_dict: ", employee_dict)
print ("----------------------------")


# Write a program to create a dictionary containing names of competition winner students as keys 
# and number of their wins as values 

n = int(input("How mane students: "))
CompWinners = {}    # Empty Dict 
for a in range (n): 
    key = input("Enter name of student: ")
    value = int(input("Number of competitions won: "))
    CompWinners[key] = value
print ("CompWinners: ", CompWinners)
print ("----------------------------")

# Deleting elements from a dictionary
''' 
=> To delete an element (key:value pair), we can use the del command. 
Syntax: del <dictionary>[<key>] 
    With del statements, the key that we are giving MUST exist in the dictionary, otherwise Python will return an error. 

=> Another method to delete elements from dict is by using pop() method.
Syntax: <dictionary>.pop(<key>) 
    The pop method will not only delete the key:value pair for the mentioned key but will also return the corresponding value. 
    pop() method also allows us to specify what to display when the given key does not exist :
Syntax: <dictionary>.pop(<new key>, "Not Found")
''' 
print ("Deleting elements from a dict")
print ("employee_dict: ", employee_dict) 
del employee_dict["age"] 
print ("employee_dict: ", employee_dict)

print ("teachers: ", teachers) 
teachers.pop("Karen")
print ("teachers: ", teachers)
teachers.pop("Hetansh", "Not Found") 
print ("teachers: ", teachers)
print ("----------------------------") 

# Checking for Existence of a Key 
''' 
Syntax: <key> in <dictionary>           returns True is key is present, otherwise False
        <key> not in <dictionary>       returns True is key is absent, otherwise False 
''' 
print ("Checking for existance of a key") 
emp1 = {"salary":10000, "name":"John", "age":29}
print ("emp1: ", emp1) 
print ("\'age\' in emp1: ", 'age' in emp1)      # True 
print ("\"John\" in emp1: ", "John" in emp1)    # False
print ("----------------------------")  

# The len() method 
''' The len() method returns the length of the dictionary, ie, the count of elements (key:value pairs) 
    in the dictionary. 
Syntax: len(<dictionary>)
'''
print ("The len() method")
print ("vowel_dict: ", vowel_dict) 
print ("len(vowel_dict): ", len(vowel_dict))
print ("----------------------------")  

# The clear() method 
''' This method removes all items from the dictionary and the dictionary becomes empty post this method. 
Syntax: <dictionary>.clear() 
'''
print ("The clear() method") 
print ("emp1: ", emp1)  
print ("emp1.clear() : ", emp1.clear()) 
print ("----------------------------")  

# The get() method 
''' With this method, we can get the item with the given key, similar to <dictionary>[<key>] 
    If the key is not present, python by default will give error, but we can specify our own message 
    through default argument. 
Syntax: <dictionary>.get(key, [default]) 
'''
print ("The get() method") 
print ("employee_dict: ", employee_dict)
print ("employee_dict.get(\"salary\"): ", employee_dict.get("salary")) 
print ("employee_dict.get(\"desig\"): ", employee_dict.get("desig", "Error, Key not found !")) 
print ("----------------------------")  
 

# The items() method 
''' This method returns all of the items in the dictionary as a sequence of (key, value) tuples, in no particular order 
Syntax: <dictionary>.items() 
'''
print ("The items() method") 
print ("employee_dict: ", employee_dict)
print ("employee_dict.items(): ", employee_dict.items())
print ("vowel_dict: ", vowel_dict) 
print ("vowel_dict.items(): ", vowel_dict.items())
print ("----------------------------")   

# The update() method 
''' This method merges key:value pairs from the new dictionary into the original dictionary, 
    adding or replacing as needed. The items in the new dictionary are added to the old one 
    and override any items already there with the same keys. 
Syntax: <dictionary>.update(<other-dictionary)
''' 
print ("The update() method")
print ("employee_dict: ", employee_dict)
print ("vowel_dict: ", vowel_dict) 
print ("vowel_dict.update(employee_dict): ", vowel_dict.update(employee_dict))
print ("----------------------------")   

# ========================================================================================================

# Write a program that reads a string and checks if it is a palindrome 

string3 = input ("Enter a string: ") 
if string3[::] == string3[::-1]:
    print ("string is palindrome")
else:
    print ("string is not a palindrome")

# ========================================================================================================


