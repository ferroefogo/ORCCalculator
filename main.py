#  Main app launch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3
import re

bg = 'gray20'
fg = 'yellow'


# Connect to database
with sqlite3.connect('ComponentData.db') as db:
    c = db.cursor()


def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped


class ComponentCreation(tk.Frame):
    @counted
    def __init__(self, top, mid1, mid2, mid3, bottom, name_var_list, metric_var_list, metric_var_name, quantity_var_list, i, name_iter_list):
        #  frame = frame that is connected to the notebook heading related.
        #  num = number of components they want to enter.
        count = self.__init__.calls

        self.name_var_list = name_var_list
        self.metric_var_list = metric_var_list
        self.quantity_var_list = quantity_var_list

        self.name_iter_list = name_iter_list

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

        if children_total < 30:
            tk.Frame.__init__(self, frame, bg='gray20')
            self.pack(side=tk.LEFT, padx=5, pady=5)

            comp_canvas = tk.Canvas(self, width=200, height=200, relief=tk.RIDGE, bd=1, bg='gray15')
            comp_canvas.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=15)

            title_lbl = tk.Label(comp_canvas, text='Component Information %d' % count, fg=fg, bg='gray25')
            title_lbl.pack()

            # Component Name
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

            # Component Metric
            metric_frame = tk.Frame(comp_canvas, relief=tk.FLAT, bd=0, bg='gray15')
            metric_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True) 

            metric_lbl = tk.Label(metric_frame, relief=tk.FLAT, bd=0, bg='gray15')
            metric_lbl.config(bd=0, text='%s' % metric_var_name, font='System 6', fg=fg)
            metric_lbl.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

            metric_reg = frame.register(self.metric_validate)

            self.metric_var = tk.DoubleVar()
            self.metric_var.set('0.0')

            metric_entry = ttk.Entry(metric_frame, textvariable=self.metric_var, validate="key", validatecommand=(metric_reg, '%P'))
            metric_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

            # Component Quantity
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

            remove_btn = ttk.Label(self, text='Remove')
            remove_btn.pack(pady=5)
            remove_btn.bind("<Button-1>", self._destroy)

            self.top_widgets = top.winfo_children()

            # Append vars into a list
            self.name_var_list.append(self.name_var)
            self.metric_var_list.append(self.metric_var)
            self.quantity_var_list.append(self.quantity_var)

            self.name_iter_list.append(name_entry["textvariable"])

        elif children_total == 30:
            ms.showerror('Error', 'You cannot create more than 30 components', icon='error')

    def _destroy(self, event):
        # Get the parent window of the event widget
        event_parent_name = event.widget.winfo_parent()

        # Get the instance of the entry field of the name of the componenet within the frame, within the canvas, within the component information frame that the 'Remove' button resides in.
        event_parent_name_entry = event.widget._nametowidget(event_parent_name).winfo_children()[0].winfo_children()[1].winfo_children()[1].cget("textvariable")

        for x in range(len(self.name_iter_list)):
            try:
                if self.name_iter_list[x] == str(event_parent_name_entry):
                    self.name_iter_list.pop(x)
                    self.name_var_list.pop(x)
            except IndexError:
                pass
        self.destroy()

    def name_validate(self, name_inp):
        if name_inp == "":
            return True
        elif name_inp is None:
            return False
        else:
            return True

    def metric_validate(self, metric_inp):
        try:
            float(metric_inp)
        except Exception:
            return False
        return True

    def quantity_validate(self, quantity_inp):
        if quantity_inp.isdigit():
            quantity_inp_lencheck = ''.join(quantity_inp)
            if quantity_inp_lencheck[0] == '0':
                return False
            else:
                return True
        elif quantity_inp == "":
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
        self.main_notebook = main_notebook
        self.turbines_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(self.turbines_page, text='Turbines')

        self.i = 0

        # Frame Rows
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

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.turbines_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        self.name_var_list = []
        self.power_var_list = []
        self.quantity_var_list = []

        self.name_iter_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):", self.quantity_var_list, self.i, self.name_iter_list)

    def info_press(self):
        # Remove now destroyed component fields from component value lists.
        self.total_turbine_cost = 0
        already_called = 0
        # Calculate total cost of components within section using specialised formulae
        for i in range(len(self.name_var_list)):
            if self.name_var_list[i].get() == '':
                ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                already_called += 1
                if already_called == 1:
                    break

            if self.quantity_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Quantity Field empty.', icon='error')
            elif isinstance(self.quantity_var_list[i].get(), int) is not True:
                ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
            if self.power_var_list[i].get() == '' or self.power_var_list[i].get() == 0.0:
                ms.showerror('Error', 'You left a Power Field empty.', icon='error')
            elif isinstance(self.power_var_list[i].get(), float) is not True:
                ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
            else:
                # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 1:
                    self.turbine_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                    self.turbine_quantity_cost = self.turbine_cost * self.quantity_var_list[i].get()
                    self.total_turbine_cost += self.turbine_quantity_cost

                    # Find next highest id
                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                    highest_val = [x[0] for x in select_highest_val][0]

                    if highest_val is None:
                        # Write information to database
                        c.execute('INSERT INTO ComponentData(id, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?)', (self.name_var_list[i].get(), self.power_var_list[i].get(), self.quantity_var_list[i].get(), round(self.turbine_cost, 2), round(self.total_turbine_cost, 2)))
                        db.commit()
                    else:
                        # Write information to database
                        c.execute('INSERT INTO ComponentData(id, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?)', (highest_val, self.name_var_list[i].get(), self.power_var_list[i].get(), self.quantity_var_list[i].get(), round(self.turbine_cost, 2), round(self.total_turbine_cost, 2)))
                        db.commit()
                    ms.showinfo('Success', 'System Cost Updated.')


