# Login module which stores login and password in dat file
import getpass, shelve, sys

def open_file(file_name):
    """Open the file"""
    try:
        file = shelve.open(file_name)
    except IOError as e:
        print("Can not open the file ", file_name, "\n", e)
        input("\n\nPress Enter to close the program.")
        sys.exit()
    else:
        return file

def checking_log(account):
    if account:
        while True:
            username = input("Please enter your username: ")
            password = getpass.getpass(prompt="Please enter your password: ")
            if username in account and password in account.values():
                print("\nYou are logged")
                break
            else:
                print("\nIncorrect username or password")

    else:
        username = input("Please enter your username to create account: ")
        password = getpass.getpass(prompt="Please enter your password: ")
        account[username] = password
        account.sync()
        print("\nPassword saved")

def main():
    account = open_file(".\\login\\log2.dat")
    checking_log(account)
    account.close()
#
# main()

#
#
# input("\n\n\nEnter to exit.")

if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
