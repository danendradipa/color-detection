from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

def show_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if filename: 
        img = Image.open(filename)
        # Image resizing   
        aspect_ratio = img.height / img.width
        target_width = 370
        target_height = int(aspect_ratio * target_width)
        img = img.resize(size=(target_width, target_height))
        img_tk = ImageTk.PhotoImage(img)    
        img_label.configure(image=img_tk, width=360, height=270)   
        img_label.image = img_tk                                        

    
def find_colors():
    if not filename:  # Check if an image has been selected
        return

    colorthief = ColorThief(filename)
    palette = colorthief.get_palette(color_count=12)

    # Update color circles and hex labels
    for i, color in enumerate(palette):
        hex_color = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
        if i < 6:  # Left palette
            colors_left.itemconfig(colors_left_circles[i], fill=hex_color)
            hex_labels_left[i].config(text=hex_color)
        else:  # Right palette
            colors_right.itemconfig(colors_right_circles[i - 6], fill=hex_color)
            hex_labels_right[i - 6].config(text=hex_color)

# --------------------------------- UI SET UP -------------------------- #
window = Tk()
window.title("IMAGE COLOR DETECTOR")
window.geometry('900x600')
window.config(bg="#f0e68c")  # Light yellow background
window.resizable(False, False)

# UI ICON
icon = PhotoImage(file="logo.png")  # Ensure the icon file is available
window.iconphoto(False, icon)

# HEADER
header_frame = Frame(window, bg='darkorange', pady=10)
header_frame.pack(fill=X)

header_label = Label(header_frame, text='Image Color Detector', font='Arial 24 bold', bg='darkorange', fg='white')
header_label.pack()

# COLOR PICKER FRAME
frame = Frame(window, bg='lightblue', bd=5)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# COLOR PALETTE LEFT
colors_left = Canvas(frame, bg='lightblue', width=150, height=280, highlightthickness=0)
colors_left.grid(row=0, column=0, padx=10, pady=10)

colors_left_circles = []
hex_labels_left = []
for i in range(6):
    circle = colors_left.create_oval((10, 10 + i * 40, 40, 50 + i * 40), fill='black')
    label = Label(colors_left, text='#000000', fg='#000', font='Arial 10 bold', bg='lightblue')
    label.place(x=50, y=15 + i * 40)
    colors_left_circles.append(circle)
    hex_labels_left.append(label)

# COLOR PALETTE RIGHT
colors_right = Canvas(frame, bg='lightblue', width=150, height=280, highlightthickness=0)
colors_right.grid(row=0, column=1, padx=10, pady=10)

colors_right_circles = []
hex_labels_right = []
for i in range(6):
    circle = colors_right.create_oval((10, 10 + i * 40, 40, 50 + i * 40), fill='black')
    label = Label(colors_right, text='#000000', fg='#000', font='Arial 10 bold', bg='lightblue')
    label.place(x=50, y=15 + i * 40)
    colors_right_circles.append(circle)
    hex_labels_right.append(label)

# IMAGE SELECTION BOX
selection_frame = Frame(frame, bg='lightgreen', bd=5)
selection_frame.grid(row=0, column=2, padx=10, pady=10)

# PIC DISPLAY
pic_frame = Frame(selection_frame, bd=3, width=370, height=280, bg='black', relief=GROOVE)
pic_frame.pack(pady=10)

img_label = Label(pic_frame, bg='black')
img_label.place(x=0, y=0)

# BUTTONS
button_frame = Frame(selection_frame, bg='lightgreen')
button_frame.pack(pady=10)

selectimage_btn = Button(button_frame, text='Select Image', width=15, height=2, font='Arial 12 bold', bg="lightcoral", command=show_image)
selectimage_btn.grid(row=0, column=0, padx=5)

find_colors_btn = Button(button_frame, text='Find Colors', width=15, height=2, font='Arial 12 bold', bg="lightcoral", command=find_colors)
find_colors_btn.grid(row=0, column=1, padx=5)

window.mainloop()