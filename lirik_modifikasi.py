import tkinter as tk

# Tempel potongan lirikmu di sini
lyrics = [
    "The same song on repeat",
    "You can call me anything you want",
    "It's fine by me",
    "Number two out of three",
    "He says that it's his favorite",
    "And I can't disagree"
]

root = tk.Tk()
root.title("Anything You Want")
root.geometry("900x600")
root.configure(bg="#090909")

title = tk.Label(
    root,
    text="Anything You Want",
    font=("Helvetica", 24, "bold"),
    fg="#d94f70",
    bg="#090909"
)
title.pack(pady=(25, 0))

artist = tk.Label(
    root,
    text="Reality Club",
    font=("Helvetica", 12),
    fg="#888",
    bg="#090909"
)
artist.pack()

container = tk.Frame(root, bg="#090909")
container.pack(expand=True, fill="both", padx=40, pady=20)

bubble = tk.Label(
    container,
    font=("Helvetica", 22, "bold"),
    wraplength=550,
    padx=25,
    pady=18,
    fg="white"
)

index = 0

def typewriter(text, i=0):
    bubble.config(text=text[:i])

    if i < len(text):
        root.after(35, lambda: typewriter(text, i + 1))

def show():

    global index

    bubble.pack_forget()

    if index % 2 == 0:
        bubble.configure(
            bg="#181818",
            justify="left"
        )
        bubble.pack(anchor="w", pady=12)

    else:
        bubble.configure(
            bg="#74263d",
            justify="left"
        )
        bubble.pack(anchor="e", pady=12)

    typewriter(lyrics[index])

    index = (index + 1) % len(lyrics)

    root.after(2600, show)

show()
root.mainloop()