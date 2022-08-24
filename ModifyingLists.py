#In this script, we are going to be modifying a list by adding and removing items to it.

DunePlanets = ['Arrakis', 'Caladan', 'Salusa Secundus', 'Giedi Prime', 'Ix', 'Chapterhouse']
print(DunePlanets)

#The lines below edit the first item of the list, and then print the updated list.
DunePlanets[0] = 'Dune'
print(DunePlanets)

#Now we will append a new item to the end of the list.
DunePlanets.append('Grumman')
print(DunePlanets)

#now we will append into the middle of the list.
DunePlanets.insert(3, 'Corrin')
print(DunePlanets)

#Now to remove an item from the list. Damn Ixian technology...
del DunePlanets[5]
print(DunePlanets)

#new line for readability
print('\n')

#Removing an item using the pop() method
#pop() removes the last item in a list, but it lets you work with that item after remove it. 
DuneChars = ['paul', 'jessica', 'duncan', 'duke leto', 'alia', 'gurney', 'baron', 'chani']
print(DuneChars)
#this is creating a variable to hold the popped item of the list
poppedChar = DuneChars.pop()
#printing the list of characters after popping off the last one
print(DuneChars)
#printing the popped character.
print(poppedChar)

#you can specify which list item you'd like to pop off by placing the list item in the pop() parenthesis
poppedDune = DuneChars.pop(3)
print("That Bene Gesserit turbo pussy has me, " + poppedDune + ", acting a fool")

#DuneChars.remove('Baron')
too_evil = 'baron'
DuneChars.remove(too_evil)
print("\nThe " + too_evil.title() +" is too evil to be left alive!")
print(DuneChars)

DunePlanets.sort()
print(DunePlanets)