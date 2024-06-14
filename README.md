# enum_sqli_test

## Description

`enum_sqli_test` is a test application designed to demonstrate potential SQL injection vulnerabilities through enumeration on a local Rust server. This project includes a server that simulates both a vulnerable and a secure application for educational and security testing purposes. 

It also includes a Python bruteforcer that exploits vulnerabilities through enumeration.

## Features

- **SQL Injection Demonstration**: Includes examples of how SQL injection vulnerabilities can be exploited and how to prevent them.
- **Rust Server**: Implementation of a server in Rust using Actix-web.
- **Brute Forcer**: A tool for brute-forcing usernames and passwords.

## Installation

### Prerequisites

- [Rust](https://www.rust-lang.org/tools/install) (for compiling the code if needed)
- [PostgreSQL](https://www.postgresql.org/download/)
- Python 3 (for the brute forcer)

### Compiled Executables

You can use the compiled executables found in the release directory:

- Safe_sqli: Secure code version.
- Unsafe_sqli: Vulnerable code version.

Run the appropriate script to start the server:

```sh
./release/run_Safe_sqli.sh
```
or

```sh
./release/run_Unsafe_sqli.sh
```

The server will start at http://127.0.0.1:8080.

### Database Setup

1. Ensure you have a PostgreSQL server running locally with user `postgres` and password `postgres`.

2. Create a database named `users_sqli` and a table `users` with `username` and `password` columns.

```sql
CREATE DATABASE users_sqli;
\c users_sqli
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
-- Insert users 
INSERT INTO users (username, password) VALUES ('protos50', 'protos50') RETURNING id;
INSERT INTO users (username, password) VALUES ('papitas', 'pure') RETURNING id;
INSERT INTO users (username, password) VALUES ('admin', 'admin') RETURNING id;
```

3. Access the login page:

    - Open your web browser and navigate to:

        http://localhost:8080/login

    - You can test the SQL injection vulnerability by entering the following in the username or password field:

        ```sql
        ' OR '1'='1
        ```
    - It is possible to attempt other SQL injections, such as:
  
      ```sql
        '; DROP TABLE users;--'
      ```

### Running or Modifying the Code (Optional)

If you want to execute or modify the code yourself, follow these steps:

1. Clone the repository:

```sh
git clone https://github.com/your_username/enum_sqli_test.git
cd enum_sqli_test/sqli_example
```

2. Install Rust dependencies (if you want to compile the code yourself):

```sh
cargo build
```
3. Run the server:

```sh
cargo run
```
## Code Details

The main.rs file contains both the secure and insecure login handling code. The secure code is active by default, while the insecure code is commented out. You can switch between them by commenting/uncommenting the respective sections.

## Brute Forcer

This project includes a modified version of the [FJZ-Bruteforcer v1.0](https://github.com/protos50/brute-force-portswigger-login), originally intended for educational purposes such as Portswigger labs. It has been adapted to test SQL injection vulnerabilities through enumeration on a local Rust server.

### Features

- Multithreaded username validation.
- Multithreaded brute-force password cracking.
- Saves discovered credentials to a JSON file.

### Understanding the Brute Forcer

The Brute Forcer included in this project is designed to find valid usernames and passwords from pre-supplied files for a given login form vulnerable to SQL injection.

### Instructions

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your_username/enum_sqli_test.git
   cd enum_sqli_test/brute_forcer

### Install dependencies

Ensure you have Python installed. Install necessary Python dependencies:

```sh
pip install requests colorama
```
### Running the Brute Forcer

Execute the script to begin testing for SQL injection vulnerabilities:

```sh
python main_bf.py
```

or

```sh
python main_bf.py
```

### Follow the menu prompts provided by the Brute Forcer:

1. Press '1' to provide the login URL or change it. If using the default localhost and port, the URL is:

    `http://localhost:8080/login`

2. Press '2' to find valid usernames.

3. Press '3' to perform the brute-force attack.

4. Press '4' to view the results.

5. Press '5' to save found credentials to a JSON file.

6. Press '6' to exit the script.

### Disclaimer

Use this tool responsibly and only on targets where you have explicit authorization.

## Contributing

Contributions are welcome. If you wish to contribute, please follow these steps:

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push your changes to your branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## Feedback

Your feedback is highly appreciated! If you found this tool useful or have applied it in your projects, please consider leaving a comment or feedback. Your insights can help improve this tool for everyone.

Feel free to open an issue to report bugs, suggest improvements, or share your experience using the tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

