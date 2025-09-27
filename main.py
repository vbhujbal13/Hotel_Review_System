#!/usr/bin/env python
"""
_file name_ = main.py
_date created_ = 11/20/2023
_date last modified_ = 12/07/2023
__python version = 3.11
_author_ = "Anagha Ghate - aghate@binghamton.edu",
           "Vishakha Bhujbal - vbhujbal@binghamton.edu"
           "Sarthak Mushrif - smushrif@binghamton.edu"
_status_ = "Development"
"""

import tkinter as tk
import frontend

# Create the main window
root = tk.Tk()
root.title("Hotel Review Analysis")

# Set window size to full screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


def on_button_click1():
    frontend.query1_table()


def on_button_click2():
    frontend.query2_graph()


def on_button_click3():
    frontend.query3_table()


def on_button_click4():
    frontend.query4_table()


# Calculate the number of columns
num_columns = 3  # Total columns

# Create a frame as the container with padding
frame = tk.Frame(root, bg="white", padx=50, pady=20)  # Light gray frame with padding
frame.pack(expand=True)

# Create a label for the heading in the center of the frame
heading_label = tk.Label(frame, text="Hotel Review Analysis", font=("Arial", 20, "bold"), fg="black")
heading_label.grid(row=0, column=0, columnspan=num_columns, pady=(50, 10), sticky='nsew')  # Centered heading

# Button colors and text configurations
button_bg_color = "black"  
button_text_color = "white"  # White text color for buttons
button_font = ("Arial", 14, "bold")  # Bold font for button text

button1 = tk.Button(frame, text="Analysis 1", command=on_button_click1, bg=button_bg_color, fg=button_text_color, font=button_font)
button2 = tk.Button(frame, text="Analysis 2", command=on_button_click2, bg=button_bg_color, fg=button_text_color, font=button_font)
button3 = tk.Button(frame, text="Analysis 3", command=on_button_click3, bg=button_bg_color, fg=button_text_color, font=button_font)
button4 = tk.Button(frame, text="Analysis 4", command=on_button_click4, bg=button_bg_color, fg=button_text_color, font=button_font)

# Arrange the buttons using grid layout in the center
button1.grid(row=1, column=1, pady=10)
button2.grid(row=2, column=1, pady=10)
button3.grid(row=3, column=1, pady=10)
button4.grid(row=4, column=1, pady=10)

# Add information labels for each button
info_label1 = tk.Label(frame, text="Hotel trend according to user's reviews", font=("Arial", 14, "bold"), bg="#F0F0F0")
info_label1.grid(row=1, column=2, pady=20, sticky='w')

info_label2 = tk.Label(frame, text="Season wise hotel ratings categorized by state", font=("Arial", 14, "bold"), bg="#F0F0F0")
info_label2.grid(row=2, column=2, pady=20, sticky='w')

info_label3 = tk.Label(frame, text="Citywise Top hotels", font=("Arial", 14, "bold"), bg="#F0F0F0")
info_label3.grid(row=3, column=2, pady=20, sticky='w')

info_label4 = tk.Label(frame, text="Worthy customer recognition for promotion", font=("Arial", 14, "bold"), bg="#F0F0F0")
info_label4.grid(row=4, column=2, pady=20, sticky='w')

root.mainloop()



