running=False
while True:
    command=input(">")
    command.lower()
    if command=='help':
        print('''
Start-to start the car
Stop-to stop the car
Quit-to quit the game 
              ''')
    elif command=='start':
        if running:
            print("Car already started")
            continue
        print("Car has started")
        running=True
    elif command=='stop':
        if not running:
            print("Car is already stopped")
            continue
        print("Car has been stopped")
        running=False
    elif command=='quit':
        print("Thank you for playing the game")
        break
    else:
        print("I don't understand what you are saying")        