class HeatExchangers():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook
        hx_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(hx_page, text='Heat Exchangers')

        self.sub_notebook = ttk.Notebook(hx_page)
        self.sub_notebook.pack(expand=True, fill=tk.BOTH)

        self.snt(self.sub_notebook)
        self.plate(self.sub_notebook)
        self.acc(self.sub_notebook)

    def snt(self, sub_notebook):
        hx_snt_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_snt_page, text="Shell and Tube")

        self.i = 0

        # Frame Rows
        self.snt_top_frame = tk.Frame(hx_snt_page, bg='gray25')
        self.snt_top_frame.pack(expand=True, fill=tk.BOTH)

        self.snt_mid1_frame = tk.Frame(hx_snt_page, bg='gray23')
        self.snt_mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.snt_mid2_frame = tk.Frame(hx_snt_page, bg='gray21')
        self.snt_mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.snt_mid3_frame = tk.Frame(hx_snt_page, bg='gray19')
        self.snt_mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.snt_bottom_frame = tk.Frame(hx_snt_page, bg='gray17')
        self.snt_bottom_frame.pack(expand=True, fill=tk.BOTH)

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(hx_snt_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.snt_num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        self.name_var_list = []
        self.area_var_list = []
        self.quantity_var_list = []

    def plate(self, sub_notebook):
        hx_plate_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_plate_page, text="Plate")

        self.i = 0

        # Frame Rows
        self.plate_top_frame = tk.Frame(hx_plate_page, bg='gray25')
        self.plate_top_frame.pack(expand=True, fill=tk.BOTH)

        self.plate_mid1_frame = tk.Frame(hx_plate_page, bg='gray23')
        self.plate_mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.plate_mid2_frame = tk.Frame(hx_plate_page, bg='gray21')
        self.plate_mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.plate_mid3_frame = tk.Frame(hx_plate_page, bg='gray19')
        self.plate_mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.plate_bottom_frame = tk.Frame(hx_plate_page, bg='gray17')
        self.plate_bottom_frame.pack(expand=True, fill=tk.BOTH)

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(hx_plate_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.plate_num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        self.name_var_list = []
        self.area_var_list = []
        self.quantity_var_list = []

    def acc(self, sub_notebook):
        hx_acc_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_acc_page, text="Air-Cooled Condenser")

        self.i = 0

        # Frame Rows
        self.acc_top_frame = tk.Frame(hx_acc_page, bg='gray25')
        self.acc_top_frame.pack(expand=True, fill=tk.BOTH)

        self.acc_mid1_frame = tk.Frame(hx_acc_page, bg='gray23')
        self.acc_mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.acc_mid2_frame = tk.Frame(hx_acc_page, bg='gray21')
        self.acc_mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.acc_mid3_frame = tk.Frame(hx_acc_page, bg='gray19')
        self.acc_mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.acc_bottom_frame = tk.Frame(hx_acc_page, bg='gray17')
        self.acc_bottom_frame.pack(expand=True, fill=tk.BOTH)

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(hx_acc_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.acc_num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        self.name_var_list = []
        self.area_var_list = []
        self.quantity_var_list = []

    def snt_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.snt_top_frame, self.snt_mid1_frame, self.snt_mid2_frame, self.snt_mid3_frame, self.snt_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i)

    def plate_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.plate_top_frame, self.plate_mid1_frame, self.plate_mid2_frame, self.plate_mid3_frame, self.plate_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i)

    def acc_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.acc_top_frame, self.acc_mid1_frame, self.acc_mid2_frame, self.acc_mid3_frame, self.acc_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i)

    def info_press(self):
        self.total_snt_cost = 0
        self.total_plate_cost = 0
        self.total_acc_cost = 0
        already_called = 0
        # Calculate total cost of components within section using specialised formulae
        for i in range(len(self.name_var_list)):
            if self.name_var_list[i].get() == '':
                ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                already_called += 1
                if already_called == 1:
                    break
            elif isinstance(self.area_var_list[i].get(), float) != True:
                ms.showerror('Error', 'Please enter a valid number in the Area Field.', icon='error')
            else:
                if self.main_notebook.index(self.main_notebook.select()) == 2:
                    if self.sub_notebook.index(self.sub_notebook.select()) == 0:
                        # Shell and Tube
                        self.snt_cost = (627.6 * self.area_var_list[i].get() ** 0.9199)
                        self.snt_quantity_cost = self.snt_cost * self.quantity_var_list[i].get()
                        self.total_snt_cost +=self.snt_quantity_cost

                    elif self.sub_notebook.index(self.sub_notebook.select()) == 1:
                        # Plate
                        self.plate_cost = (2667.7 * self.area_var_list[i].get() ** 0.3472)
                        self.plate_quantity_cost = self.plate_cost * self.quantity_var_list[i].get()
                        self.total_plate_cost +=self.plate_quantity_cost

                    elif self.sub_notebook.index(self.sub_notebook.select()) == 2:
                        # Air-Cooled Condenser
                        self.acc_cost = (1706.2 * self.acc_area_1 ** 0.4301)
                        self.acc_quantity_cost = self.acc_cost * self.quantity_var_list[i].get()
                        self.total_acc_cost +=self.acc_quantity_cost

        ms.showinfo('Success', 'System Cost Updated.')


