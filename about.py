#  Main app launch
import tkinter as tk


class About():
    def __init__(self, master, main_notebook):
        self.master = master
        about_page = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(about_page, text='About')

        # About page
        about_frame = tk.Frame(about_page, bg='gray20')
        about_frame.pack(expand=True)

        title_label_1 = tk.Label(about_frame, bg='gray20')
        title_label_1.config(bd=0, text='Software Developed by Marco Fernandes', font='System 30', fg='yellow')
        title_label_1.pack(expand=True, fill=tk.X, anchor=tk.N)

        title_label_2 = tk.Label(about_frame, bg='gray20')
        title_label_2.config(bd=0, text='Component Cost Equations Developed by Robert Platica', font='System 30', fg='yellow')
        title_label_2.pack(expand=True, fill=tk.X, anchor=tk.N)
