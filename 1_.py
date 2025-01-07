#functions are ways to wrap yyour code into reusable units 
from determineEligibility import determinElegibilityGraduate, listOfMovies
#you difne a function one time and then you can use it whenever 


# #difne a function with def 
# #only define the function once 
# #when i pass a paramater , i am passing in a place holder for future information 
# def say_hello(name,age,adress):
#     print (f'Hello {name}!')
#     print (f'How are you {name}?')
#     print (f'You are {age} years old')
#     print (f'{name} lives in {adress}')

# #call the function 
# #pass in information called an ardument 
# say_hello('Alice',22,'508 St')
# say_hello('Paul',34, '738 Pl')
# say_hello('Altair',43, '835 Ave')
# say_hello('Bob',53, '098 St')

determinElegibilityGraduate('Alice', 120, 2.0, 800)
determinElegibilityGraduate('Bob', 119, 1.9, 799)

listOfMovies('The Matrix', 10, 'action')
listOfMovies('Mufasa', 2, 'animated')

#the return statment is used to return a function and send it back to the caller 

def add(x,y):
    z = x+y
    return z

def subtract(x,y):
    z = x-
    return z

def multiply(x,y):
    z = x*
    return z

def devide(x,y):
    z = x/y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(devide(1,2))