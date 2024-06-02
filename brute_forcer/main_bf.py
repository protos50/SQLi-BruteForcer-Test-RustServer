import os
from brute_forcer import BruteForcer
from colorama import  Style, Fore

# Name of Users and Passwords list
users_file_name = "usernames.txt"
passwords_file_name = "passwords.txt"
    
   
def menu_header():
    """
    Prints a visually appealing header for the brute-forcer menu.

    Includes the program's name, version, and a disclaimer about its intended usage.
    """

    print(Style.BRIGHT + Fore.GREEN)
    print("*******************************************************")
    print("*                                                     *")
    print("*       Bruteforcer v1.0 by Franco Joaquin Zini       *")
    print("*        Coded to only be used on local hosts.        *")
    print("*                                                     *")
    print("*******************************************************")
    print(Style.RESET_ALL)

def menu_body(bf):
    """
    Displays the main body of the brute-forcer menu.

    Args:
        bf (BruteForcer): An instance of the BruteForcer class, or None if a URL hasn't been provided yet.

    Prints the current login URL (if available), a list of available menu options, and prompts the user for input.
    """

    print("Current LOGIN URL: " + Fore.LIGHTBLUE_EX + (bf.url if bf is not None else "None") + Style.RESET_ALL)
    print("\n[1] Enter login URL")
    print("[2] Find valid user")
    print("[3] Perform brute force attack")
    print("[4] Print results")
    print("[5] Save credentials in a JSON file")
    print("[6] Exit")

def enterURL_option():
    """
    Prompts the user to enter the login URL and creates a BruteForcer instance.

    Returns:
        BruteForcer: A new instance of the BruteForcer class, initialized with the provided URL, username file, and password file.
    """

    url = input("\n>>> Please enter the login URL: ")
    return BruteForcer(url, users_file_name, passwords_file_name)
 

def find_username_option(bf):
    """
    Attempts to find valid usernames using the existing BruteForcer instance.

    Args:
        bf (BruteForcer): The BruteForcer instance to use for finding valid usernames.

    Prints a list of valid usernames, if any are found.
    """

    #Proceed only if a URL has been provided.
    if bf is not None:
        bf.find_valid_usernames()
        if len(bf.valid_usernames) > 0:
            print(Style.BRIGHT + Fore.GREEN + f"\n-> Valid usernames: {', '.join(bf.valid_usernames)}" + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.RED + "\nNo username has been found." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")
        
        
def brute_force_option(bf):
    """
    Performs a brute-force attack on passwords using the existing BruteForcer instance.

    Args:
        bf (BruteForcer): The BruteForcer instance to use for the brute-force attack.

    Prints a list of valid passwords, if any are found.
    """

    #Proceed only if a URL has been provided.
    if bf is not None:
        #Proceed only if at least one user name has been found
        if len(bf.valid_usernames) > 0:
            bf.find_valid_passwords()
            print(Style.BRIGHT + Fore.GREEN + f"\n-> Passwords found: {', '.join(bf.valid_passwords)}" + Style.RESET_ALL)
        else:
            print(Style.BRIGHT + Fore.RED + "\nNo username has been found yet. Try using [2]OPTION to find one." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")
    
    
def output_results(bf):
    """
    Prints the results of the brute-force attack, including valid usernames, passwords, and credentials.

    Args:
        bf (BruteForcer): The BruteForcer instance containing the results to be printed.
    """

    valid_usernames = bf.valid_usernames
    valid_passwords = bf.valid_passwords
    print(f"\n-> Valid usernames: {Fore.LIGHTGREEN_EX} {', '.join(valid_usernames)} {Style.RESET_ALL}")

    if len(valid_passwords) > 0:
        print(f"-> Passwords found: {Fore.LIGHTGREEN_EX} {', '.join(valid_passwords)} {Style.RESET_ALL}")

        print("\n***********************************************************************\n\nCredentials found: ")
        credentials = [f"user: {Fore.LIGHTGREEN_EX}\'{username}\'{Style.RESET_ALL}, password: {Fore.LIGHTGREEN_EX}\'{password}\'{Style.RESET_ALL}" for username, password in zip(valid_usernames, valid_passwords)]

        for credential in credentials:
            print(f"- {credential}")
        print("\n***********************************************************************")
    else:
        print("\nNo passwords found yet")
        
            
def print_results_option(bf):
    """
    Provides a menu option for printing the results of the brute-force attack.
    
    Args:
        bf (BruteForcer): The BruteForcer instance containing the results to be printed.

    Calls the output_results() function to handle the actual printing.
    """

    #Proceed only if a URL has been provided.
    if bf is not None:
        output_results(bf)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")  
    
    
def save_file_option(bf):
    """
    Provides a menu option for saving the found credentials to a JSON file.

    Args:
        bf (BruteForcer): The BruteForcer instance containing the credentials to be saved.
    """

    #Proceed only if a URL has been provided.
    if bf is not None:
        # Check if there is at least one valid username and password.
        if len(bf.valid_usernames) > 0 and len(bf.valid_passwords):
            filename = input("\n>>> Please enter the file name to save the credentials that were found:")
            bf.save_credentials(filename)
            print(f"\n{Fore.GREEN}Credentials written on: {filename}.{Style.RESET_ALL}")
        else:
            print(Fore.LIGHTRED_EX + "\nNo valid credentials to save." + Style.RESET_ALL)
    else:
        print(Fore.LIGHTRED_EX + "\nPlease provide the login URL first." + Style.RESET_ALL)
    input("\n>>> Press ENTER to continue...")

    
       
def menu():
    """
    Runs the main menu loop for interacting with the brute-forcer.

    Handles user input, validates choices, and calls the appropriate functions for each menu option.
    """

    bf = None
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clean the terminal
        
        menu_header()
        menu_body(bf)
        
        option = input("\nPlease, select an option: ")
        #OPTION 1 - Enter login URL
        if option == '1':
            bf = enterURL_option()
        #OPTION 2 - Find valid user
        elif option == '2':
            find_username_option(bf)
        #OPTION 3 - Perform brute force attack
        elif option == '3':
            brute_force_option(bf)
        #OPTION 4 - Print results 
        elif option == '4':
            print_results_option(bf)
        #OPTION 5 - Save credentials in JSON file
        elif option == '5':
            save_file_option(bf)
        #OPTION 6 - Exit  
        elif option == '6':
            break
        #INVALID OPTION
        else:
            print(Fore.LIGHTRED_EX + "\nInvalid option. Please try again." + Style.RESET_ALL)
            input("\n>>> Press ENTER to continue...")

if __name__ == "__main__":
    menu()