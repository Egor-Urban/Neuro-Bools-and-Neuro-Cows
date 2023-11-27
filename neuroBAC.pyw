'''
        Разработчик: Hex_
        Страна: Россия
        Версия: 2.2.56[RBA]  (Релиз 2; Бета 2; альфа 56)
        Имя: Нейро-быки и Нейро-коровы
'''
#IMPORTS
import subprocess
import tkinter as tk
from tkinter import messagebox

def get_generated_number():
    result = subprocess.run(['python', 'generator.pyw'], capture_output=True, text=True)
    if result.returncode == 0:
        generated_number = int(result.stdout.strip())
        return generated_number
    else:
        print("!ERROR! => [code:1] => Ошибка при импорте числа генератора")
        return None

number_g = get_generated_number()

if number_g is not None:
    print(number_g)

def count_bulls_cows(guess, number):
    bulls = 0
    cows = 0
    for i in range(len(guess)):
        if guess[i] == number[i]:
            bulls += 1
        elif guess[i] in number:
            cows += 1
    return bulls, cows

def submit_guess():
    global attempts_left

    guess = guess_entry.get()
    guess_entry.delete(0, tk.END)

    if not guess.isdigit() or len(guess) != 4:
        messagebox.showerror("Ошибка", "Пожалуйста, введите четырехзначное число.")
        return

    guess_list = list(guess)
    number_list = list(str(number_g))

    bulls, cows = count_bulls_cows(guess_list, number_list)
    result_text = f"Б: {bulls}, К: {cows}"
    result_label.config(text=result_text)

    attempts_left -= 1
    attempts_text = f"Попыток осталось: {attempts_left}"
    attempts_label.config(text=attempts_text)

    guesses_listbox.insert(tk.END, guess) 
    results_listbox.insert(tk.END, result_text)  

    if bulls == 4:
        messagebox.showinfo("Победа!", "Поздравляю, вы угадали число!")
        window.destroy()  

    if attempts_left == 0:
        messagebox.showinfo("Поражение", f"К сожалению, вы исчерпали все попытки.\nЗагаданное число было: {number_g}.")
        reset_game()


def reset_game():
    global attempts_left

    attempts_left = 9
    attempts_text = f"Попыток осталось: {attempts_left}"
    attempts_label.config(text=attempts_text)

    guesses_listbox.delete(0, tk.END)  
    results_listbox.delete(0, tk.END)  

    result_label.config(text="")


window = tk.Tk()
#window.iconbitmap('OIG.ico') ЭТА ТВАРь НЕ КОМПИЛИРУЕТСЯ В ОДИН ФАЙЛ, и идёт нафиг
window.title("Нейро-Быки и Нейро-Коровы [ver. 2.2.56 RBA]")
window.geometry("400x400")
guess_label = tk.Label(window, text="Введите число:")
guess_label.pack()
guess_entry = tk.Entry(window, width=10)
guess_entry.pack()
submit_button = tk.Button(window, text="Проверить", command=submit_guess)
submit_button.pack()
attempts_left = 9
attempts_text = f"Попыток осталось: {attempts_left}"
attempts_label = tk.Label(window, text=attempts_text)
attempts_label.pack()
result_label = tk.Label(window, text="")
result_label.pack()
guesses_frame = tk.Frame(window)
guesses_frame.pack(side=tk.LEFT, padx=10)
guesses_label = tk.Label(guesses_frame, text="Введенные числа:")
guesses_label.pack()
guesses_listbox = tk.Listbox(guesses_frame, width=30, height=16)
guesses_listbox.pack()
results_frame = tk.Frame(window)
results_frame.pack(side=tk.RIGHT, padx=10)
results_label = tk.Label(results_frame, text="Результаты:")
results_label.pack()
results_listbox = tk.Listbox(results_frame, width=30, height=16)
results_listbox.pack()

window.mainloop()
