from utils import get_choice, solved, contact_support

def wifi_flow():
    print("\nAre any lights blinking on your router?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        restart_router()

    elif choice == "2":
        print("\nIs your router powered on and plugged in?")
        print("1. Yes")
        print("2. No")
    
        choice = get_choice(["1", "2"])
    
        if choice == "1":
            check_wifi_connection()
    
        elif choice == "2":
            print("\nPlease plug in your router and turn it on.")
            print("Did this fix the issue?")
            print("1. Yes")
            print("2. No")
        
            choice = get_choice(["1", "2"])
            if choice == "1":
                solved()
            elif choice == "2":
                check_wifi_connection()


def restart_router(): # 1
    print("\nHave you tried restarting your router?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        check_wifi_connection()

    elif choice == "2":
        print("\nPlease restart your router and wait 1-2 minutes.")
        print("Try to reconnect your device to the router.")
        print("Did this fix the issue?")
        print("1. Yes")
        print("2. No")

        choice = get_choice(["1", "2"])

        if choice == "1":
            solved()
        elif choice == "2":
            check_wifi_connection()


def check_wifi_connection(): # 1 -> 1, 2 -> 1
    print("\nCan your device see the Wi-Fi network?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        check_password()

    elif choice == "2":
        print("\nTry restarting your device's Wi-Fi connection and make sure you are in range of your router")
        print("Can another device connect to the Wi-Fi?")
        check_other_devices()


def check_password():
    print("\nDid you enter the correct Wi-Fi password?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        print("\nCan another device connect to the Wi-Fi?")
        check_other_devices()

    elif choice == "2":
        print("\nPlease verify that you're using the correct password.")
        enter_the_right_password()
        
def enter_the_right_password():
    print("Did you enter the correct Wi-Fi password?")
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        print("\nCan another device connect to the Wi-Fi?")
        check_other_devices()

    elif choice == "2":
        print("\nTry again using the correct password.")
        enter_the_right_password()


def check_other_devices():
    print("1. Yes")
    print("2. No")

    choice = get_choice(["1", "2"])

    if choice == "1":
        print("\nTry disconnecting those devices and retry.")
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
        