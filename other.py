from utils import get_choice, solved, contact_support

def other_please_explain():
    print("\nPlease describe the issue you're experiencing.")

    issue = input("> ").strip().lower()

    while issue == "":
        print("\nPlease enter a brief description of your issue.")
        issue = input("> ").strip().lower()

    if "wifi" in issue or "wi-fi" in issue or "internet" in issue or "router" in issue:
        print("\nYour issue sounds related to a Wi-Fi connection.")
        print("Please try the 'Wi-Fi won't connect' troubleshooting option or contact support directly through https://www.egain.com/contact-us/.")

    elif "computer" in issue or "laptop" in issue or "pc" in issue or "power" in issue:
        print("\nYour issue sounds related to a computer startup problem.")
        print("Please try the 'Computer doesn't turn on' troubleshooting option or contact support directly through https://www.egain.com/contact-us/.")

    elif "bluetooth" in issue or "headphones" in issue or "speaker" in issue or "mouse" in issue or "keyboard" in issue:
        print("\nYour issue sounds related to Bluetooth.")
        print("Please try the 'Bluetooth not connecting' troubleshooting option or contact support directly through https://www.egain.com/contact-us/.")

    elif "printer" in issue or "print" in issue or "paper" in issue or "ink" in issue:
        print("\nYour issue sounds related to your printer.")
        print("Please try the 'Printer won't print' troubleshooting option or contact support directly through https://www.egain.com/contact-us/.")

    else:
        print("\nThank you for providing the details.")
        print("It doesn't seem like it matches any of our options and you will need assistance")
        print("Please send the following information to our technical support team:")
        print(f'"{issue}"')
        print("\nWe will review your issue and assist you further.")
        print("https://www.egain.com/contact-us/")
        exit()
    