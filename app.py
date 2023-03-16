command = ""
start = False
while True:
    command = input("> ").lower()
    if command == "start":
        if start:
            print("already")
        else:
            start = True
            print(" Car started")
    elif command == "stop":
        if not start:
            print("already stopped")
        else:
            start = False
            print("car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("sorry id understand")