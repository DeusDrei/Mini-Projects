from tkinter import *


def calculate():
    x = user_input.get()
    num = round(int(x) * 1.609)
    km_num.config(text=num)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)
window.config(padx=60, pady=20)

# Blank
label = Label()
label.grid(row=0,column=0)

# Entry
user_input = Entry(width=10)
user_input.grid(row=0, column=1)

# Miles
miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

# is equal to
is_equal = Label(text="is equal to")
is_equal.grid(row=1,column=0)

# num km
km_num = Label(text="0")
km_num.grid(row=1,column=1)

# text km
text_num = Label(text="Km")
text_num.grid(row=1,column=2)

# Button
button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)



window.mainloop()

