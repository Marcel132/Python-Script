import tkinter as tk
import os

user_folder_path = "users"

def create_user_interface():
    clear_screen()
    add_user_label = tk.Label(root, text="Podaj nazwę użytkownika:")
    username_entry = tk.Entry(root)
    submit_add_user_button = tk.Button(root, text="Dodaj", command=lambda: create_user(username_entry.get()))

    add_user_label.pack()
    username_entry.pack()
    submit_add_user_button.pack()

def create_user(username):
    if not username:
        return 

    if username_exists(username):
        add_user_comment_label.config(text=f"Użytkownik {username} już istnieje")
    else:
        create_user_folder(username)
        add_user_comment_label.config(text=f"Użytkownik {username} został dodany")

def username_exists(username):
    files = os.listdir(user_folder_path)
    return username in files

def create_user_folder(username):
    user_folder = os.path.join(user_folder_path, username)
    os.mkdir(user_folder)

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()

def display_user_folders():
    clear_screen()
    user_label = tk.Label(root, text="Użytkownicy:")
    user_label.pack()

    for folder in os.listdir(user_folder_path):
        user_button = tk.Button(root, text=folder, command=lambda folder=folder: read_user_folder(folder))
        user_button.pack()

def read_user_folder(folder_name):
    clear_screen()
    folder_name = os.path.join(user_folder_path, folder_name)
    if os.path.exists(folder_name):
        with open(folder_name, 'r') as folder:
            data = folder.read()
            label_comment = tk.Label(root, text=data)
            label_comment.pack()
    else:
        label_comment = tk.Label(root, text=f"Plik {folder_name} nie istnieje")
        label_comment.pack()

root = tk.Tk()
root.title("Norma pracy")
root.geometry("800x600")

display_user_folders()

add_new_user_button = tk.Button(root, text="Dodaj użytkownika", command=create_user_interface)
add_new_user_button.pack()

add_user_comment_label = tk.Label(root, text="")
add_user_comment_label.pack()

root.mainloop()