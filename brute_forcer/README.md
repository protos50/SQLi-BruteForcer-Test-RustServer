# Python-login-bruteForce

## FJZ-Bruteforcer v1.0

**A simple, multithreaded Python brute-forcer intended for educational use such as Portswigger labs, specifically the login on the "Lab: Username enumeration via different responses" lab (https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses). It helps find valid usernames and passwords from pre-supplied files for a given login form.**

### Features:

- Multithreaded username validation
- Multithreaded brute-force password cracking
- Saves discovered credentials to a JSON file

### Disclaimer:

Use this tool responsibly and only on targets where you have explicit authorization.

### Understanding the target login Lab:

The Portswigger's login lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, found within the provided usernames and passwords wordlists.

### How the Bruteforcer Works:

1. Username Enumeration: The tool attempts to find valid usernames by sending login requests with usernames from the provided wordlist. It analyzes the server's response to differentiate between valid and invalid usernames.
2. Password Brute-Force: Once a valid username is identified, the tool attempts to crack the associated password by trying various password combinations from the provided password list.
3. Accessing the Account: If a valid username and password combination is found, the tool attempts to access the user's account page.


### Instructions:

1. Clone the repository:

    ```git clone https://github.com/protos50/brute-force-portswigger-login.git```

2. Install dependencies:

    ```pip install requests colorama```

3. Run the script:

    `python main_bf.py`
   
   or
   
    `python3 main_bf.py`

5. Follow the menu prompts:

  - Press '1' to provide the login URL or change it.
  - Press '2' to find valid usernames.
  - Press '3' to perform the brute-force attack.
  - Press '4' to view the results.
  - Press '5' to save found credentials to a JSON file.
  - Press '6' to exit the script

---

## Important Note

Before attempting a brute-force attack, it's crucial to **enumerate valid usernames** using the provided username list. This is because the brute-force attack requires a valid username as a target to crack the associated password.

The tool facilitates username enumeration and password brute-forcing, but it's **essential to adhere to responsible use and only target authorized systems**.

### Additional Notes:

- Remember to replace the example filenames ("usernames.txt" and "passwords.txt") in main_bf.py with the actual names of your custom files if you choose to use them.
- Ensure the wordlists are in a text format and adhere to the expected format (one username or password per line).

#### Known Issue: Incorrect Username-Password Pairing

##### Issue:

While the tool combines usernames and corresponding passwords in the credentials list, a known limitation exists. If a password cannot be found for a valid username, the tool may incorrectly pair usernames with passwords, leading to inaccurate results and potentially compromising the security of the target system.

##### Context:

Lab Objective: obtain a single valid username and password combination
This issue arises when the tool assumes a one-to-one correspondence between usernames and passwords in the provided wordlists. However, in real-world scenarios, there might be fewer passwords than usernames, or a username might have multiple potential passwords.

---

## About

This project was created by Franco Joaquin Zini

You can contact me at:

- Email: francojzini@gmail.com
- LinkedIn: https://www.linkedin.com/in/francojzini/

## License:
GNU General Public License (GNU GPL)

