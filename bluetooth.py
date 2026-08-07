from utils import get_choice, solved, contact_support

# Handles the initial Bluetooth troubleshooting question
def bluetooth_flow():
    print("\nIs Bluetooth turned on for both devices?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        in_range()
        
    elif choice == "2":
        print("\nTurn them on now !")
        print("Did this fix the issue?")
        print("1. Yes")
        print("2. No")
        
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            prev_pairing()
            
# Checks whether the devices are close enough to connect
def in_range():
    print("\nAre you in range?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        prev_pairing()
        
    elif choice == "2":
        print("\nGet in range please!")
        print("Did this fix the issue?")
        print("1. Yes")
        print("2. No")
        
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            prev_pairing()
    
# Determines whether the devices have been paired previously
def prev_pairing():
    print("\nHas it been paired before?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        disconnect_reconnect()
        
    elif choice == "2":
        on_off_device()
        
# Attempts to resolve pairing issues by reconnecting the device
def disconnect_reconnect():
    print("\nTry disconnecting and reconnecting your device. (Forget Device)")
    print("Did this fix the issue?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        solved()
        
    elif choice == "2":
        on_off_device()
    
# Restarts the device as a final troubleshooting step
def on_off_device():
    print("\nTry turning the device off and on. (Restart device)")
    print("Repeat the steps above after your device has been restarted.")
    print("Did this fix the issue?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        solved()
        
    elif choice == "2":
        contact_support()
