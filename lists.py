#The line below offers a Inexhaustive list of the planets of Dune.
DunePlanets = ['Arrakis', 'Caladan', 'Salusa Secundus', 'Giedi Prime', 'Ix', 'Chapterhouse']

#this print statement will print the entire list, including the syntax.
#print(DunePlanets)

#this print statement will only print the first element of the above list, without any additional syntax.
print(DunePlanets[0])
print('\n')

#These print statements show that there are more than 1 way to print the last item in a list.
print(DunePlanets[5])
print(DunePlanets[-1])
#printing some new line characters to give it some space.
print('\n')

message = "The atriedes come from " + DunePlanets[1] + "."
print(message)