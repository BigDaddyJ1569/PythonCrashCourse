personName = "Duncan Idaho"
print("Hello " + personName + ", would you like to learn some python today?")

#this line will force Duncan Idaho to be all lower case
print(personName.lower())

#this line will force Duncan Idaho to be all upper case
print(personName.upper())

#this line will force Duncan Idaho to have every word have it's first letter capitalized
print(personName.title())

#the use of \ in this quote is to tell Python to ignore the " after the escape operator, the \, that way Python doesn't think we are ending our string and will print it as quote
personQuote = "\"Dreams make good stories, but everything important happens when we’re awake.\""
print(personName + " once said, " + personQuote)