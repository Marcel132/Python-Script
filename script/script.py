import tkinter as tk
import os

# Styles

custom_font = ('Arial', 17)

# All necessary paths 
user_folder_path = 'users'
folders_path = 'users/'

def create_user_interface():
    clear_screen()
    add_user_label = tk.Label(main_box, text="Podaj nazwę użytkownika:")
    username_entry = tk.Entry(main_box)
    submit_add_user_button = tk.Button(main_box, text="Dodaj", command=lambda: create_user(username_entry.get()))
    add_user_comment_label = tk.Label(main_box, text="", font=custom_font)

    add_user_label.pack()
    username_entry.pack()
    submit_add_user_button.pack()
    add_user_comment_label.pack()
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
    for widget in main_box.winfo_children():
        widget.destroy()

def display_users_folder():
    clear_screen()
    user_label = tk.Label(main_box, text="Użytkownicy:")
    user_label.pack()

    for folder in os.listdir(user_folder_path):
        user_button = tk.Button(main_box, text=folder, command=lambda folder=folder: display_user_data(folder), borderwidth=2, relief="ridge")
        user_button.pack()

def display_user_data(username):
    # Clear screen after open account folder
    clear_screen()

    user_label = tk.Label(main_box, text=f"Profil użytkownika: {username}")
    user_label.pack()

    dates = os.listdir(os.path.join(user_folder_path, username))
    for date in dates:
        date_button = tk.Button(main_box, text=date, command=lambda date=date: display_date_data(username, date), borderwidth=2, relief="ridge")
        date_button.pack(side="top-left")

def display_date_data(username, date):
    date_label = tk.Label(main_box, text=f"Data: {date}")
    date_label.pack()

    files = os.listdir(os.path.join(user_folder_path, username, date))
    for file in files:
        file_label = tk.Label(main_box, text=file)
        file_label.pack()

# Main interface - users account
root = tk.Tk()
root.title("Norma pracy")

# Root's styles
root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())

main_box = tk.Frame(root)
main_box.pack(fill="both", expand=True)

display_users_folder()

add_new_user_button = tk.Button(main_box, text="Dodaj użytkownika", command=create_user_interface)
add_new_user_button.pack()

add_user_comment_label = tk.Label(main_box, text="")
add_user_comment_label.pack()

root.mainloop()