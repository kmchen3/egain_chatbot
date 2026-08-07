
def get_choice(valid_choices):
    """
    Gets validated input from the user.
    Handles empty and invalid inputs.
    """
    while True:
        choice = input("> ").strip()

        if choice == "":
            print("\n Please enter a response.\n")
            continue

        if choice not in valid_choices:
            print(f"\n Invalid option. Please choose {', '.join(valid_choices)}.\n")
            continue

        return choice

# Displays the main menu and available troubleshooting categories
def display_menu():
    print("~" * 26)
    print(" Customer Service Chatbot")
    print("~" * 26)
    print("1. Wi-Fi won't connect")
    print("2. Computer doesn't turn on")
    print("3. Bluetooth not connecting")
    print("4. Printer won't print ")
    print("5. Other (Please Explain) ")
    print("6. Exit\n")

# Confirms that the user's issue has been resolved and ends the chatbot
def solved():
    print("\nYay! I'm glad I could help resolve this issue.")
    print("\nI shall leave you to it, if you need any more help in the future, I'd love to chat :)")
    exit()
    
# Directs the user to additional technical support when the chatbot cannot resolve the issue
def contact_support():
    print("\nSorry, this issue may require additional technical support, please contact us !!")
    print("https://www.egain.com/contact-us/")
    print("\nReturning you to main menu . . .")
