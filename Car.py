print('Type "help" for help')
started = False
while True:
    cmd = input('> ').lower()
    if cmd == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game
        ''')

    elif cmd == "start":
        if started:
            print("The Car is already Started!...")
        else:
            started = True
            print("The car started successfully...")
    elif cmd == "stop":
        if not started:
            print('The Car is already Stopped!...')
        else:
            started = False
            print("Car stopped...")
    elif cmd == "quit":
        break
    else:
        print("Sorry! I don't understand that...")
