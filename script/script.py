import tkinter as tk
import os
from datetime import datetime

# Styles
# main styles
font_main = ('Arial', 16)
font_small = ('Arial', 13)
main_frame_background = "#f2f2f2"
button_background = ""
button_cursor = "hand2"

# All necessary paths 
user_folder_path = 'users'


# This function can clear all content on screen
def clear_screen():
    for widget in main_frame.winfo_children():
        widget.destroy()

# This function can return user to main screen 
def return_to_main_site():
    clear_screen()
    main_screen()

# Change value to percentage
def change_pixels_to_percents(number):
    percents = number * 100
    return percents



# This function create users accounts
def create_user_interface():
    clear_screen()

    return_button = tk.Button(main_frame, text="Powrót na stronę", command=return_to_main_site,
    font=font_small, cursor=button_cursor)
    return_button.pack(side="top", anchor="ne", padx=10, pady=10)

    add_user_label = tk.Label(main_frame, text="Podaj nazwę użytkownika:", 
    font=font_main)
    add_user_label.pack()

    username_entry = tk.Entry(main_frame, 
    font=font_main)
    username_entry.pack()

    submit_add_user_button = tk.Button(main_frame, text="Dodaj", command=lambda: create_user(username_entry.get()), 
    font=font_small, cursor=button_cursor)
    submit_add_user_button.pack()

    add_user_comment_label = tk.Label(main_frame, text="", 
    font=font_small)
    add_user_comment_label.pack()

    # Function that checks if user doesn't filled input, username doesn't exists or account has the same name
    def create_user(username):
        if not username:
            add_user_comment_label.config(text="Błąd! Wpisz poprawnie dane", 
            font=font_small)

        if username_exists(username):
            add_user_comment_label.config(text=f"Użytkownik {username} już istnieje", 
            font=font_small)

        else:
            create_user_folder(username)
            add_user_comment_label.config(text=f"Użytkownik {username} został dodany", 
            font=font_small)
    
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
        borderwidth=0, font=font_main, cursor=button_cursor, padx=10, pady=10)
        user_button.pack()

    # Show accounts folder
    def display_user_data(username):
        clear_screen()
    
        top_section_frame = tk.Frame(main_frame,
        borderwidth=2, relief="ridge")
        top_section_frame.pack()

        left_section_frame = tk.Frame(main_frame,
        borderwidth=2, relief="ridge")
        left_section_frame.pack(side="left", anchor="nw")

        content_section_frame = tk.Frame(main_frame,
        borderwidth=2, relief="ridge")
        content_section_frame.pack()

        user_label = tk.Label(top_section_frame, text=f"Profil użytkownika: {username}", 
        font=font_small)
        user_label.pack(side="left", padx=(2, 300), pady=2)

        return_button = tk.Button(top_section_frame, text="Powrót na stronę", command=return_to_main_site, 
        font=font_small, cursor=button_cursor)
        return_button.pack(side="left", padx=(300, 2), pady=2)

        dates = os.listdir(os.path.join(user_folder_path, username))
        for date in dates:
                date_button = tk.Button(left_section_frame, text=date, command=lambda: main_program(username, date), 
                font=font_small, cursor=button_cursor)
                date_button.pack(padx=10, pady=2)

        add_date_folder_button = tk.Button(left_section_frame, text="+", command=lambda username=username: create_folder(username),
        font=font_small)
        add_date_folder_button.pack()

        # create folder that name include current date 
        def create_folder(username):
            current_date = datetime.now().date()
            if not os.path.exists(user_folder_path):
                os.mkdir(user_folder_path)
            add_folder = os.path.join(user_folder_path, username, str(current_date))
            os.mkdir(add_folder)
            clear_screen()
            display_user_data(username)
            

        # Show account data
        def main_program(username, date):
            file_name = os.path.join(user_folder_path, username, date, f"{date}.txt")

            label_frame = tk.Frame(content_section_frame)
            label_frame.pack(side="left")
            entry_frame = tk.Frame(content_section_frame)
            entry_frame.pack(side='left')

            line_number_label = tk.Label(label_frame, text='Numer Linii',
            font=font_small)
            line_number_label.pack(padx=10, pady=3)
            line_number_entry = tk.Entry(entry_frame)
            line_number_entry.pack(padx=10, pady=3)
            

            article_label = tk.Label(label_frame, text='Nazwa artykułu',
            font=font_small)
            article_label.pack(padx=10, pady=3)
            article_entry = tk.Entry(entry_frame)
            article_entry.pack(padx=10, pady=3)

            number_article_label = tk.Label(label_frame, text='Numer artykułu',
            font=font_small)
            number_article_label.pack(padx=10, pady=3)
            number_article_entry = tk.Entry(entry_frame)
            number_article_entry.pack(padx=10, pady=3)

            number_on_palette_label = tk.Label(label_frame, text='Ilość sztuk na palecie',
            font=font_small)
            number_on_palette_label.pack(padx=10, pady=3)
            number_on_palette_entry = tk.Entry(entry_frame)
            number_on_palette_entry.pack(padx=10, pady=3)
            
            standard_work_label = tk.Label(label_frame, text='Norma',
            font=font_small)
            standard_work_label.pack(padx=10, pady=3)
            standard_work_entry = tk.Entry(entry_frame)
            standard_work_entry.pack(padx=10, pady=3)
            
            add_file_button = tk.Button(content_section_frame, text="Dodaj", command=lambda: create_file(file_name))
            add_file_button.pack(padx=10, pady=3)    
           
            def create_file(file_name):
                content = (
                    f"Numer linii: {line_number_entry.get()} \n" + 
                    f"Nazwa artykułu: {article_entry.get()} \n" +
                    f"Numer artykułu: {number_article_entry.get()} \n" +
                    f"Ilość sztuk na palecie: {number_on_palette_entry.get()} \n" + 
                    f"Norma: {standard_work_entry.get()}"
                    )
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(content)
        

                

# Main screen
def main_screen():
    display_users_folder()

    add_new_user_button = tk.Button(main_frame, text="Dodaj użytkownika", command=create_user_interface, 
    font=font_main, cursor=button_cursor)
    add_new_user_button.pack()

# Main interface
root = tk.Tk()
root.title("Norma pracy")

# Set default screen size
root.geometry(f"{change_pixels_to_percents(100)}x{change_pixels_to_percents(100)}")

main_frame = tk.Frame(root, bg=main_frame_background)
main_frame.pack(fill="both", expand=True)


main_screen()
root.mainloop()