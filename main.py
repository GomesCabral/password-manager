from tkinter import *
from tkinter import messagebox
import random
import pyperclip as pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    #for char in range(nr_letters):
     # password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    #for char in range(nr_symbols):
     # password_list += random.choice(symbols)

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    #for char in range(nr_numbers):
     # password_list += random.choice(numbers)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    password_entry.insert(0, password)

    #auto copy - ready to paste
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website_name) == 0:
        messagebox.showwarning(title='oopsss', message="The Website field is empty")
    elif len(password) == 0:
        messagebox.showwarning(title='oopsss', message="The Password field is empty")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIt's ok to save?")

        if is_ok:
            with open("passwords.txt", mode='a') as file:
                file.write(f'Website: {website_name} | Email: {email} | Password: {password}\n')

                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


#WEBSITE
website_label = Label(text="website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

#EMAIL/USERNAME
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(END, string="myemail@hotmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

#PASSWORD
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()