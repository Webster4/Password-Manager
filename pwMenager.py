# Program allows you save all your passwords from different counts
import pyperclip, sys, shelve, getpass, login


def open_file(file_name):
    """Open the file"""
    try:
        store = shelve.open(file_name)
    except IOError as e:
        print("Can not open the file ", file_name, "\n", e)
        input("\n\nPress Enter to close the program.")
        sys.exit()
    else:
        return store

def display_instruct():
    """Displaying instrution"""
    print("""
You can save your all passwords in one place and remind it whenever you need.
You have to only enter the name of your acount eg. gmail and matching password.
When you want to use menager you should write name of one of your accounts
(which was saved before) and proper password will be copied to clipboard.
    """)

def display_menu():
    """Function which displays menu, gets and returns user choice"""
    print(
    """
    MENU

    1 - copy password to clipboard
    2 - enter new to a store
    0 - exit
    """
    )

def copy_password(store):
    """Copying password to clipboard"""
    account = input("\nEnter one of your accounts: ")
    if account in store:
        pyperclip.copy(store[account])
        print("Password for " + account + " was copied to clipboard")
    else:
        print("There is no account named " + account)

def add_account(store):
    """Adding new account to own store"""
    account = input("\nEnter account to save in store: ")
    if account in store:
        print("This account is already in store.")
    else:
        password = input("Please enter password: ")
        store[account] = password
        store.sync()
        print("\nNew account has been saved.")
    return store


def main():
    account = login.open_file(".\\data\\login.dat")
    login.checking_log(account)
    account.close()
    store = open_file(".\\data\\password_data.dat")
    display_instruct()
    display_menu()
    response = None
    while response != "0":
        response = input("\nPlease choose one option: ")
        if response == "0":
            store.close()
            print("Any changes was saved. Good bye!")
        elif response == "1":
            copy_password(store)
        elif response == "2":
            store = add_account(store)
        else:
            print("Incorrect choice. Try again.")

main()


input("\n\n\nEnter to exit.")
