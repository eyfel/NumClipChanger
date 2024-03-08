import pyperclip
import re
import keyboard
from tkinter import Tk, Label
import threading

def update_gui_with_new_text(new_text):
    window.title("Clipboard Content")
    label.config(text=f"{new_text}")
    window.update_idletasks()
    window.update()
    window.after(800, lambda: label.config(bg="SystemButtonFace"))

def keep_window_always_on_top():
    window.attributes('-topmost', True)

def start_gui():
    global window, label
    window = Tk()
    window.title("Clipboard Content")
    window_width = 1100
    window_height = 115
    screen_width = window.winfo_screenwidth()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = 0
    window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
    label = Label(window, font=("Arial", 48, "bold"), foreground="red", text="No clipboard content yet")
    label.pack(expand=True)
    window.attributes('-topmost', True)

    # Panodaki mevcut içeriği al ve göster
    current_clipboard_content = pyperclip.paste()
    update_gui_with_new_text(current_clipboard_content)  # GUI'yi başlangıçta güncelle

    window.mainloop()

gui_thread = threading.Thread(target=start_gui, daemon=True)
gui_thread.start()



def increment_number(number_str):
    padding = ''
    for char in number_str:
        if char == '0':
            padding += char
        else:
            break

    number_part = number_str[len(padding):]
    incremented_number = int(number_part) + 1

    incremented_number_str = padding + str(incremented_number)

    return incremented_number_str


def decrease_number(number_str):
    padding = ''
    for char in number_str:
        if char == '0':
            padding += char
        else:
            break

    number_part = number_str[len(padding):]
    decremented_number = int(number_part) - 1

    decremented_number_str = padding + str(decremented_number)

    return decremented_number_str


def handle_clipboard_update(e):
    global label  # label widget'ını güncellemek için global değişkeni kullan
    if e.event_type == 'down' and e.name.lower() == 'e':
        
        current_clipboard_content = pyperclip.paste()
        parts = current_clipboard_content.split("-")
        last_part = parts[-1]

        search_result = re.search(r'\d+$', last_part)
        if search_result:
            number_str = search_result.group()
            incremented_number_str = increment_number(number_str)

            parts[-1] = re.sub(r'\d+$', incremented_number_str, last_part)
            new_clipboard_content = "-".join(parts)
            pyperclip.copy(new_clipboard_content)
            update_gui_with_new_text(new_clipboard_content)  # GUI'yi güncelle
        else:
            update_gui_with_new_text("No number found to increment.")  # GUI'yi güncelle

    elif e.event_type == 'down' and e.name.lower() == 'r':
        
        current_clipboard_content = pyperclip.paste()
        parts = current_clipboard_content.split("-")
        last_part = parts[-1]

        search_result = re.search(r'\d+$', last_part)
        if search_result:
            number_str = search_result.group()
            decremented_number_str = decrease_number(number_str)

            parts[-1] = re.sub(r'\d+$', decremented_number_str, last_part)
            new_clipboard_content = "-".join(parts)
            pyperclip.copy(new_clipboard_content)
            update_gui_with_new_text(new_clipboard_content)  # GUI'yi güncelle
        else:
            update_gui_with_new_text("No number found to decrement.")  # GUI'yi güncelle



keyboard.on_press(handle_clipboard_update)
print("Listening for 'e' key press to increment and 'r' key press to decrement the last number after '-' in the clipboard content.")
print("Press 'F10' to exit the program.")

keyboard.wait('f10')
