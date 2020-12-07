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
    def __init__(self, top, mid1, mid2, mid3, bottom, name_var_list, metric_var_list, metric_var_name, quantity_var_list, i):
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
            metric_lbl.config(bd=0, text='%s'%metric_var_name, font='System 6', fg=fg)
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
        print(type(metric_inp))
        try:
            float(metric_inp)
        except:
            return False
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
        self.main_notebook = main_notebook
        self.turbines_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(self.turbines_page, text='Turbines')

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
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):",self.quantity_var_list, self.i)

    def info_press(self):
        
        self.total_turbine_cost = 0
        already_called = 0
        #Calculate total cost of components within section using specialised formulae
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
                #Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 1:
                    self.turbine_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                    self.turbine_quantity_cost = self.turbine_cost * self.quantity_var_list[i].get()
                    self.total_turbine_cost +=self.turbine_quantity_cost

        ms.showinfo('Success','System Cost Updated.')
        



class HeatExchangers():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook
        hx_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(hx_page, text='Heat Exchangers')


        self.sub_notebook = ttk.Notebook(hx_page)
        self.sub_notebook.pack(expand=True, fill=tk.BOTH)

        SHELL_N_TUBE = self.snt(self.sub_notebook)
        PLATE = self.plate(self.sub_notebook)
        AIR_COOLED_CONDENSER = self.acc(self.sub_notebook)

    def snt(self, sub_notebook):
        hx_snt_page = tk.Frame(sub_notebook, bg=bg)
        sub_notebook.add(hx_snt_page, text="Shell and Tube")

        self.i=0

        #Frame Rows
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

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(hx_snt_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.snt_num_press)
        num_comp_btn.pack()

        #Retrieve Information
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

        self.i=0

        #Frame Rows
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

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(hx_plate_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.plate_num_press)
        num_comp_btn.pack()

        #Retrieve Information
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

        self.i=0

        #Frame Rows
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

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(hx_acc_page, relief=tk.FLAT, bd=0, bg='gray15')
        comp_frame.pack(side=tk.BOTTOM, anchor=tk.S, expand=True, pady=5, padx=5)

        num_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        num_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        num_comp_btn = ttk.Button(comp_frame, text='Add Component', command=self.acc_num_press)
        num_comp_btn.pack()

        #Retrieve Information
        info_btn_frame = tk.Frame(comp_frame, relief=tk.FLAT, bd=0, bg='gray15')
        info_btn_frame.pack(side=tk.TOP, anchor=tk.N)

        info_comp_btn = ttk.Button(comp_frame, text='Confirm Information', command=self.info_press)
        info_comp_btn.pack(side=tk.TOP, anchor=tk.E)

        self.name_var_list = []
        self.area_var_list = []
        self.quantity_var_list = []


    def snt_num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.snt_top_frame, self.snt_mid1_frame, self.snt_mid2_frame, self.snt_mid3_frame, self.snt_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i)

    def plate_num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.plate_top_frame, self.plate_mid1_frame, self.plate_mid2_frame, self.plate_mid3_frame, self.plate_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i)

    def acc_num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.acc_top_frame, self.acc_mid1_frame, self.acc_mid2_frame, self.acc_mid3_frame, self.acc_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i)

    def info_press(self):
        self.total_snt_cost = 0
        self.total_plate_cost = 0
        self.total_acc_cost = 0
        already_called = 0
        #Calculate total cost of components within section using specialised formulae
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
                        #Shell and Tube
                        self.snt_cost = (627.6 * self.area_var_list[i].get() ** 0.9199)
                        self.snt_quantity_cost = self.snt_cost * self.quantity_var_list[i].get()
                        self.total_snt_cost +=self.snt_quantity_cost

                    elif self.sub_notebook.index(self.sub_notebook.select()) == 1:
                        #Plate
                        self.plate_cost = (2667.7 * self.area_var_list[i].get() ** 0.3472)
                        self.plate_quantity_cost = self.plate_cost * self.quantity_var_list[i].get()
                        self.total_plate_cost +=self.plate_quantity_cost

                    elif self.sub_notebook.index(self.sub_notebook.select()) == 2:
                        #Air-Cooled Condenser
                        self.acc_cost = (1706.2 * self.acc_area_1 ** 0.4301)
                        self.acc_quantity_cost = self.acc_cost * self.quantity_var_list[i].get()
                        self.total_acc_cost +=self.acc_quantity_cost

        ms.showinfo('Success','System Cost Updated.')

    

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
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):", self.quantity_var_list, self.i)

    def info_press(self):
        self.total_pump_cost = 0
        already_called = 0
        #Calculate total cost of components within section using specialised formulae
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
                #Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 3:
                    self.pump_cost = (1513.4 * self.power_var_list[i].get() ** 0.1946)
                    self.pump_quantity_cost = self.pump_cost * self.quantity_var_list[i].get()
                    self.total_pump_cost +=self.pump_quantity_cost
        ms.showinfo('Success','System Cost Updated.')

    

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
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):",self.quantity_var_list, self.i)

    def info_press(self):
        self.total_expander_cost = 0
        already_called = 0
        #Calculate total cost of components within section using specialised formulae
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
                #Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 4:
                    self.expander_cost = (544 * self.power_var_list[i].get() ** 0.8331)
                    self.expander_quantity_cost = self.expander_cost * self.quantity_var_list[i].get()
                    self.total_expander_cost +=self.expander_quantity_cost
        ms.showinfo('Success','System Cost Updated.')

class StorageTanks():
    def __init__(self, master, main_notebook):
        self.master = master
        self.st_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(self.st_page, text='Storage Tanks')

        self.i=0

        #Frame Rows
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

        #Entry field to enter how many turbines you want.
        comp_frame = tk.Frame(self.st_page, relief=tk.FLAT, bd=0, bg='gray15')
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
        self.volume_var_list = []
        self.quantity_var_list = []

    def num_press(self):
        self.i+=1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.volume_var_list, "Volume (L):", self.quantity_var_list, self.i)

    def info_press(self):
        self.total_st_cost = 0
        already_called = 0
        #Calculate total cost of components within section using specialised formulae
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
                #Check if its the Turbine Page to calculate the correct results for the turbine costs.
                if self.main_notebook.index(self.main_notebook.select()) == 5:
                    self.st_cost = (52.6 * self.st_volume_1 ** 0.5531)
                    self.st_quantity_cost = self.st_cost * self.quantity_var_list[i].get()
                    self.total_st_cost +=self.st_quantity_cost
        ms.showinfo('Success','System Cost Updated.')

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