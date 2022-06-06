from tkinter import *

def calculate():
    converter = round(float(input.get()) * 1.6)
    convert.config(text=converter)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=20, pady=50)

input = Entry(width=8, font=("Arial", 14, "normal"))
input.grid(column=1, row=0)
print(input.get())

label1 = Label(text="is equal to", font=("Arial", 14, "normal"))
label1.config(padx=20, pady=10)
label1.grid(column=0, row=1)

convert = Label(text="0",font=("Arial", 14, "normal"))
convert.grid(column=1, row=1)
convert.config(padx=20)

label2 = Label(text="Miles", font=("Arial", 14, "normal"))
label2.config(padx=10, pady=5)
label2.grid(column=2, row=0)

label3 = Label(text="Km", font=("Arial", 14, "normal"))
label1.config(padx=10, pady=5)
label3.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate, font=("Arial", 14, "normal"))
button.grid(column=1, row=2)

window.mainloop()