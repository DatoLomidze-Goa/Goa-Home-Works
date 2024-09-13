#Codewarks Homework

#Homework 1:

#Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

#Examples:

#1: -1
#14: -14
#-34: 34

#def opposite(number):
#   return -number


#Homework 2:

#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

#def bool_to_word(bool):
   # return "Yes" if bool else "No"

#Homework 3:

#Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

#Examples (input -> output)
6, "I"     -> "IIIIII"
#5, "Hello" -> "HelloHelloHelloHelloHello"



#def repeat_str(repeat, string):
    #return repeat * string

#Homework 4:

#Make a simple function called greet that returns the most-famous "hello world!".

#Style Points
#Sure, this is about as easy as it gets. But how clever can you be to create the most creative "hello world" you can think of? What is a "hello world" solution you would want to show your friends?

#def greet():
    #return "hello world!"

#Homework 5:

#Your task is to create a function that does four basic mathematical operations.

#The function should take three arguments - operation(string/char), value1(number), value2(number).
#The function should return result of numbers after applying the chosen operation.

#Examples(Operator, value1, value2) --> output

#('+', 4, 7) --> 11
#('-', 15, 18) --> -3
#('*', 5, 5) --> 25
#('/', 49, 7) --> 7

#def basic_op(operator, value1, value2):
   #if operator=='+':
     # return value1+value2
    #if operator=='-':
     # return value1-value2
   #if operator=='/':
     # return value1/value2
   #if operator=='*':
     # return value1*value2