import tkinter as tk
from tkinter import ttk, Text, messagebox, Scrollbar
from hashlib import sha256
from pynostr.key import PrivateKey
import os
import base64

def copy_to_clipboard(text_widget):
    text = text_widget.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def clear_all_results():
    entries = [hex_entry, hash_entry]
    for entry in entries:
        entry.config(state=tk.NORMAL)
        entry.delete("1.0", tk.END)
        entry.config(state=tk.DISABLED)

    nostr_result_text.config(state=tk.NORMAL)
    nostr_result_text.delete("1.0", tk.END)
    nostr_result_text.config(state=tk.DISABLED)

def update_text_entry(entry_widget, text, readonly=True):
    entry_widget.config(state='normal')
    entry_widget.delete(1.0, "end")
    entry_widget.insert(1.0, text)
    if readonly:
        entry_widget.config(state='disabled')

def create_readonly_entry(label_text_cn, label_text_en, frame):
    label = ttk.Label(frame, text=f"{label_text_en} / {label_text_cn}")
    label.pack(anchor='center')
    entry_frame = tk.Frame(frame)
    entry_frame.pack(fill='x', expand=True)
    text_entry_height = 1
    text_entry = tk.Text(entry_frame, height=text_entry_height, width=80, bg='#f0f0f0', wrap="word")
    text_entry.config(state='disabled')
    text_entry.pack(side='left')
    copy_button = ttk.Button(entry_frame, text='Copy | 复制', command=lambda: copy_to_clipboard(text_entry))
    copy_button.pack(side='left', padx=5)
    return text_entry

def validate_hash_times(new_value):
    if not new_value:
        return True
    try:
        value = int(new_value)
        return 1 <= value <= 10000
    except ValueError:
        return False

def validate_generate_count(new_value):
     if not new_value:
        return True
     try:
        value = int(new_value)
        return 1 <= value <= 1000
     except ValueError:
        return False

def generate_nostr_keys(initial_passphrase, count, salt, hash_times):
    nostr_keys = []
    for i in range(1, count + 1):
        seed_string = initial_passphrase

        for _ in range(hash_times):
            if salt:
              seed_string = seed_string + salt
            bytes_seed_string = seed_string.encode('utf-8')
            seed_string = sha256(bytes_seed_string).hexdigest()


        seed_string_bytes = seed_string.encode('utf-8') + f"[{i}]".encode('utf-8')

        private_key_seed = sha256(seed_string_bytes).digest()
        private_key = PrivateKey(private_key_seed)
        public_key = private_key.public_key
        nostr_keys.append((private_key.bech32(), public_key.bech32()))
    return nostr_keys

def generate_brain_wallet():
    passphrase = passphrase_entry.get()
    salt = salt_entry.get()
    try:
        hash_times = int(hash_times_entry.get())
    except ValueError:
         messagebox.showerror("Error", "哈希次数必须是一个整数")
         return
    try:
        generate_count = int(generate_count_entry.get())
    except ValueError:
        messagebox.showerror("Error", "生成数量必须是一个整数")
        return


    initial_passphrase = passphrase

    for _ in range(hash_times):
        if salt:
            passphrase = passphrase + salt
        bytes_passphrase = passphrase.encode('utf-8')
        passphrase = sha256(bytes_passphrase).hexdigest()

    hex_passphrase = "0x" + bytes_passphrase.hex()

    nostr_keys = generate_nostr_keys(initial_passphrase, generate_count, salt, hash_times)

    clear_all_results()

    update_text_entry(hex_entry, hex_passphrase)
    update_text_entry(hash_entry, passphrase)

    nostr_result_text.config(state=tk.NORMAL)
    for private_key, public_key in nostr_keys:
        nostr_result_text.insert(tk.END, f"{private_key}\n{public_key}\n")
    nostr_result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Nostr Brain Address Generator by @btcdage / Nostr脑地址生成器 by @囤饼达")
root.geometry("800x800")

main_frame = ttk.Frame(root, padding=10)
main_frame.pack(fill="both", expand=True)


title_label = ttk.Label(main_frame, text="Nostr Brain Address Generator / Nostr脑地址生成器", font=("Arial", 16))
title_label.pack(side="top", pady=5)

passphrase_label = ttk.Label(main_frame, text="Passphrase / 脑口令:")
passphrase_label.pack(side="top", pady=3)
passphrase_entry = ttk.Entry(main_frame, width=80,)
passphrase_entry.pack(side="top", pady=3)

salt_label = ttk.Label(main_frame, text="Salt / 加盐:")
salt_label.pack(side="top", pady=3)
salt_entry = ttk.Entry(main_frame, width=80)
salt_entry.pack(side="top", pady=3)

hash_times_label = ttk.Label(main_frame, text="Hash Times / 哈希次数 (1-10000):")
hash_times_label.pack(side="top", pady=3)
hash_times_entry = ttk.Entry(main_frame, width=10, validate="key")
hash_times_entry['validatecommand'] = (hash_times_entry.register(validate_hash_times), '%P')
hash_times_entry.pack(side="top", pady=3)
hash_times_entry.insert(0, "1")

generate_count_label = ttk.Label(main_frame, text="Generate Count / 生成数量(1-1000):")
generate_count_label.pack(side="top", pady=3)
generate_count_entry = ttk.Entry(main_frame, width=10, validate="key")
generate_count_entry['validatecommand'] = (generate_count_entry.register(validate_generate_count), '%P')
generate_count_entry.pack(side="top", pady=3)
generate_count_entry.insert(0, "1")

generate_button = ttk.Button(main_frame, text="Generate Nostr Keys / 生成 Nostr 密钥", command=generate_brain_wallet)
generate_button.pack(side="top", pady=3)
clear_button = ttk.Button(main_frame, text="Clear All / 清空所有", command=clear_all_results)
clear_button.pack(side="top", pady=10)

hex_hash_frame = ttk.Frame(main_frame)
hex_hash_frame.pack(fill="x",expand=True)

hex_entry= create_readonly_entry("字节化","Hexadecimal Encoding:", hex_hash_frame)
hash_entry= create_readonly_entry("SHA-256哈希:","SHA-256 Hash:", hex_hash_frame)

nostr_result_label = ttk.Label(main_frame, text="Nostr Keys / Nostr 密钥:")
nostr_result_label.pack(side="top", pady=3)

nostr_result_frame = tk.Frame(main_frame)
nostr_result_frame.pack(fill="both", expand=True)

nostr_result_text = Text(nostr_result_frame, wrap=tk.WORD, state=tk.DISABLED,height=10)
nostr_result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_y = Scrollbar(nostr_result_frame, orient=tk.VERTICAL, command=nostr_result_text.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
nostr_result_text.config(yscrollcommand=scrollbar_y.set)

copy_button_nostr = ttk.Button(main_frame, text="Copy Nostr Keys / 复制 Nostr 密钥", command=lambda: copy_to_clipboard(nostr_result_text))
copy_button_nostr.pack(side="top", pady=5)

root.mainloop()
