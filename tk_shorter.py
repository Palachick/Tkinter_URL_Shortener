import tkinter as tk
import pyshorteners as sh

root = tk.Tk()

#WINDOW SETTINGS
root.title("Shorter URL")
root.resizable(width=False, height=False)
root.geometry("600x300")

#FUNCTIONS
def shortener():
    result_input = url.get()
    shortener = sh.Shortener()
    short_url.replace(1.0, tk.END,shortener.tinyurl.short(result_input))
    btn['bg'] = "#aa0000"

#INTERFACE
header_before_input = tk.Label(text="Enter URL for shorten",font="Consolas 20")
url = tk.Entry(width=25,font="Consolas 20")
btn = tk.Button(text="Shorten URL", command=shortener,font="Consolas 20", bg="#00aa00", fg="#fff")
header_after_input = tk.Label(text="Ready link",font="Consolas 20")
short_url = tk.Text(width=25, height=2,font="Consolas 20")

#PACK
header_before_input.pack(pady=10)
url.pack()
btn.pack(pady=5)
header_after_input.pack(pady=10)
short_url.pack()

#RUN
if __name__ == "__main__":
    root.mainloop()