class Pumps():
    def __init__(self, master, main_notebook):
        self.master = master
        self.pumps_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.pumps_page, text='Pumps')

        self.i = 0

        # Frame Rows
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

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.pumps_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        # Name var list
        self.name_var_list = []
        self.power_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):", self.quantity_var_list, self.i)

    def info_press(self):
        self.total_pump_cost = 0
        already_called = 0
        # Calculate total cost of components within section using specialised formulae
        for i in range(len(self.name_var_list)):
            if self.name_var_list[i].get() == '':
                ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                already_called += 1
                if already_called == 1:
                    break

            if self.quantity_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Quantity Field empty.', icon='error')
            elif isinstance(self.quantity_var_list[i].get(), int) != True:
                ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')

            if self.power_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Power Field empty.', icon='error')
            elif isinstance(self.power_var_list[i].get(), float) != True:
                ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
            else:
                # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 3:
                    self.pump_cost = (1513.4 * self.power_var_list[i].get() ** 0.1946)
                    self.pump_quantity_cost = self.pump_cost * self.quantity_var_list[i].get()
                    self.total_pump_cost += self.pump_quantity_cost
        ms.showinfo('Success', 'System Cost Updated.')


class Expanders():
    def __init__(self, master, main_notebook):
        self.master = master
        self.expanders_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.expanders_page, text='Expanders')

        self.i = 0

        # Frame Rows
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

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.expanders_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        # Name var list
        self.name_var_list = []
        self.power_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):",self.quantity_var_list, self.i)

    def info_press(self):
        self.total_expander_cost = 0
        already_called = 0
        # Calculate total cost of components within section using specialised formulae
        for i in range(len(self.name_var_list)):
            if self.name_var_list[i].get() == '':
                ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                already_called += 1
                if already_called == 1:
                    break

            if self.quantity_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Quantity Field empty.', icon='error')
            elif isinstance(self.quantity_var_list[i].get(), int) != True:
                ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')

            if self.power_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Power Field empty.', icon='error')
            elif isinstance(self.power_var_list[i].get(), float) != True:
                ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
            else:
                # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 4:
                    self.expander_cost = (544 * self.power_var_list[i].get() ** 0.8331)
                    self.expander_quantity_cost = self.expander_cost * self.quantity_var_list[i].get()
                    self.total_expander_cost +=self.expander_quantity_cost
        ms.showinfo('Success', 'System Cost Updated.')


