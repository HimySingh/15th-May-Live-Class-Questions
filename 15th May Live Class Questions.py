"""
# 1 . Try to extract data from index one to index 300 with a jump of 3
n6= "this is My First Python programming class and i am learNING python string and its function"
print(n6[0:300:3])
"""

"""
# 2. Try to reverse a string without using reverse function 
n6= "this is My First Python programming class and i am learNING python string and its function"
print(n6[ : : -1])
"""

"""
# 3. Try to split a string after conversion of entire string in uppercase 
n6= "this is My First Python programming class and i am learNING python string and its function"
print(n6.upper())
print(len(n6))
print(n6[2:90:2])
print(n6[90:30:-2])
print(n6[-6:-80:-3])
"""

"""
# 4. Try to convert the whole string into lower case.
n6= "this is My First Python programming class and i am learNING python string and its function"
print(n6.lower())
"""

"""
# 5 . Try to capitalize the whole string.
n6= "this is My First Python programming class and i am learNING python string and its function"
print(n6.capitalize())
"""


"""
# 6 . Write a difference between isalnum() and isalpha().
isalnum(): Returns TRUE when the characters in " " or ' ' are the mixture of ALPHABETS AND NUMBERS, WITHOUT SYMBOLS.
isalpha(): Returns TRUE when the characters in " " or ‘ ’ are ALPHABET.  
"""

"""
# 7. Try to give an example of expand tab.
n7= "Him\tan\tshu"
print(n7.expandtabs(2))
"""

"""
# 8 . Give an example of strip , lstrip and rstrip.
n8= "    Ramanuj    "
print(n8.lstrip())
print(n8.rstrip())
print("The boy named", n8.strip(), "have a cycle.")
"""

"""
# 9.  Replace a string character by another character by taking your own example.
n6= "this is My First Python programming class and i am learNING python string and its function"
print(n6.replace("this","@THAT@"))
print(n6.replace("a", "$"))
"""

"""
# 10 . Try to give a definition of string center function with and example.
n9= "him"
print(n9.center(16,"&"))
The string center function put the string in the center of the space given in the first attribute of the function and fills the rest of the space with the character/symbol given in the 2nd attribute.
"""

"""
# 11 . Write your own definition of compiler and interpreter without copy paste form internet in your own language.
Compiler: It first scans/processes the entire source code and converts the code into machine language (0,1). This ML code is then executed by the processor. If there is an error in any line of the source code, the result will not be shown or performed by the processor.
Interpreter: It reads the source code line by line and if there is an error in a line, it stops the further scanning/processing at that point and shows that error.  
"""

"""
# 12 . Python is a interpreted or compiled language give a clear an with your understanding.
Python is a platform-independent language. Python is a complied as well as an interpreted language. In Python to convert the high-level language into a low-level language, the terms compiler comes into the picture. 
In python when we executed the program 1st the compiler converts the source code into byte and then the interpreter converts the byte code into the machine-level language.
Source code ---> compiler ---> byte code ---> interpreter ---> machine code
						(virtual machine (PVM))

In python, the process of execution is a bit different because to make it a platform-free language (we can write code once and can run on the different platforms). As the machine changed the CPU architecture also changed, so if we are writing some code on one machine it may not be executed on the other. So to resolve this problem virtual machine converts the byte code into machine code and makes it platforms independent.

"""

"""
# 13 . Try to write use cases of python with your understanding.
1. Face Detection 
2. Vehicle Number Plate Detection 
3. Stock Exchange Trading Apps that have AI for trading analysis 
4. Phone Keyboard
5. Snapchat's Bitmoji predictor
6. Google Map 
7. Airlines ticket price predicter
"""
