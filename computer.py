from utils import get_choice, solved, contact_support

def computer_status():
    print("\nIs your computer fully charged or plugged in?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])
    
    if choice == "1":
        hold_power_button()

    elif choice == "2":
        print("\nPlease do so now.")
        print("Did that fix the issue?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            computer_response()
        
        
def hold_power_button():
    print("\nDid you hold the power button?")
    print("1. Yes")
    print("2. No")
    
    choice = get_choice(["1", "2"])
    
    if choice == "1":
        computer_response()
        
    elif choice == "2":
        print("\nPlease hold the power button down for 10 seconds.")
        print("Did that fix the issue?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            computer_response()
        
        
def computer_response():
    print("\nDoes anything turn on? Ex. Does the fan turn on? Does the keyboard light up?")
    print("1. Yes")
    print("2. No")
    
    choice = get_choice(["1", "2"])
    
    if choice == "1":
        print("\nThis could be a hardware issue. Check the device for any damages and if there are any present, get them fixed by a professional soon. ")
        print("Inspection is needed or contact support for future information.")
        print("As a final attempt, try WINDOWS KEY + CTRL + SHIFT + B (all at once) to reset your video drivers.")
        print("Did this fix the issue?")
        print("1. Yes")
        print("2. No")
        
        choice = get_choice(["1", "2"])
        
        if choice == "1":
            solved()
        elif choice == "2":
            contact_support()
        
    elif choice == "2":
        contact_support()
    
