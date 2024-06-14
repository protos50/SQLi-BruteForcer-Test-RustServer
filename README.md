# enum_sqli_test

## Description

`enum_sqli_test` is a test application designed to demonstrate potential SQL injection vulnerabilities through enumeration on a local Rust server. This project includes a server that simulates both a vulnerable and a secure application for educational and security testing purposes.

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
INSERT INTO users (username, password) VALUES ('morron', 'rojo') RETURNING id;
INSERT INTO users (username, password) VALUES ('morroncito', 'verde') RETURNING id;
INSERT INTO users (username, password) VALUES ('guiso', 'dearroz') RETURNING id;
INSERT INTO users (username, password) VALUES ('admin', 'password123');
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

## Brute Forcer

Navigate to the brute forcer directory:

```sh
cd ../brute_forcer
```
Run the brute forcer:

```sh
python main_bf.py
```
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

