import customtkinter as ctk
from PIL import Image
import requests


ctk.set_appearance_mode('Dark')
ctk.set_default_color_theme('dark-blue')

def Weather(label, frame):
    api_key = '8088069684d79e46ed0b1c9994a3f0e3'
    city = label.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp'] - 273.15 #) * 9/4 + 32 (fahrenheit)
        desc = data['weather'][0]['description']

        weather_entry = ctk.CTkEntry(frame, width=200, height=50)
        weather_entry.pack(pady=20)
        weather_entry.insert(0, f'Temp: {temp}°C, Desc: {desc}')
        weather_entry.configure(state='disabled')


def main(root):
    for widget in root.winfo_children():
        widget.destroy()

    #weatherimage = ctk.CTkImage(dark_image=Image.open('weather02-512.webp'), size=(50, 50))
    #image_label = ctk.CTkLabel(root, image=weatherimage, text='')
    #image_label.image = weatherimage
    #image_label.pack(anchor='n', padx=(10,0), pady=(10,0))

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    label = ctk.CTkEntry(frame, placeholder_text='Enter State')
    label.pack(pady=12, padx= 10)

    button = ctk.CTkButton(frame, text='Enter', command=lambda: Weather(label, frame))
    button.pack(pady=12, padx=10)

    root.mainloop()




