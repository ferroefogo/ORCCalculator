#Main app launch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox




bg='gray20'







































class ComponentCreation(tk.Frame):
    def __init__(self, frame, i, func):
        self.func = func
        #frame = frame that is connected to the notebook heading related.
        #num = number of components they want to enter.
        tk.Frame.__init__(self, frame)
        lbl = tk.Label(self, text='Component Information %d' % i)
        btn = tk.Button(self, text='Remove', command=self.destroy)
        lbl.pack()
        btn.pack()
        self.pack(side=tk.LEFT, padx=5)
        i+=1
        
    def __call__(self, *args, **kwargs):
        self.count +=1
        return self.func

class Home():
    def __init__(self, master, main_notebook):
        self.master = master
        home_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(home_page, text='Home')


class Turbines():
    def __init__(self, master, main_notebook):
        self.master = master
        self.turbines_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.turbines_page, text='Turbines')

        self.i=0

        #Entry field to enter how many turbines you want.
        num_comp_frame = tk.Frame(self.turbines_page, relief=tk.FLAT, bd=0, bg='gray15')
        num_comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(num_comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(num_comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()


    def num_press(self):
        self.i+=1
        c = ComponentCreation(self.turbines_page, self.i)


class HeatExchangers():
    def __init__(self, master, main_notebook):
        self.master = master
        hx_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(hx_page, text='Heat Exchangers')


        sub_notebook = ttk.Notebook(hx_page)
        sub_notebook.pack(expand=True, fill=tk.BOTH)

        #
        hx_snt_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_snt_page, text="Shell and Tube")

        hx_plate_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_plate_page, text="Plate")

        hx_acc_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_acc_page, text="Air-Cooled Condenser")

class Pumps():
    def __init__(self, master, main_notebook):
        self.master = master
        pumps_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(pumps_page, text='Pumps')

class Expanders():
    def __init__(self, master, main_notebook):
        self.master = master
        expanders_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(expanders_page, text='Expanders')

class StorageTanks():
    def __init__(self, master, main_notebook):
        self.master = master
        st_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(st_page, text='Storage Tanks')

class Results():
    def __init__(self, master, main_notebook):
        self.master = master
        results_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(results_page, text='Results')

class About():
    def __init__(self, master, main_notebook):
        self.master = master
        about_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(about_page, text='About')

class MainApp():
    def __init__(self, master):
        master.configure(bg='gray15')
        master.title('Component Cost Calculator')
        master.option_add('*Font', 'System 12')
        master.option_add('*Label.Font', 'System 14')
        master.geometry('1920x1080')
        master.wm_state('zoomed')

        global_frame = tk.Frame(master, relief=tk.FLAT, bd=1, bg='gray15')
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