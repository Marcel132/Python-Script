# import time

# print("Podaj liczbę osób")
# people = int(input())

# times = people * 3

# print("Ilość osób pomnożone przez 3", times)



import tkinter as tk

def hello():
  label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Prosty program w Tkinter")

label = tk.Label(root, text="Wprowadź swoje imię:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Przywitaj się", command=hello)
button.pack()

root.mainloop()