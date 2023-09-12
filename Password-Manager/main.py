from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- SEARCH ------------------------------- #
def search_website():
    website = website_text.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")
    

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    x = website_text.get()
    y = email_text.get()
    z = password_text.get()
    new_data = {
        x: {
            "email": y,
            "password" : z,
        }
    }

    if len(x) == 0 or len(y) == 0 or len(z) == 0:
        return messagebox.askokcancel(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:    
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)


# Lock Picture
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Website Label and text box
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_text = Entry(width=33)
website_text.focus()
website_text.grid(row=1, column=1)


# Email Label and text box
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_text = Entry(width=52)
email_text.insert(0, "sample@gmail.com")
email_text.grid(row=2, column=1, columnspan=2)


# Password label and text box
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_text = Entry(width=33)
password_text.grid(row=3, column=1)


# Generate Password Button
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2)


# Add Button
add_button = Button(text="Add", width=44, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

# Seach Button
search_button = Button(text="Search", width=14, command=search_website)
search_button.grid(row=1, column=2)



window.mainloop()