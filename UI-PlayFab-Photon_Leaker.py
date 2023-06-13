import json, ctypes
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox

def handle_file_select():
    file_paths = filedialog.askopenfilenames(filetypes=[("DAT files", "*.dat")])

    for file_path in file_paths:
        with open(file_path, "rb") as file:
            root.geometry("600x300")
            if "PhotonServerSettings-resources.assets-3654.dat" in file_path:
                file.seek(0x38)
                pun = file.read(36).decode('utf-8')

                file.seek(0x68)
                voice = file.read(36).decode('utf-8')
                
                pun_value_label.config(text=pun)
                voice_value_label.config(text=voice)

            elif "PlayFabSharedSettings-resources.assets-3655.dat" in file_path:
                file.seek(0x3C)
                title = file.read(5).decode('utf-8')

                title_value_label.config(text=title)

def handle_save():
    pun_value = pun_value_label.cget("text")
    voice_value = voice_value_label.cget("text")
    title_value = title_value_label.cget("text")

    data = {
        "pun": pun_value,
        "voice": voice_value,
        "title": title_value
    }

    save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if save_path:
        with open(save_path, "w") as file:
            json.dump(data, file)
        messagebox.showinfo("Save", "File saved successfully.")

def handle_copy():
    pun_value = pun_value_label.cget("text")
    voice_value = voice_value_label.cget("text")
    title_value = title_value_label.cget("text")

    data = {
        "pun": pun_value,
        "voice": voice_value,
        "title": title_value
    }

    json_data = json.dumps(data, indent=4)
    root.clipboard_clear()
    root.clipboard_append(json_data)
    messagebox.showinfo("Copy", "Data copied to clipboard as JSON.")

root = tk.Tk()
root.title("Photon & PlayFab Leaker")
root.geometry("300x100")

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
root.iconbitmap(default='icon.ico')

root.tk_setPalette(background='#222', foreground='white')

header_label = tk.Label(root, text="Photon & PlayFab Leaker", font=("Arial", 16), fg='white', bg='#222')
header_label.pack(pady=10)

select_button = tk.Button(root, text="Select Files", font=("Arial", 12), command=handle_file_select, fg='white', bg='#333')
select_button.pack(pady=10)

fields_frame = tk.Frame(root, bg='#222')
fields_frame.pack(pady=10)

pun_label = tk.Label(fields_frame, text="Pun Value:", font=("Arial", 12), fg='white', bg='#222')
pun_label.grid(row=0, column=0, sticky="w")

pun_value_label = tk.Label(fields_frame, text="", font=("Arial", 12), fg='white', bg='#222')
pun_value_label.grid(row=0, column=1, sticky="w")

voice_label = tk.Label(fields_frame, text="Voice Value:", font=("Arial", 12), fg='white', bg='#222')
voice_label.grid(row=1, column=0, sticky="w")

voice_value_label = tk.Label(fields_frame, text="", font=("Arial", 12), fg='white', bg='#222')
voice_value_label.grid(row=1, column=1, sticky="w")

title_label = tk.Label(fields_frame, text="Title:", font=("Arial", 12), fg='white', bg='#222')
title_label.grid(row=2, column=0, sticky="w")

title_value_label = tk.Label(fields_frame, text="", font=("Arial", 12), fg='white', bg='#222')
title_value_label.grid(row=2, column=1, sticky="w")

save_button = tk.Button(root, text="Save", font=("Arial", 12), command=handle_save, fg='white', bg='#333')
save_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy as JSON", font=("Arial", 12), command=handle_copy, fg='white', bg='#333')
copy_button.pack(pady=10)

root.mainloop()
