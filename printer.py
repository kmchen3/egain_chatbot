from utils import get_choice, solved, contact_support

# Handles the initial check to make sure the printer is powered on
def printer_troubleshoot():
    print("\nIs your printer on?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])
    
    if choice == "1":
        warning_lights()

    elif choice == "2":
        print("\nTurn it on now please !")
        print("Did that fix the issue?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            connection_status()
     
# Checks for warning lights that may indicate a printer problem       
def warning_lights():
    print("\nAre there any warning lights on/blinking?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])
    
    if choice == "1":
        print("\nRead them and act accordingly based on the lights !")
        print("Did that fix the issue?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            connection_status()

    elif choice == "2":
        connection_status()

# Checks whether the user's device is properly connected to the printer
def connection_status():
    print("\nIs your device connected to the printer? (via. Bluetooth or Plug-In)")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])
    
    if choice == "1":
        sufficient_materials()

    elif choice == "2":
        print("\nConnect them please ! ")
        print("Was it successful?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            sufficient_materials()
        elif choice == "2":
            # Failed connection may indicate an issue with printer drivers
            print("\nDrivers may be outdated.")
            contact_support()
        
# Checks whether the printer has enough paper and ink to operate
def sufficient_materials():
    print("\nIs there enough materials? (i.e. ink and paper)")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])
    
    if choice == "1":
        print("\nDid that fix the issue?")
        print("1. Yes")
        print("2. No")
        
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            contact_support()

    elif choice == "2":
        print("\nRefill those components and retry.")
        print("Did that fix the issue?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            contact_support()
