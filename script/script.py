import tkinter as tk
import os

# Styles
# main styles
font_main = ('Arial', 16)
main_frame_background = "#f2f2f2"
button_background = ""
button_cursor = "hand2"
padding_x = 10
padding_y = 10


# .UI/UX-1-hex { color: #A4A5A6; }
# .UI/UX-2-hex { color: #A68256; }
# .UI/UX-3-hex { color: #F2F2F2; }
# .UI/UX-4-hex { color: #262626; }
# .UI/UX-5-hex { color: #0D0D0D; }

# /* Color Theme Swatches in RGBA */
# .UI/UX-1-rgba { color: rgba(164, 164, 165, 1); }
# .UI/UX-2-rgba { color: rgba(165, 129, 86, 1); }
# .UI/UX-3-rgba { color: rgba(242, 242, 242, 1); }
# .UI/UX-4-rgba { color: rgba(38, 38, 38, 1); }
# .UI/UX-5-rgba { color: rgba(12, 12, 12, 1); }

# /* Color Theme Swatches in HSLA */
# .UI/UX-1-hsla { color: hsla(224, 0, 64, 1); }
# .UI/UX-2-hsla { color: hsla(33, 31, 49, 1); }
# .UI/UX-3-hsla { color: hsla(0, 0, 95, 1); }
# .UI/UX-4-hsla { color: hsla(0, 0, 15, 1); }
# .UI/UX-5-hsla { color: hsla(0, 0, 5, 1); }


# All necessary paths 
user_folder_path = 'users'
folders_path = 'users/'


# This function can clear all content on screen
def clear_screen():
    for widget in main_frame.winfo_children():
        widget.destroy()

# This function can return user to main screen 
def return_to_main_site():
    clear_screen()
    main_screen()



# This function create users accounts
def create_user_interface():
    clear_screen()

    return_button = tk.Button(main_frame, text="Powrót na stronę", command=return_to_main_site,
    font=font_main, cursor=button_cursor)
    return_button.pack(side="top", anchor="ne", padx=padding_x, pady=padding_y)

    add_user_label = tk.Label(main_frame, text="Podaj nazwę użytkownika:", 
    font=font_main)
    add_user_label.pack()

    username_entry = tk.Entry(main_frame, 
    font=font_main)
    username_entry.pack()

    submit_add_user_button = tk.Button(main_frame, text="Dodaj", command=lambda: create_user(username_entry.get()), 
    font=font_main, cursor=button_cursor)
    submit_add_user_button.pack()

    add_user_comment_label = tk.Label(main_frame, text="", 
    font=font_main)
    add_user_comment_label.pack()

    # Function that checks if user doesn't filled input, username doesn't exists or account has the same name
    def create_user(username):
        if not username:
            add_user_comment_label.config(text="Błąd! Wpisz poprawnie dane", 
            font=font_main)

        if username_exists(username):
            add_user_comment_label.config(text=f"Użytkownik {username} już istnieje", 
            font=font_main)

        else:
            create_user_folder(username)
            add_user_comment_label.config(text=f"Użytkownik {username} został dodany", 
            font=font_main)
    
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

    user_label = tk.Label(main_frame, text="Użytkownicy: ", 
    font=font_main)
    user_label.pack()

    for folder in os.listdir(user_folder_path):
        user_button = tk.Button(main_frame, text=folder, command=lambda folder=folder: display_user_data(folder), 
        borderwidth=0, font=font_main, cursor=button_cursor, padx=padding_x, pady=padding_y)
        user_button.pack()

    # Show accounts folder
    def display_user_data(username):
        clear_screen()
    
        top_section_frame = tk.Frame(main_frame)
        top_section_frame.pack()
        top_left = tk.Frame(top_section_frame)
        top_left.pack()
        top_right = tk.Frame(top_section_frame)
        top_right.pack()

        user_label = tk.Label(top_left, text=f"Profil użytkownika: {username}", 
        font=font_main)
        user_label.pack( padx=4, pady=4)

        return_button = tk.Button(top_right, text="Powrót na stronę", command=return_to_main_site, 
        font=font_main, cursor=button_cursor)
        return_button.pack(padx=4, pady=4)

        dates = os.listdir(os.path.join(user_folder_path, username))
        for date in dates:
            date_button = tk.Button(main_frame, text=date, command=lambda date=date: display_date_data(username, date), 
            cursor=button_cursor)
            date_button.pack(side="left", anchor="nw")

        # Show account data
        def display_date_data(username, date):
            date_label = tk.Label(main_frame, text=f"Data: {date}")
            date_label.pack()

            files = os.listdir(os.path.join(user_folder_path, username, date))
            for file in files:
                file_label = tk.Label(main_frame, text=file)
                file_label.pack()

# Main screen
def main_screen():
    display_users_folder()

    add_new_user_button = tk.Button(main_frame, text="Dodaj użytkownika", command=create_user_interface, 
    font=font_main, cursor=button_cursor)
    add_new_user_button.pack()

    # add_user_comment_label = tk.Label(main_frame, text="", 
    # font=font_main)
    # add_user_comment_label.pack()


# Main interface
root = tk.Tk()
root.title("Norma pracy")

# Root's styles
root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())

main_frame = tk.Frame(root, bg=main_frame_background)
main_frame.pack(fill="both", expand=True)


main_screen()
root.mainloop()