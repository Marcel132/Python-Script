import tkinter as tk

# Funkcja obliczająca normę
def main_program(number_people_entry, efficiency_entry, assumed_standard_entry, result_working_standard_label, comment_label):
    try:
        number_people = int(number_people_entry.get())
        efficiency = float(efficiency_entry.get())
        assumed_standard = int(assumed_standard_entry.get())
        working_standard = efficiency
        calc_working_standard = assumed_standard - working_standard

        # Logika dotycząca normy pracy
        if calc_working_standard < 0:
            result_working_standard_label.config(text=f"Obliczona norma: {working_standard}")
            comment_label.config(text=f"Norma wynosi: {calc_working_standard}. Aby utrzymać normę, należy zwiększyć wydajność pracy!")
        elif calc_working_standard == 0:
            result_working_standard_label.config(text=f"Obliczona norma: {working_standard}")
            comment_label.config(text=f"Norma wynosi {calc_working_standard}. Aby zachować normę, należy utrzymać lub przyspieszyć wydajność pracy!")
        elif calc_working_standard > 0:
            result_working_standard_label.config(text=f"Obliczona norma: {working_standard}")
            comment_label.config(text=f"Norma wynosi {calc_working_standard}. Aby zachować normę, należy utrzymać wydajność pracy!")
    except ValueError:
        result_working_standard_label.config(text="Obliczona norma: !Błąd! Popraw dane.")

# Funkcja do dodawania nowej taśmy
def add_new_line():
    new_frame = tk.Frame(root)
    new_frame.pack(padx=10, side="left")

    number_people_label = tk.Label(new_frame, text="Liczba osób: ")
    number_people_label.pack()
    number_people_entry = tk.Entry(new_frame)
    number_people_entry.pack()

    efficiency_label = tk.Label(new_frame, text="Wydajność pracy: ")
    efficiency_label.pack()
    efficiency_entry = tk.Entry(new_frame)
    efficiency_entry.pack()

    assumed_standard_label = tk.Label(new_frame, text="Wydajność zakładana: ")
    assumed_standard_label.pack()
    assumed_standard_entry = tk.Entry(new_frame)
    assumed_standard_entry.pack()

    calc_button = tk.Button(new_frame, text="Zachowaj", command=lambda: main_program(number_people_entry, efficiency_entry, assumed_standard_entry, result_working_standard_label, comment_label))
    calc_button.pack()

    result_working_standard_label = tk.Label(new_frame, text="")
    result_working_standard_label.pack()
    comment_label = tk.Label(new_frame, text="")
    comment_label.pack()

root = tk.Tk()
root.title("Norma pracy")

add_new_line_button = tk.Button(root, text="Dodaj nową linie", command=add_new_line)
add_new_line_button.pack()

root.mainloop()