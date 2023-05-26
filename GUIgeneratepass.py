import tkinter as tk
from tkinter import messagebox
import random

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random Password Generator")
        self.root.geometry("1000x450") 

        self.label = tk.Label(self.root, text="Random Password Generator", font=("Sans", 16))
        self.label.pack(padx=20, pady=10)

        self.small_letters_state = tk.IntVar()
        self.big_letters_state = tk.IntVar()
        self.digits_state = tk.IntVar()
        self.special_chars_state = tk.IntVar()

        self.small_letters_check = tk.Checkbutton(self.root, text="Small Letters", font=("Sans", 12), variable=self.small_letters_state)
        self.small_letters_check.pack(padx=5, pady=5)

        self.big_letters_check = tk.Checkbutton(self.root, text="Big Letters", font=("Sans", 12), variable=self.big_letters_state)
        self.big_letters_check.pack(padx=5, pady=5)

        self.digits_check = tk.Checkbutton(self.root, text="Digits", font=("Sans", 12), variable=self.digits_state)
        self.digits_check.pack(padx=5, pady=5)

        self.special_chars_check = tk.Checkbutton(self.root, text="Special Characters", font=("Sans", 12), variable=self.special_chars_state)
        self.special_chars_check.pack(padx=5, pady=5)

        self.length_label = tk.Label(self.root, text="Password Length:", font=("Sans", 12))
        self.length_label.pack()

        self.length_entry = tk.Entry(self.root, font=("Sans", 12))
        self.length_entry.pack(padx=5, pady=5)

        self.generate_button = tk.Button(self.root, text="Generate Password", font=("Sans", 12), command=self.generate_pass)
        self.generate_button.pack(padx=10, pady=10)

        self.password_label = tk.Label(self.root, text="", font=("Sans", 12))
        self.password_label.pack(padx=20, pady=10)

        self.root.mainloop()

    def generate_pass(self):
        length = self.length_entry.get().strip()
        is_length_empty = length == ""
        is_no_checkbox_checked = (
            self.small_letters_state.get() == 0 and
            self.big_letters_state.get() == 0 and
            self.digits_state.get() == 0 and
            self.special_chars_state.get() == 0
        )

        if is_length_empty and is_no_checkbox_checked:
            messagebox.showerror("Invalid Input", "Please check a box and enter a password length.")
            return

        if is_length_empty:
            messagebox.showerror("Invalid Input", "Please enter a password length.")
            return
        
        if is_no_checkbox_checked:
            messagebox.showerror("Invalid Input", "Please check a box")

        if not length.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")
            return

        length = int(length)

        if length < 4:
            messagebox.showerror("Invalid Input", "Please enter a number greater than or equal to 4.")
            return

        list1 = []
        list2 = ""
        wordssmall = "abcdefghijklmnopqrstuvwxyz"
        wordsbig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        specha = "_?!+=-#*"

        if length >= 4:
            if self.small_letters_state.get() == 1:
                list1.append(random.choice(wordssmall))
                list2 += wordssmall
            if self.big_letters_state.get() == 1:
                list1.append(random.choice(wordsbig))
                list2 += wordsbig
            if self.digits_state.get() == 1:
                list1.append(random.choice(nums))
                list2 += nums
            if self.special_chars_state.get() == 1:
                list1.append(random.choice(specha))
                list2 += specha

            total = length - len(list1)

            for i in range(total):
                gen = random.choice(list2)
                list1.append(gen)

            random.shuffle(list1)
            password = "".join(list1)
            self.password_label.config(text=password)

GUI()
