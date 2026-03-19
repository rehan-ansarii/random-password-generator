# Random Password Generator

A simple Python script that generates secure random passwords with customizable length.

## Description

This script creates a random password containing a mix of uppercase letters, lowercase letters, digits, and punctuation characters. Users can specify the desired password length, making it flexible for different security requirements.

## Features

- **Customizable Length**: Users can input any desired password length
- **Diverse Character Set**: Includes:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Punctuation characters (!@#$%^&*, etc.)
- **Fast Generation**: Generates passwords instantly

## Requirements

- Python 3.x
- No external dependencies (uses only the Python standard library)

## Usage

1. Run the script:
   ```bash
   python password_generator.py
   ```

2. When prompted, enter the desired password length:
   ```
   Enter a length: 12
   ```

3. The script will output your generated password:
   ```
   Your Password is: aB3$xK9@mL2#
   ```

## Example

```bash
$ python password_generator.py
Enter a length: 16
Your Password is: K7$mP2@xQ9!lR4%sT
```

## How It Works

1. The script imports the `random` and `string` modules
2. It prompts the user to enter the desired password length
3. It creates a pool of characters (letters, digits, and punctuation)
4. It randomly selects characters from the pool based on the specified length
5. It displays the generated password
