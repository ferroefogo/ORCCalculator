#Main app launch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms




bg='gray20'
fg='yellow'



































def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls+=1
        return f(*args, **kwargs)
    wrapped.calls=0
    return wrapped


class ComponentCreation(tk.Frame):
    @counted
    def __init__(self, top, mid1, mid2, mid3, bottom, name_var_list, metric_var_list, quantity_var_list, i):
        #frame = frame that is connected to the notebook heading related.
        #num = number of components they want to enter.
        count = self.__init__.calls
        self.name_var_list = name_var_list
        self.metric_var_list = metric_var_list
        self.quantity_var_list = quantity_var_list

        top_children = len(top.winfo_children())
        mid1_children = len(mid1.winfo_children())
        mid2_children = len(mid2.winfo_children())
        mid3_children = len(mid3.winfo_children())
        bottom_children = len(bottom.winfo_children())

        children_total = top_children + mid1_children + mid2_children + mid3_children + bottom_children

        if top_children <= 5:
            frame = top
        elif top_children == 6 and mid1_children <= 5:
            frame = mid1
        elif top_children == 6 and mid2_children <= 5:
            frame = mid2
        elif top_children == 6 and mid3_children <= 5:
            frame = mid3
        elif top_children == 6 and bottom_children <= 5:
            frame = bottom
        
        if children_total<30:
            tk.Frame.__init__(self, frame, bg='gray20')
            self.pack(side=tk.LEFT, padx=5, pady=5)

            comp_canvas = tk.Canvas(self, width=200, height=200, relief=tk.RIDGE, bd=1, bg='gray15')
            comp_canvas.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=15)

            title_lbl = tk.Label(comp_canvas, text='Component Information %d' % count, fg=fg, bg='gray25')
            title_lbl.pack()

            #Component Name
            name_frame = tk.Frame(comp_canvas, relief=tk.FLAT, bd=0, bg='gray15')
            name_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

            name_lbl = tk.Label(name_frame, relief=tk.FLAT, bd=0, bg='gray15')
            name_lbl.config(bd=0, text='Name: ', font='System 6', fg=fg)
            name_lbl.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

            name_reg = frame.register(self.name_validate)

            self.name_var = tk.StringVar()
            self.name_var.set('')

            name_entry = ttk.Entry(name_frame, textvariable=self.name_var, validate="key", validatecommand=(name_reg, '%P'))
            name_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

            #Component Metric
            metric_frame = tk.Frame(comp_canvas, relief=tk.FLAT, bd=0, bg='gray15')
            metric_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

            metric_lbl = tk.Label(metric_frame, relief=tk.FLAT, bd=0, bg='gray15')
            metric_lbl.config(bd=0, text='Power (kW):', font='System 6', fg=fg)
            metric_lbl.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

            metric_reg = frame.register(self.metric_validate)

            self.metric_var = tk.DoubleVar()
            self.metric_var.set('0.0')

            metric_entry = ttk.Entry(metric_frame, textvariable=self.metric_var, validate="key", validatecommand=(metric_reg, '%P'))
            metric_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

            #Component Quantity
            quantity_frame = tk.Frame(comp_canvas, relief=tk.FLAT, bd=0, bg='gray15')
            quantity_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

            quantity_lbl = tk.Label(quantity_frame, relief=tk.FLAT, bd=0, bg='gray15')
            quantity_lbl.config(bd=0, text='Quantity: ', font='System 6', fg=fg)
            quantity_lbl.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

            quantity_reg = frame.register(self.quantity_validate)

            self.quantity_var = tk.IntVar()
            self.quantity_var.set('1')

            quantity_entry = ttk.Entry(quantity_frame, textvariable=self.quantity_var, validate="key", validatecommand=(quantity_reg, '%P'))
            quantity_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

            remove_btn = tk.Button(self, text='Remove', command=self._destroy)
            remove_btn.pack(pady=5)

            #Append vars into a list
            self.name_var_list.append(self.name_var)
            self.metric_var_list.append(self.metric_var)
            self.quantity_var_list.append(self.quantity_var)


        elif children_total == 30:
            ms.showerror('Error','You cannot create more than 30 components', icon='error')

    def _destroy(self):
        self.name_var_list.pop(-1)
        self.metric_var_list.pop(-1)
        self.quantity_var_list.pop(-1)
        self.destroy()

    def name_validate(self, name_inp):
        if name_inp is "":
            return True
        elif name_inp is None:
            return False
        else:
            return True 

    def metric_validate(self, metric_inp):
        if metric_inp is "":
            return True
        elif metric_inp is None:
            return False
        else:
            return True

    def quantity_validate(self, quantity_inp):
        if quantity_inp.isdigit():
            quantity_inp_lencheck = ''.join(quantity_inp)
            if quantity_inp_lencheck[0] == '0':
                return False
            else:
                return True
        elif quantity_inp is "":
            return True
        elif quantity_inp is None:
            return True
        else:
            return False

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

        #Frame Rows
        self.top_frame = tk.Frame(self.turbines_page, bg='gray25')
        self.top_frame.pack(expand=True, fill=tk.BOTH)

        self.mid1_frame = tk.Frame(self.turbines_page, bg='gray23')
        self.mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.mid2_frame = tk.Frame(self.turbines_page, bg='gray21')
        self.mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.mid3_frame = tk.Frame(self.turbines_page, bg='gray19')
        self.mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = tk.Frame(self.turbines_page, bg='gray17')
        self.bottom_frame.pack(expand=True, fill=tk.BOTH)

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.turbines_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        #Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        
        self.name_var_list = []
        self.power_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, self.quantity_var_list, self.i)

    def info_press(self):
        already_called = 0
        for i in range(len(self.name_var_list)):
            self.name_var_list[i].get()
            if self.name_var_list[i].get() == '':
                ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                already_called += 1
                if already_called == 1:
                    break
            try:
                self.power_var_list[i].get()
                if self.power_var_list[i].get() == '':
                    ms.showerror('Error', 'You left a Power Field empty.', icon='error')
            except Exception:
                ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
            try:
                self.quantity_var_list[i].get()
            except Exception:
                ms.showerror('Error', 'You left a Quantity Field empty.', icon='error')



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
        self.pumps_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.pumps_page, text='Pumps')

        self.i=0

        #Frame Rows
        self.top_frame = tk.Frame(self.pumps_page, bg='gray25')
        self.top_frame.pack(expand=True, fill=tk.BOTH)

        self.mid1_frame = tk.Frame(self.pumps_page, bg='gray23')
        self.mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.mid2_frame = tk.Frame(self.pumps_page, bg='gray21')
        self.mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.mid3_frame = tk.Frame(self.pumps_page, bg='gray19')
        self.mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = tk.Frame(self.pumps_page, bg='gray17')
        self.bottom_frame.pack(expand=True, fill=tk.BOTH)

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.pumps_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        #Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        #Name var list
        self.name_var_list = []
        self.power_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, self.quantity_var_list, self.i)

    def info_press(self):
        print(self.name_var_list)
        for i in range(len(self.name_var_list)):
            comp_name = self.name_var_list[i].get()
            try:
                comp_metric = self.power_var_list[i].get()
            except Exception:
                ms.showerror('Error', 'Please enter a valid number in the Power Field.')
            try:
                comp_quantity = self.quantity_var_list[i].get()
            except Exception:
                comp_quantity = 1

class Expanders():
    def __init__(self, master, main_notebook):
        self.master = master
        self.expanders_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.expanders_page, text='Expanders')

        self.i=0

        #Frame Rows
        self.top_frame = tk.Frame(self.expanders_page, bg='gray25')
        self.top_frame.pack(expand=True, fill=tk.BOTH)

        self.mid1_frame = tk.Frame(self.expanders_page, bg='gray23')
        self.mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.mid2_frame = tk.Frame(self.expanders_page, bg='gray21')
        self.mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.mid3_frame = tk.Frame(self.expanders_page, bg='gray19')
        self.mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = tk.Frame(self.expanders_page, bg='gray17')
        self.bottom_frame.pack(expand=True, fill=tk.BOTH)

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.expanders_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        #Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        #Name var list
        self.name_var_list = []
        self.power_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, self.quantity_var_list, self.i)

    def info_press(self):
        print(self.name_var_list)
        for i in range(len(self.name_var_list)):
            comp_name = self.name_var_list[i].get()
            try:
                comp_metric = self.power_var_list[i].get()
            except Exception:
                ms.showerror('Error', 'Please enter a valid number in the Power Field.')
            try:
                comp_quantity = self.quantity_var_list[i].get()
            except Exception:
                comp_quantity = 1

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