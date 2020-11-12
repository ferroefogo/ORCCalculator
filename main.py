#Main app launch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




















































class Home():
    def __init__(self, master, main_notebook):
        self.master = master
        home_page = tk.Frame(main_notebook)
        main_notebook.add(home_page, text='Home')

class Turbines():
    def __init__(self, master, main_notebook):
        self.master = master
        turbines_page = tk.Frame(main_notebook)
        main_notebook.add(turbines_page, text='Turbines')

class HeatExchangers():
    def __init__(self, master, main_notebook):
        self.master = master
        hx_page = tk.Frame(main_notebook)
        main_notebook.add(hx_page, text='Heat Exchangers')

class Pumps():
    def __init__(self, master, main_notebook):
        self.master = master
        pumps_page = tk.Frame(main_notebook)
        main_notebook.add(pumps_page, text='Pumps')

class Expanders():
    def __init__(self, master, main_notebook):
        self.master = master
        expanders_page = tk.Frame(main_notebook)
        main_notebook.add(expanders_page, text='Expanders')

class StorageTanks():
    def __init__(self, master, main_notebook):
        self.master = master
        st_page = tk.Frame(main_notebook)
        main_notebook.add(st_page, text='Storage Tanks')

class Results():
    def __init__(self, master, main_notebook):
        self.master = master
        results_page = tk.Frame(main_notebook)
        main_notebook.add(results_page, text='Results')

class About():
    def __init__(self, master, main_notebook):
        self.master = master
        about_page = tk.Frame(main_notebook)
        main_notebook.add(about_page, text='About')

class MainApp():
    def __init__(self, master):
        master.configure(bg='gray15')
        master.title('Component Cost Calculator')
        master.option_add('*Font', 'System 12')
        master.option_add('*Label.Font', 'System 14')
        master.geometry('1920x1080')
        master.wm_state('zoomed')

        global_frame = tk.Frame(master, relief=tk.FLAT, borderwidth=1, bg='gray15')
        global_frame.pack(fill=tk.BOTH, side=tk.TOP)

        global_label = tk.Label(global_frame, relief=tk.GROOVE, bd=1, bg='ghost white')
        global_label.config(text='Component Cost Calculator v3.0', font='System 12')
        global_label.pack(fill=tk.X, anchor=tk.N)

        main_notebook = ttk.Notebook(master)
        main_notebook.pack(fill=tk.BOTH, expand=True)

        HP = Home(master, main_notebook)
        TBP = Turbines(master, main_notebook)
        HXP = HeatExchangers(master, main_notebook) 
        PP = Pumps(master, main_notebook)
        EP = Expanders(master, main_notebook)
        STP = StorageTanks(master, main_notebook)
        RP = Results(master, main_notebook)
        AP = About(master, main_notebook)


def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()