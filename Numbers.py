# Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so
# on. Python treats numbers in several different ways, depending on how
# they are being used. Let’s first look at how Python manages integers,
# because they are the simplest to work with.

#Simple addition, results in 5
equation1 = 2 + 3
print(equation1)

#Simple subtraction, results in 10
eq2 = 19 - 9
print(eq2)

#Simple multiplication, results in 100
eq3 = 4 * 25
print(eq3)

#Simple division, results in a float of 5.5
eq4 = 11 / 2
print(eq4)

#Python does support PEMDAS, so it will solve the division first then perform the addition
eq5 = 69 + 34/22
print(eq5)


#A Lesson on avoiding Type errors within the str() function
#
#Line 35 will display the error on line 31 because you cannot cat an int into a string. It will produce a type error.
#
#Exception has occurred: TypeErrorcan only concatenate str (not "int") to str
#
#
age = 21
#message = "Happy " + age + "st birthday!"
message = "Happy " + str(age) + "st birthday!"
print(message)
