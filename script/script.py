import tkinter as tk
import os

# Styles
font_main = ('Arial', 16)

bg_color_black = (255, 255, 255)

# All necessary paths 
user_folder_path = 'users'
folders_path = 'users/'

# This function can clear all content on screen
def clear_screen():
    for widget in main_box.winfo_children():
        widget.destroy()

# This function can return user to main screen 
def return_to_main_site():
    clear_screen()
    main_screen()

# This function create users accounts
def create_user_interface():
    clear_screen()

    return_button = tk.Button(main_box, text="Powrót na stronę", command=return_to_main_site, font=font_main)
    return_button.pack(side="top", anchor="ne", padx=6, pady=2)

    add_user_label = tk.Label(main_box, text="Podaj nazwę użytkownika:", font=font_main)
    add_user_label.pack()

    username_entry = tk.Entry(main_box, font=font_main)
    username_entry.pack()

    submit_add_user_button = tk.Button(main_box, text="Dodaj", command=lambda: create_user(username_entry.get()), font=font_main)
    submit_add_user_button.pack()

    add_user_comment_label = tk.Label(main_box, text="", font=font_main)
    add_user_comment_label.pack()

    # Function that checks if user doesn't filled input, username doesn't exists or account has the same name
    def create_user(username):
        if not username:
            add_user_comment_label.config(text="Błąd! Wpisz poprawnie dane", font=font_main)

        if username_exists(username):
            add_user_comment_label.config(text=f"Użytkownik {username} już istnieje", font=font_main)

        else:
            create_user_folder(username)
            add_user_comment_label.config(text=f"Użytkownik {username} został dodany", font=font_main)
    
    def username_exists(username):
        files = os.listdir(user_folder_path)
        return username in files
    
# Create account folder 
def create_user_folder(username):
    user_folder = os.path.join(user_folder_path, username)
    os.mkdir(user_folder)

# Show accounts
def display_users_folder():
    clear_screen()

    user_label = tk.Label(main_box, text="Użytkownicy: ", font=font_main)
    user_label.pack()

    for folder in os.listdir(user_folder_path):
        user_button = tk.Button(main_box, text=folder, command=lambda folder=folder: display_user_data(folder), borderwidth=2, relief="ridge", font=font_main)
        user_button.pack()

    # Show accounts folder
    def display_user_data(username):
        clear_screen()
    
        

        return_button = tk.Button(main_box, text="Powrót na stronę", command=return_to_main_site, font=font_main)
        return_button.pack(side="top", anchor="ne", padx=6, pady=2)

        user_label = tk.Label(main_box, text=f"Profil użytkownika: {username}")
        user_label.pack(side="top")

        dates = os.listdir(os.path.join(user_folder_path, username))
        for date in dates:
            date_button = tk.Button(main_box, text=date, command=lambda date=date: display_date_data(username, date), borderwidth=2, relief="ridge")
            date_button.pack(side="left", anchor="nw")

        # Show account data
        def display_date_data(username, date):
            date_label = tk.Label(main_box, text=f"Data: {date}")
            date_label.pack()

            files = os.listdir(os.path.join(user_folder_path, username, date))
            for file in files:
                file_label = tk.Label(main_box, text=file)
                file_label.pack()

# Main screen
def main_screen():
    display_users_folder()

    add_new_user_button = tk.Button(main_box, text="Dodaj użytkownika", command=create_user_interface, font=font_main)
    add_new_user_button.pack()

    add_user_comment_label = tk.Label(main_box, text="", font=font_main)
    add_user_comment_label.pack()


# Main interface
root = tk.Tk()
root.title("Norma pracy")

# Root's styles
root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())

main_box = tk.Frame(root)
main_box.pack(fill="both", expand=True)

main_screen()
root.mainloop()