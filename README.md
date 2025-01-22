# Password Manager App

This is a simple **Password Manager** application built using Python's **Tkinter** library. The app allows users to generate strong random passwords, save website login credentials (email and password) for different websites, and store them securely in a text file.

## Features
- **Password Generator**: Generates a strong random password that includes letters, symbols, and numbers.
- **Save Credentials**: Users can save the website, email, and password in a file (`passwords.txt`).
- **Password Copying**: Automatically copies the generated password to the clipboard for easy pasting.
- **User-Friendly UI**: A simple and intuitive graphical user interface (GUI) to manage passwords.

## Technologies Used
- **Python**: The programming language used for the application.
- **Tkinter**: A Python library for creating graphical user interfaces.
- **pyperclip**: A library used to copy text to the clipboard.
- **random**: Python's built-in module used to generate random values for passwords.

## Requirements
Before running the script, make sure you have the following libraries installed:

```bash
pip install pyperclip
````

1 - Usage
Clone this repository to your local machine:
  git clone https://github.com/your-username/password-manager-app.git
2- Make sure you have the necessary image file (logo.png) in the same directory as the script.
3 - Run the application:

python password_manager.py

4 - The application window will open. You can:
Generate a random password by clicking the Generate Password button.
Enter the website name, email/username, and password, then click Add to save the credentials.
Your password will be copied to the clipboard automatically after generation.

How the App Works
Password Generator: When the user clicks the "Generate Password" button, the app generates a random password with:

8 to 10 random letters (both uppercase and lowercase).
2 to 4 symbols.
2 to 4 numbers.
The generated password is automatically inserted into the password entry field and copied to the clipboard using pyperclip.

Save Credentials: When the user clicks the "Add" button, the entered website name, email/username, and password are saved in a text file called passwords.txt. If any required field (website or password) is empty, a warning message will appear.

Text File Storage: The saved credentials are stored in passwords.txt in the following format:
Website: example.com | Email: user@example.com | Password: generatedpassword

Example of passwords.txt file
The file passwords.txt will store the saved credentials like this:
Website: example.com | Email: user@example.com | Password: mysecurepassword123
Website: anotherwebsite.com | Email: myemail@gmail.com | Password: randompass456
