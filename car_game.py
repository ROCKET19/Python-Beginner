start_status = False
stop_status = False

while True:
    msg = input('> ')
    if msg.lower() == 'help':
        print('''
Start - to start the car
Stop - to stop the car
Quit - to quit the game
''')
    elif msg.lower() == 'start':
        if start_status:
            print("Car is already Started")
        else:
            start_status = True
            print("Car is ready to go!")
    elif msg.lower() == 'stop':
        if stop_status:
            print("Car is already Stopped")
        else:
            stop_status = True
            print('Car Stopped!')
    elif msg.lower() == 'quit':
        break;
    else:
        print("I do not understand that. Type 'help' to get help")


