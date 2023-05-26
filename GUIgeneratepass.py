import tkinter as tk
import random

class GUI():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Random Password Generator")
        self.root.geometry("500x325")

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

        self.button = tk.Button(self.root, text="Generate Password", font=("Sans", 16), command=self.generate_pass)
        self.button.pack(padx=10, pady=10)

        self.password_label = tk.Label(self.root, text="", font=("Sans", 12))
        self.password_label.pack(padx=20, pady=10)

        self.root.mainloop()

    def generate_pass(self):
        if not any([self.small_letters_state.get(), self.big_letters_state.get(), self.digits_state.get(), self.special_chars_state.get()]):
            self.password_label.config(text="Please check a box")
            return

        list1 = []
        list2 = ""
        wordssmall = "abcdefghijklmnopqrstuvwxyz"
        wordsbig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums = "1234567890"
        specha = "_?!+=-#*"

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

        total = 8 - len(list1)

        for i in range(total):
            gen = random.choice(list2)
            list1.append(gen)

        random.shuffle(list1)
        password = "".join(list1)
        self.password_label.config(text=password)

GUI()
