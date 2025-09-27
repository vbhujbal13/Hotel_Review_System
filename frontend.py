#!/usr/bin/env python
"""
_file name_ = frontend.py
"""

import tkinter as tk
from tkinter import ttk
import mongo_conn


def query1_table():
    data = mongo_conn.run_query1()
    print(len(data))
    
    # Create the main window 
    root = tk.Tk()   
    root.title("Hotel Data with trend")

    # Set window size to full screen
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))


    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=('hotel', 'trend', 'avg_rating', 'categories', 'province'), show='headings')

    # Define column names and set them as headings
    tree.heading('hotel', text='Hotel')
    tree.heading('trend', text='Trend')
    tree.heading('avg_rating', text='Average Rating')
    tree.heading('categories', text='Categories')
    tree.heading('province', text='Province')

    # Set a custom style for column headings
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'), foreground='blue')

    # Populate the Treeview with data
    for item in data:
        tree.insert('', 'end', values=(item['hotel'], item['trend'], item['avg_rating'], item['categories'], item['province']))

    # Set column width
    tree.column('hotel', width=200)
    tree.column('trend', width=100)
    tree.column('avg_rating', width=100)
    tree.column('categories', width=200)
    tree.column('province', width=100)

    # Create a vertical scrollbar
    vsb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Pack the Treeview and scrollbar to expand and fill the available space
    tree.pack(expand=True, fill='both', side='left', padx=10, pady=10)
    vsb.pack(fill='y', side='right')

    # Run the Tkinter event loop
    root.mainloop()


def query2_graph():
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt

    def plot_line_graph(monthly_ratings):
        # Destroy existing widgets (if any)
        for widget in root.winfo_children():
            widget.destroy()

        # Create a figure and axis
        fig, ax = plt.subplots()

        # Plot the line graph
        x_data = list(monthly_ratings.keys())
        y_data = list(monthly_ratings.values())
        ax.plot(x_data, y_data, marker='o', linestyle='-')

        # Set labels and title
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title("Monthly ratings")

        # Embed the plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Function to handle button click
    def button_click(monthly_ratings):
        plot_line_graph(monthly_ratings)

    # Create the main window
    root = tk.Tk()
    root.title("States")

    # Fetch data from MongoDB
    data = mongo_conn.run_query2()

    # Limit the number of buttons for demonstration purposes
    data = data[:10]

    # Create buttons dynamically
    for item in data:
        button_text = item["state"]
        monthly_ratings = item["monthly_ratings"]
        button = ttk.Button(root, text=button_text, command=lambda monthly_ratings=monthly_ratings: button_click(monthly_ratings))
        button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()



def query3_table():
    data = mongo_conn.run_query3()
    print(len(data))
    
    # Create the main window 
    root = tk.Tk()   
    root.title("City wise top hotels")

    # Set window size to full screen
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=('city', 'hotel', 'address', 'website', 'averageRating'), show='headings')

    # Define column names and set them as headings
    tree.heading('city', text='City')
    tree.heading('hotel', text='Hotel')
    tree.heading('address', text='Address')
    tree.heading('website', text='Website')
    tree.heading('averageRating', text='Average Rating')

    # Set a custom style for column headings
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'), foreground='blue')

    # Populate the Treeview with data
    for item in data:
        tree.insert('', 'end', values=(item['city'], item['hotel'], item['address'], item['website'], item['averageRating']))

    # Set column width
    tree.column('city', width=100)
    tree.column('hotel', width=200)
    tree.column('address', width=200)
    tree.column('website', width=200)
    tree.column('averageRating', width=100)

    # Create a vertical scrollbar
    vsb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Pack the Treeview and scrollbar to expand and fill the available space
    tree.pack(expand=True, fill='both', side='left', padx=10, pady=10)
    vsb.pack(fill='y', side='right')

    # Run the Tkinter event loop
    root.mainloop()


def query4_table():
    data = mongo_conn.run_query4()
    print(len(data))
    
    # Create the main window 
    root = tk.Tk()   
    root.title("Worthy customer recognition for promotion")

    # Set window size to full screen
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # Create a Treeview widget
    tree = ttk.Treeview(root, columns=('hotel', 'city', 'province', 'username', 'rating', 'date'), show='headings')

    # Define column names and set them as headings    
    tree.heading('hotel', text='Hotel')
    tree.heading('city', text='City')
    tree.heading('province', text='Province')
    tree.heading('username', text='Username')
    tree.heading('rating', text='Rating')
    tree.heading('date', text='Date')

    # Set a custom style for column headings
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'), foreground='blue')

    # Populate the Treeview with data
    for item in data:
        tree.insert('', 'end', values=(item['hotel'], item['city'], item['province'], item['username'], item['rating'], item['date']))

    # Set column width
    tree.column('hotel', width=200)
    tree.column('city', width=100)   
    tree.column('province', width=50) 
    tree.column('username', width=100)
    tree.column('rating', width=100)
    tree.column('date', width=100)

    # Create a vertical scrollbar
    vsb = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    # Pack the Treeview and scrollbar to expand and fill the available space
    tree.pack(expand=True, fill='both', side='left', padx=10, pady=10)
    vsb.pack(fill='y', side='right')

    # Run the Tkinter event loop
    root.mainloop()