class StorageTanks():
    def __init__(self, master, main_notebook):
        self.master = master
        self.st_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.st_page, text='Storage Tanks')

        self.i = 0

        # Frame Rows
        self.top_frame = tk.Frame(self.st_page, bg='gray25')
        self.top_frame.pack(expand=True, fill=tk.BOTH)

        self.mid1_frame = tk.Frame(self.st_page, bg='gray23')
        self.mid1_frame.pack(expand=True, fill=tk.BOTH)

        self.mid2_frame = tk.Frame(self.st_page, bg='gray21')
        self.mid2_frame.pack(expand=True, fill=tk.BOTH)

        self.mid3_frame = tk.Frame(self.st_page, bg='gray19')
        self.mid3_frame.pack(expand=True, fill=tk.BOTH)

        self.bottom_frame = tk.Frame(self.st_page, bg='gray17')
        self.bottom_frame.pack(expand=True, fill=tk.BOTH)

        # Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.st_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.num_press)
        num_comp_btn.pack()

        # Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        # Name var list
        self.name_var_list = []
        self.volume_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.volume_var_list, "Volume (L):", self.quantity_var_list, self.i)

    def info_press(self):
        self.total_st_cost = 0
        already_called = 0
        # Calculate total cost of components within section using specialised formulae
        for i in range(len(self.name_var_list)):
            if self.name_var_list[i].get() == '':
                ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                already_called += 1
                if already_called == 1:
                    break

            if self.quantity_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Quantity Field empty.', icon='error')
            elif isinstance(self.quantity_var_list[i].get(), int) != True:
                ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')

            if self.volume_var_list[i].get() == '':
                ms.showerror('Error', 'You left a Volume Field empty.', icon='error')
            elif isinstance(self.volume_var_list[i].get(), float) != True:
                ms.showerror('Error', 'Please enter a valid number in the Volume Field.', icon='error')
            else:
                # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 5:
                    self.st_cost = (52.6 * self.st_volume_1 ** 0.5531)
                    self.st_quantity_cost = self.st_cost * self.quantity_var_list[i].get()
                    self.total_st_cost +=self.st_quantity_cost
        ms.showinfo('Success', 'System Cost Updated.')


class Results():
    def __init__(self, master, main_notebook):
        self.master = master
        results_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(results_page, text='Results')

        # RESULTS PAGE
        treeview_frame = tk.Frame(results_page, relief=tk.GROOVE, bd=0, bg='gray15')
        treeview_frame.pack(side=tk.TOP, padx=10, pady=10)

        treeview_label = tk.Label(treeview_frame, relief=tk.GROOVE, bg='gray15')
        treeview_label.config(text='Components Submitted', font='System 6', fg='yellow')
        treeview_label.pack(side=tk.TOP, padx=10, pady=10)

        # Create the columns necessary to display the database in the GUI as a table.
        self.columns = ('Type', 'Name', 'Area/Power/Volume', 'Quantity', 'Individual Cost', 'Quantity x Individual Cost')
        self.treeview = ttk.Treeview(treeview_frame, columns=self.columns, show='headings')
        # Makes the column titles
        self.treeview.column('Type', width=250)
        self.treeview.column('Name', width=100)
        self.treeview.column('Area/Power/Volume', width=200)
        self.treeview.column('Quantity', width=100)
        self.treeview.column('Individual Cost', width=100)
        self.treeview.column('Quantity x Individual Cost', width=250)

        # Fetch values from database
        comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
        comp_values = [x[0] for x in comp_values_fetch]

        for i in range(len(comp_values)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(comp_values_fetch[i][0], comp_values_fetch[i][1], comp_values_fetch[i][2], comp_values_fetch[i][3],
                                             comp_values_fetch[i][4], comp_values_fetch[i][5]))
                i += 1
            except IndexError:
                # Insert an empty string if this error is caught
                self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', ''))
                i += 1
            self.treeview.pack(pady=2, padx=2)
        # For every column in the columns list, make the column able to be
        # sorted alphabetically or numerically by calling the
        # treeview_sort_column function for every column each time the column
        # heading is pressed.
        for col in self.columns:
            self.treeview.heading(col, text=col,
                                  command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))

        results_frame = tk.Frame(results_page)
        results_frame.pack(expand=True, fill=tk.X)

        results_label = tk.Label(results_frame, relief=tk.GROOVE, bg='gray15')
        results_label.config(text='Calculate System Total', font='System 6', fg='yellow')
        results_label.pack(pady=10)

        results_button = tk.Button(results_frame)
        results_button.config(relief=tk.RAISED, bd=5, text='    Calculate    ',
                                 command=self.total_cost_calculate)
        results_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        self.results_label = tk.Label(results_frame, bg='gray15')
        self.results_label.config(bd=0, text='Total System Cost: £0', font='System 6', fg='yellow')
        self.results_label.pack()

        #HELP PAGE

    def total_cost_calculate(self):
        # Get all the total_cost values from the table.
        # Add them all together. BANG!
        total_system_cost = 0

        comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData').fetchall()
        comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
        for individual_cost in comp_values_individual_costs:
            total_system_cost += individual_cost

        self.results_label["text"] = 'Total System Cost: £%.2f' % total_system_cost
        ms.showinfo('Updated', 'Cost has been updated to £%.2f' % total_system_cost)

    # Treeview sorting algorithm
    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: \
            self.treeview_sort_column(tv, col, not reverse))


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

        Home(master, main_notebook)
        Turbines(master, main_notebook)
        HeatExchangers(master, main_notebook) 
        Pumps(master, main_notebook)
        Expanders(master, main_notebook)
        StorageTanks(master, main_notebook)
        Results(master, main_notebook)
        About(master, main_notebook)


def main():
    root = tk.Tk()
    MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
