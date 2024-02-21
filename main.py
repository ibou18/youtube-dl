import tkinter as tk
import customtkinter
from pytube import YouTube

import os
print(os.getcwd())



def progress_function(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size
    title = stream.title
    progress_bar.set(progress * 100)

def download_video():
    try:
        url = url_var.get()
        yt = YouTube(url, on_progress_callback=progress_function)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Download complete")
    except Exception as e:
        print("Erreur lors du téléchargement de la vidéo : ", e)
        
# print(dir(customtkinter))
#System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


#Create window
app = customtkinter.CTk()
app.geometry("900x800")
app.title("Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Youtube Downloader", font=("Arial", 24))
title.pack(padx=10, pady=10)


url_var = tk.StringVar()
url_var.set("https://youtu.be/p1XNUFa1RWw?si=EibP9ciPkLm07URa")
link = customtkinter.CTkEntry(app, width=400, height=50, font=("century gothic", 14), textvariable=url_var)
link.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=download_video)
download.pack(padx=10, pady=10)


progress_bar = customtkinter.CTkProgressBar(app, width=400, height=10)
progress_bar.pack(padx=10, pady=10)


def button_function():
    print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()


    
    