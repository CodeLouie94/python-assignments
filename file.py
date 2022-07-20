num1 = 42 # variable declaration, numbers 
num2 = 2.3 # variable declaration, numbers
boolean = True #variable declaration, Boolean
string = 'Hello World' #variable declaration, strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, array of Strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Variable declaration, object , strings, numbers, boolean
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration, array of strings
print(type(fruit)) #log statement, access value
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms')#function, add value
print(person['name'])#log statement, string of object
person['name'] = 'George' #variable declaration , string
person['eye_color'] = 'blue' #variable declaration, string
print(fruit[2]) #log statement, access value

if num1 > 45: #conditional, if
    print("It's greater") #log statement, strings
else: #conditional, else
    print("It's lower") #log statement, strings

if len(string) < 5: #conditional, if
    print("It's a short word!")#log statement, string
elif len(string) > 15:#conditional, else if 
    print("It's a long word!")# log statement, string
else: #conditional, else
    print("Just right!") # log statement, string

for x in range(5): #for loop, stop
    print(x) #log statement, number
for x in range(2,5): # for loop, start, stop
    print(x)#log statement, number
for x in range(2,10,3): #for loop, start, stop, increment
    print(x) #log statement, number 
x = 0 #variable declaration, number
while(x < 5): #while loop, stop 
    print(x) #log statement, number
    x += 1 #increment

pizza_toppings.pop() #function, delete value 
pizza_toppings.pop(1)  #function, delete value

print(person) # log statement, access value
person.pop('eye_color') # functionm, delete value
print(person) #log statement, access value

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional, if
        continue #continue
    print('After 1st if statement') #log statement, string
    if topping == 'Olives': #if, access value
        break #break

def print_hello_ten_times(): #function, parameter
    for num in range(10): #for loop, stop
        print('Hello') #log statement, string

print_hello_ten_times() #function, argument, string

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop
        print('Hello') #log statement, string

print_hello_x_times(4) #function, argument

def print_hello_x_or_ten_times(x = 10): #function, parameter
    for num in range(x): #for loop, stop
        print('Hello') #log statement, string

print_hello_x_or_ten_times() #function, argument
print_hello_x_or_ten_times(4) #function, argument


"""
Bonus section
"""

# print(num3)                               - log statement, access value
# num3 = 72                                 - variable declaration, numbers
# fruit[0] = 'cranberry'                    - function, declaration on array fruit
# print(person['favorite_team'])            - log statement, access value
# print(pizza_toppings[7])                  - log statement, access value
#   print(boolean)                          - log statement, boolean
# fruit.append('raspberry')                 - function, add value
# fruit.pop(1)                              - function, delete value

