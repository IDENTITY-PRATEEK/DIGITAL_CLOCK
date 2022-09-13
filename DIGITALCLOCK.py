#Digital Clock Made Using Python

from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')   #Giving a Better UI
background = "#202324"
foreground= "#c4e4ee"
border_width = 35

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():       # To View Realtime Data on Clock
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digital_clock)

digital_clock()  #to View Output
app_window.mainloop()