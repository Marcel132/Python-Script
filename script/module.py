# from script import root, tk, main_screen
from script import root, tk, main_screen

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

# Style
font_main = ('Arial', 16)
font_small = ('Arial', 13)
main_frame_background = "#f2f2f2"
button_background = ""
button_cursor = "hand2"

# All necessary paths 
user_folder_path = 'users'

#Frames
main_frame = tk.Frame(root,
bg=main_frame_background)
main_frame.pack(fill="both", expand=True)

top_section_frame = tk.Frame(main_frame,
borderwidth=2, relief="ridge")
top_section_frame.pack()

left_section_frame = tk.Frame(main_frame,
borderwidth=2, relief="ridge")
left_section_frame.pack(side="left", anchor="nw")

content_section_frame = tk.Frame(main_frame,
borderwidth=2, relief="ridge")
content_section_frame.pack()

label_frame = tk.Frame(content_section_frame)
label_frame.pack(side="left")

entry_frame = tk.Frame(content_section_frame)
entry_frame.pack(side='left')

