import customtkinter
import tkinter as tk

windows =  tk.Tk()

# customtkinter.set_appearance_mode('dark')
# customtkinter.set_default_color_theme("dark-blue")

width = 500
height = 300
windows.geometry(f'{width}x{height}')

def click():
    print('Log true')


text = customtkinter.CTkLabel(windows, text='Fazer login')
text.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(windows,placeholder_text='Email')
email.pack(padx=10, pady=10)

password = customtkinter.CTkEntry(windows, placeholder_text='Password', show='*')
password.pack(padx=5,pady=5)

button = customtkinter.CTkButton(windows,text='Login', command=click)
button.pack(padx=10, pady=10)




windows.mainloop()