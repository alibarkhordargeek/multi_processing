import threading
from time import sleep

def clean(places):
    sleep(2)
    for place in range(0, len(places)):
        print(f'The {places[place]} cleaned!')
    print('party is cleaned!!!')

def invite(people):
    for person in range(0, len(people)):
        print(f'Hi {people[person]} you are invited to the party!!!')
    print(f'{len(people)} people had invited')

def drink(drink_names):
    sleep(3)
    for drink in range(0, len(drink_names)):
        print(f'We bought {drink_names[drink]} for the party!')
    print(f'totally bought {len(drink_names)} drinks for the party!')

thrdd_clean = threading.Thread(target = clean, name = 'cleaning', daemon = False, args = (['yard', 'back yard', 'floor', 'balconi'], ))
thrdd_invite = threading.Thread(target = invite, name = 'invitng', daemon = False, args = (['ali', 'abalfazl', 'alex', 'ahmad', 'azadeh', 'arman', 'abbas'], ))
thrdd_drink = threading.Thread(target = drink, name = 'drinks', daemon = False, args = (['tomoto juice', 'orange juice', 'limonade', 'mojito', 'pomegranate juice'], ))

# runnig function clean & drink with threds
thrdd_clean.start()
thrdd_drink.start()
# joining clean & drink together
thrdd_clean.join()
thrdd_drink.join()
# after finishing the functions clean & drink, starts running the function invite
thrdd_invite.start()