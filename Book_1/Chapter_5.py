cars = ['audi' , 'bmw' , 'subaru' , 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


#

car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'

car = 'Audi'
car == 'audi'

car = 'Audi'
car.lower() == 'audi'

car = 'Audi'
car.lower() == 'audi'
car

#

request_topping = 'mushrooms'

if request_topping != 'anchovies':
    print("Hold the anchovies!")

#

age = 18
age == 18

#

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


#

age = 19
age < 21

age <= 21

age > 21

age >= 21

#

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_1 = 22
age_0 >= 21 and age_1 >= 21

#

age_0 = 22
age_1 = 18
age_0 >= or age_1 >= 21

age_0 = 18
age_0 >= 21 or age_1 >= 21

#

requested_toppings = ['mushrooms' , 'onions' , 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

#

banned_users = ['andrew' , 'carolina' , 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#

game_active = True
can_edit = False

#

age = 19
if age >= 18:
    print("You are old enough to vote!")

#

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("please register to vote as soon as you turn 18!")

#

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

#

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

#

requested_toppings = ['mushrooms' , 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#

requested_toppings = ['mushrooms' , 'green peppers' , 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorri, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

#

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#

available_toppings = ['mushrooms' , 'olives' , 'green peppers' , 'pepperoni' , 'pineapple' , 'extra cheese']
requested_toppings = ['mushrooms' , 'french fries' , 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorri, we don't have " + requested_topping + ".")
print("\nFinished making yor pizza!")