
from wifi import wifi_flow
from computer import computer_status
from bluetooth import bluetooth_flow
from printer import printer_troubleshoot
from other import other_please_explain
from utils import get_choice, display_menu

# main()
def main():
    print("\nHello! I'm your Customer Service Chatbot.")
    print("Given the options below, what issues are you encountering?\n")

    while True:
        display_menu()

        choice = get_choice(["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            wifi_flow()

        elif choice == "2":
            computer_status()
        
        elif choice == "3":
            bluetooth_flow()
            
        elif choice == "4":
            printer_troubleshoot()
            
        elif choice == "5":
            other_please_explain()
             
        else: #elif choice == "6"
            print("\nThank you for using the chatbot! Hope this helped :)")
            break


if __name__ == "__main__":
    main()