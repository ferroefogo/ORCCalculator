#  Main app launch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3

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

            self.quantity_var = tk.StringVar()
            self.quantity_var.set('1')

            quantity_entry = ttk.Entry(quantity_frame, textvariable=self.quantity_var, validate="key", validatecommand=(quantity_reg, '%P'))
            quantity_entry.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

            remove_btn = ttk.Label(self, text='Remove')
            remove_btn.pack(pady=5)
            remove_btn.bind("<Button-1>", self._destroy)

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
                    self.metric_var_list.pop(x)
                    self.quantity_var_list.pop(x)
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
            return False
        else:
            return False


class Home():
    def __init__(self, master, main_notebook):
        self.master = master
        home_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(home_page, text='Home')

        home_frame = tk.Frame(home_page, bg='gray20')
        home_frame.pack(expand=True, fill=tk.BOTH)

        title_label = tk.Label(home_frame)
        title_label.config(bd=0, text='How to use this software', font='System 30', bg='gray20', fg='yellow')
        title_label.pack(expand=True, fill=tk.BOTH, anchor=tk.N)

        howtouse_frame = tk.Frame(home_frame, bg='gray20')
        howtouse_frame.pack(fill=tk.BOTH, expand=True)

        tip_label_1 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_1.config(bd=0, text="- Each tab shows each component and where said components' information must be entered.\n")
        tip_label_1.pack(side=tk.TOP)

        tip_label_2 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_2.config(bd=0, text='- Create up to 30 components under each tab and enter your information into each.\n')
        tip_label_2.pack(side=tk.TOP)

        tip_label_3 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_3.config(bd=0, text="- Press the 'Enter Information' button once you have made sure all information entered is correct and you want to submit it into the final system cost calculation.\n")
        tip_label_3.pack(side=tk.TOP)

        tip_label_4 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_4.config(bd=0, text="- If you would like to go back and make a change, just edit the component information of the component in question and press the 'Enter Information' button again.\nOR you can edit the name, power/area/volume and quantity values of a component in the Results page's table by LEFT CLICKING the relevant row.")
        tip_label_4.pack(side=tk.TOP)

        tip_label_5 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_5.config(bd=0, text="- If you would like to remove a component from the final calculation, RIGHT CLICK the relevant component row in the Results page's 'Components Submitted' table and select 'Delete'.\n")
        tip_label_5.pack(side=tk.TOP)

        tip_label_6 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_6.config(bd=0, text="- You may press the column headings of the table at the 'Results' table to sort the information alphabetically or numerically.\n")
        tip_label_6.pack(side=tk.TOP)

        tip_label_7 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_7.config(bd=0, text="- The final cost of the system should update as you add components, however if you want to be double sure that the final value displayed is correct, you may use the 'Calculate' button.\n")
        tip_label_7.pack(side=tk.TOP)

        tip_label_8 = tk.Label(howtouse_frame, bg='gray20', fg='yellow')
        tip_label_8.config(bd=0, text="- You may clear the entire database using the 'Clear Database' button. Keep in mind the data stored will be non-retrievable and removed permanently.\n")
        tip_label_8.pack(side=tk.TOP)


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
        self.total_turbine_cost = 0
        already_called = 0
        invalid_entries = []
        _type = 'Turbine'

        if len(self.name_var_list) == 0:
            ms.showerror('Error', 'No components entered.', icon='error')
        else:
            # Calculate total cost of components within section using specialised formulae
            for i in range(len(self.name_var_list)):
                if self.name_var_list[i].get() == '':
                    ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break
                try:
                    if self.quantity_var_list[i].get() == '':
                        ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.power_var_list[i].get() == '' or self.power_var_list[i].get() == 0.0:
                        ms.showerror('Error', 'You left one or more Power Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

            if len(invalid_entries) == 0:
                # Check if the name of the component is equal to any other names in the database.
                comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                comp_names_db = [x[0] for x in comp_names_db_fetch]

                duplicates_count = 0

                for x in range(len(self.name_var_list)):
                    if self.name_var_list[x].get() in comp_names_db:
                        duplicates_count += 1

                if duplicates_count > 0:
                    confirm_duplicate = ms.askquestion("Overwrite Warning", "One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?")
                    if confirm_duplicate == 'no':
                        # Stop the adding of the items to the database
                        ms.showinfo('Success', 'The duplicates have not been added.')
                    else:
                        # Continue letting the items go
                        # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                        for x in range(len(self.name_var_list)):
                            # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                            if self.main_notebook.index(self.main_notebook.select()) == 1:
                                self.turbine_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                                self.turbine_quantity_cost = self.turbine_cost * int(self.quantity_var_list[i].get())
                                self.total_turbine_cost += self.turbine_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.turbine_cost, 2), round(self.total_turbine_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.turbine_cost, 2), round(self.total_turbine_cost, 2)))
                                    db.commit()
                        ms.showinfo('Success', 'System Cost Updated.')
                else:
                    # Continue letting the items go
                    # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                    for i in range(len(self.name_var_list)):
                        self.total_turbine_cost = 0
                        # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                        if self.main_notebook.index(self.main_notebook.select()) == 1:
                            self.turbine_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                            self.turbine_quantity_cost = self.turbine_cost * int(self.quantity_var_list[i].get())
                            self.total_turbine_cost += self.turbine_quantity_cost

                            # Find next highest id
                            select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                            highest_val = [x[0] for x in select_highest_val][0]

                            if highest_val is None:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.turbine_cost, 2), round(self.total_turbine_cost, 2)))
                                db.commit()
                            else:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.turbine_cost, 2), round(self.total_turbine_cost, 2)))
                                db.commit()
                    ms.showinfo('Success', 'System Cost Updated.')

                # Update Results table once this has gone through.
                # Get values from database
                comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
                comp_values = [x[0] for x in comp_values_fetch]

                # Delete the current results page and recreate it.
                self.main_notebook.forget(6)

                r = Results(self.master, self.main_notebook)
                # Clear the table and re-populate it.
                for i in r.treeview.get_children():
                    r.treeview.delete(i)

                # Update Results table once this has gone through.
                for i in range(len(comp_values)):
                    try:
                        r.treeview.insert('', tk.END,
                                             values=(comp_values_fetch[i][0], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4], comp_values_fetch[i][5],
                                                     comp_values_fetch[i][6], comp_values_fetch[i][7]))
                    except IndexError:
                        # Insert an empty string if this error is caught
                        r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
                    r.treeview.pack(pady=2, padx=2)


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

        self.name_iter_list = []

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

        self.name_iter_list = []

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

        self.name_iter_list = []

    def snt_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.snt_top_frame, self.snt_mid1_frame, self.snt_mid2_frame, self.snt_mid3_frame, self.snt_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i, self.name_iter_list)

    def plate_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.plate_top_frame, self.plate_mid1_frame, self.plate_mid2_frame, self.plate_mid3_frame, self.plate_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i, self.name_iter_list)

    def acc_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.acc_top_frame, self.acc_mid1_frame, self.acc_mid2_frame, self.acc_mid3_frame, self.acc_bottom_frame, self.name_var_list, self.area_var_list, "Area (m²):", self.quantity_var_list, self.i, self.name_iter_list)

    def info_press(self):
        self.total_snt_cost = 0
        self.total_plate_cost = 0
        self.total_acc_cost = 0
        already_called = 0
        invalid_entries = []
        _type_snt = 'Shell and Tube'
        _type_plate = 'Plate'
        _type_acc = 'Air-Cooled Condenser'

        if len(self.name_var_list) == 0:
            ms.showerror('Error', 'No components entered.', icon='error')
        else:
            # Calculate total cost of components within section using specialised formulae
            for i in range(len(self.name_var_list)):
                if self.name_var_list[i].get() == '':
                    ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break
                try:
                    if self.quantity_var_list[i].get() == '':
                        ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.area_var_list[i].get() == '':
                        ms.showerror('Error', 'You left one or more Area Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Area Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

            if len(invalid_entries) == 0:
                # Check if the name of the component is equal to any other names in the database.
                comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                comp_names_db = [x[0] for x in comp_names_db_fetch]

                duplicates_count = 0

                for x in range(len(self.name_var_list)):
                    if self.name_var_list[x].get() in comp_names_db:
                        duplicates_count += 1

                if duplicates_count > 0:
                    confirm_duplicate = ms.askquestion('Overwrite Warning', 'One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?')
                    if confirm_duplicate == 'no':
                        # Stop the adding of the items to the database
                        ms.showinfo('Success', 'The duplicates have not been added.')
                    else:
                        # Continue letting the items go
                        # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                        for x in range(len(self.name_var_list)):
                            if self.main_notebook.index(self.main_notebook.select()) == 2:
                                if self.sub_notebook.index(self.sub_notebook.select()) == 0:
                                    # Shell and Tube
                                    self.snt_cost = (627.6 * self.area_var_list[x].get() ** 0.9199)
                                    self.snt_quantity_cost = self.snt_cost * int(self.quantity_var_list[x].get())
                                    self.total_snt_cost += self.snt_quantity_cost

                                    # Find next highest id
                                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                    highest_val = [x[0] for x in select_highest_val][0]

                                    if highest_val is None:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type_snt, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                        db.commit()
                                    else:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type_snt, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                        db.commit()

                                elif self.sub_notebook.index(self.sub_notebook.select()) == 1:
                                    # Plate
                                    self.plate_cost = (2667.7 * self.area_var_list[x].get() ** 0.3472)
                                    self.plate_quantity_cost = self.plate_cost * int(self.quantity_var_list[x].get())
                                    self.total_plate_cost += self.plate_quantity_cost

                                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                    highest_val = [x[0] for x in select_highest_val][0]

                                    if highest_val is None:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type_plate, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                        db.commit()
                                    else:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type_plate, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                        db.commit()

                                elif self.sub_notebook.index(self.sub_notebook.select()) == 2:
                                    # Air-Cooled Condenser
                                    self.acc_cost = (1706.2 * self.area_var_list[x].get() ** 0.4301)
                                    self.acc_quantity_cost = self.acc_cost * int(self.quantity_var_list[x].get())
                                    self.total_acc_cost += self.acc_quantity_cost

                                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                    highest_val = [x[0] for x in select_highest_val][0]

                                    if highest_val is None:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type_acc, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                        db.commit()
                                    else:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type_acc, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                        db.commit()
                        ms.showinfo('Success', 'System Cost Updated.')
                else:
                    # Continue letting the items go
                    # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                    for x in range(len(self.name_var_list)):
                        if self.main_notebook.index(self.main_notebook.select()) == 2:
                            if self.sub_notebook.index(self.sub_notebook.select()) == 0:
                                # Shell and Tube
                                self.snt_cost = (627.6 * self.area_var_list[x].get() ** 0.9199)
                                self.snt_quantity_cost = self.snt_cost * int(self.quantity_var_list[x].get())
                                self.total_snt_cost += self.snt_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type_snt, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type_snt, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                    db.commit()

                            elif self.sub_notebook.index(self.sub_notebook.select()) == 1:
                                # Plate
                                self.plate_cost = (2667.7 * self.area_var_list[x].get() ** 0.3472)
                                self.plate_quantity_cost = self.plate_cost * int(self.quantity_var_list[x].get())
                                self.total_plate_cost += self.plate_quantity_cost

                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type_plate, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type_plate, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                    db.commit()

                            elif self.sub_notebook.index(self.sub_notebook.select()) == 2:
                                # Air-Cooled Condenser
                                self.acc_cost = (1706.2 * self.area_var_list[x].get() ** 0.4301)
                                self.acc_quantity_cost = self.acc_cost * int(self.quantity_var_list[x].get())
                                self.total_acc_cost += self.acc_quantity_cost

                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type_acc, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type_acc, self.name_var_list[x].get(), round(self.area_var_list[x].get(), 2), self.quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                    db.commit()
                    ms.showinfo('Success', 'System Cost Updated.')

                # Update Results table once this has gone through.
                # Get values from database
                comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
                comp_values = [x[0] for x in comp_values_fetch]

                # Delete the current results page and recreate it.
                self.main_notebook.forget(6)

                r = Results(self.master, self.main_notebook)
                # Clear the table and re-populate it.
                for i in r.treeview.get_children():
                    r.treeview.delete(i)

                # Update Results table once this has gone through.
                for i in range(len(comp_values)):
                    try:
                        r.treeview.insert('', tk.END,
                                             values=(comp_values_fetch[i][0], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4], comp_values_fetch[i][5],
                                                     comp_values_fetch[i][6], comp_values_fetch[i][7]))
                    except IndexError:
                        # Insert an empty string if this error is caught
                        r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
                    r.treeview.pack(pady=2, padx=2)


class Pumps():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook

        self.pumps_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(self.pumps_page, text='Pumps')

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

        # Entry field to enter how many pumps you want.
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

        self.name_iter_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):", self.quantity_var_list, self.i, self.name_iter_list)

    def info_press(self):
        self.total_pump_cost = 0
        already_called = 0
        invalid_entries = []
        _type = 'Pump'

        if len(self.name_var_list) == 0:
            ms.showerror('Error', 'No components entered.', icon='error')
        else:
            # Calculate total cost of components within section using specialised formulae
            for i in range(len(self.name_var_list)):
                if self.name_var_list[i].get() == '':
                    ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.quantity_var_list[i].get() == '':
                        ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.power_var_list[i].get() == '' or self.power_var_list[i].get() == 0.0:
                        ms.showerror('Error', 'You left one or more Power Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

            if len(invalid_entries) == 0:
                # Check if the name of the component is equal to any other names in the database.
                comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                comp_names_db = [x[0] for x in comp_names_db_fetch]

                duplicates_count = 0

                for x in range(len(self.name_var_list)):
                    if self.name_var_list[x].get() in comp_names_db:
                        duplicates_count += 1

                if duplicates_count > 0:
                    confirm_duplicate = ms.askquestion("Overwrite Warning", "One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?")
                    if confirm_duplicate == 'no':
                        # Stop the adding of the items to the database
                        ms.showinfo('Success', 'The duplicates have not been added.')
                    else:
                        # Continue letting the items go
                        # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                        for x in range(len(self.name_var_list)):
                            # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                            if self.main_notebook.index(self.main_notebook.select()) == 1:
                                self.pump_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                                self.pump_quantity_cost = self.pump_cost * int(self.quantity_var_list[i].get())
                                self.total_pump_cost += self.pump_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.pump_cost, 2), round(self.total_pump_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.pump_cost, 2), round(self.total_pump_cost, 2)))
                                    db.commit()
                        ms.showinfo('Success', 'System Cost Updated.')
                else:
                    # Continue letting the items go
                    # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                    for i in range(len(self.name_var_list)):
                        self.total_pump_cost = 0
                        # Check if its the Turbine Page to calculate the correct results for the pump costs.
                        if self.main_notebook.index(self.main_notebook.select()) == 1:
                            self.pump_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                            self.pump_quantity_cost = self.pump_cost * int(self.quantity_var_list[i].get())
                            self.total_pump_cost += self.pump_quantity_cost

                            # Find next highest id
                            select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                            highest_val = [x[0] for x in select_highest_val][0]

                            if highest_val is None:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.pump_cost, 2), round(self.total_pump_cost, 2)))
                                db.commit()
                            else:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.pump_cost, 2), round(self.total_pump_cost, 2)))
                                db.commit()
                    ms.showinfo('Success', 'System Cost Updated.')

                # Update Results table once this has gone through.
                # Get values from database
                comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
                comp_values = [x[0] for x in comp_values_fetch]

                # Delete the current results page and recreate it.
                self.main_notebook.forget(6)

                r = Results(self.master, self.main_notebook)
                # Clear the table and re-populate it.
                for i in r.treeview.get_children():
                    r.treeview.delete(i)

                # Update Results table once this has gone through.
                for i in range(len(comp_values)):
                    try:
                        r.treeview.insert('', tk.END,
                                             values=(comp_values_fetch[i][0], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4], comp_values_fetch[i][5],
                                                     comp_values_fetch[i][6], comp_values_fetch[i][7]))
                    except IndexError:
                        # Insert an empty string if this error is caught
                        r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
                    r.treeview.pack(pady=2, padx=2)


class Expanders():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook

        self.expanders_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(self.expanders_page, text='Expanders')

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

        # Entry field to enter how many expanders you want.
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

        self.name_iter_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.power_var_list, "Power (kW):",self.quantity_var_list, self.i, self.name_iter_list)

    def info_press(self):
        self.total_expander_cost = 0
        already_called = 0
        invalid_entries = []
        _type = 'Expander'

        if len(self.name_var_list) == 0:
            ms.showerror('Error', 'No components entered.', icon='error')
        else:
            # Calculate total cost of components within section using specialised formulae
            for i in range(len(self.name_var_list)):
                if self.name_var_list[i].get() == '':
                    ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.quantity_var_list[i].get() == '':
                        ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.power_var_list[i].get() == '' or self.power_var_list[i].get() == 0.0:
                        ms.showerror('Error', 'You left one or more Power Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Power Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

            if len(invalid_entries) == 0:
                # Check if the name of the component is equal to any other names in the database.
                comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                comp_names_db = [x[0] for x in comp_names_db_fetch]

                duplicates_count = 0

                for x in range(len(self.name_var_list)):
                    if self.name_var_list[x].get() in comp_names_db:
                        duplicates_count += 1

                if duplicates_count > 0:
                    confirm_duplicate = ms.askquestion("Overwrite Warning", "One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?")
                    if confirm_duplicate == 'no':
                        # Stop the adding of the items to the database
                        ms.showinfo('Success', 'The duplicates have not been added.')
                    else:
                        # Continue letting the items go
                        # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                        for x in range(len(self.name_var_list)):
                            # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                            if self.main_notebook.index(self.main_notebook.select()) == 1:
                                self.expander_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                                self.expander_quantity_cost = self.expander_cost * int(self.quantity_var_list[i].get())
                                self.total_expander_cost += self.expander_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.expander_cost, 2), round(self.total_expander_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.expander_cost, 2), round(self.total_expander_cost, 2)))
                                    db.commit()
                        ms.showinfo('Success', 'System Cost Updated.')
                else:
                    # Continue letting the items go
                    # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                    for i in range(len(self.name_var_list)):
                        self.total_expander_cost = 0
                        # Check if its the Turbine Page to calculate the correct results for the expander costs.
                        if self.main_notebook.index(self.main_notebook.select()) == 1:
                            self.expander_cost = (2984.9 * self.power_var_list[i].get() ** 0.5171)
                            self.expander_quantity_cost = self.expander_cost * int(self.quantity_var_list[i].get())
                            self.total_expander_cost += self.expander_quantity_cost

                            # Find next highest id
                            select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                            highest_val = [x[0] for x in select_highest_val][0]

                            if highest_val is None:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.expander_cost, 2), round(self.total_expander_cost, 2)))
                                db.commit()
                            else:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.power_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.expander_cost, 2), round(self.total_expander_cost, 2)))
                                db.commit()
                    ms.showinfo('Success', 'System Cost Updated.')

                # Update Results table once this has gone through.
                # Get values from database
                comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
                comp_values = [x[0] for x in comp_values_fetch]

                # Delete the current results page and recreate it.
                self.main_notebook.forget(6)

                r = Results(self.master, self.main_notebook)
                # Clear the table and re-populate it.
                for i in r.treeview.get_children():
                    r.treeview.delete(i)

                # Update Results table once this has gone through.
                for i in range(len(comp_values)):
                    try:
                        r.treeview.insert('', tk.END,
                                             values=(comp_values_fetch[i][0], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4], comp_values_fetch[i][5],
                                                     comp_values_fetch[i][6], comp_values_fetch[i][7]))
                    except IndexError:
                        # Insert an empty string if this error is caught
                        r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
                    r.treeview.pack(pady=2, padx=2)


class StorageTanks():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook
        self.st_page = tk.Frame(self.main_notebook, bg=bg)
        self.main_notebook.add(self.st_page, text='Storage Tanks')

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

        # Entry field to enter how many storage tanks you want.
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

        self.name_iter_list = []

    def num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.top_frame, self.mid1_frame, self.mid2_frame, self.mid3_frame, self.bottom_frame, self.name_var_list, self.volume_var_list, "Volume (L):", self.quantity_var_list, self.i, self.name_iter_list)

    def info_press(self):
        self.total_st_cost = 0
        already_called = 0
        invalid_entries = []
        _type = 'Storage Tank'

        if len(self.name_var_list) == 0:
            ms.showerror('Error', 'No components entered.', icon='error')
        else:
            # Calculate total cost of components within section using specialised formulae
            for i in range(len(self.name_var_list)):
                if self.name_var_list[i].get() == '':
                    ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.quantity_var_list[i].get() == '':
                        ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

                try:
                    if self.volume_var_list[i].get() == '' or self.volume_var_list[i].get() == 0.0:
                        ms.showerror('Error', 'You left one or more Volume Fields empty.', icon='error')
                        invalid_entries.append(i)
                        already_called += 1
                        if already_called >= 1:
                            break
                except Exception:
                    ms.showerror('Error', 'Please enter a valid number in the Volume Field.', icon='error')
                    invalid_entries.append(i)
                    already_called += 1
                    if already_called >= 1:
                        break

            if len(invalid_entries) == 0:
                # Check if the name of the component is equal to any other names in the database.
                comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                comp_names_db = [x[0] for x in comp_names_db_fetch]

                duplicates_count = 0

                for x in range(len(self.name_var_list)):
                    if self.name_var_list[x].get() in comp_names_db:
                        duplicates_count += 1

                if duplicates_count > 0:
                    confirm_duplicate = ms.askquestion("Overwrite Warning", "One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?")
                    if confirm_duplicate == 'no':
                        # Stop the adding of the items to the database
                        ms.showinfo('Success', 'The duplicates have not been added.')
                    else:
                        # Continue letting the items go
                        # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                        for x in range(len(self.name_var_list)):
                            # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                            if self.main_notebook.index(self.main_notebook.select()) == 1:
                                self.st_cost = (2984.9 * self.volume_var_list[i].get() ** 0.5171)
                                self.st_quantity_cost = self.st_cost * int(self.quantity_var_list[i].get())
                                self.total_st_cost += self.st_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                    db.commit()
                        ms.showinfo('Success', 'System Cost Updated.')
                else:
                    # Continue letting the items go
                    # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                    for i in range(len(self.name_var_list)):
                        self.total_st_cost = 0
                        # Check if its the Turbine Page to calculate the correct results for the st costs.
                        if self.main_notebook.index(self.main_notebook.select()) == 1:
                            self.st_cost = (2984.9 * self.volume_var_list[i].get() ** 0.5171)
                            self.st_quantity_cost = self.st_cost * int(self.quantity_var_list[i].get())
                            self.total_st_cost += self.st_quantity_cost

                            # Find next highest id
                            select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                            highest_val = [x[0] for x in select_highest_val][0]

                            if highest_val is None:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (_type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                db.commit()
                            else:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, _type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                db.commit()
                    ms.showinfo('Success', 'System Cost Updated.')

                # Update Results table once this has gone through.
                # Get values from database
                comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
                comp_values = [x[0] for x in comp_values_fetch]

                # Delete the current results page and recreate it.
                self.main_notebook.forget(6)

                r = Results(self.master, self.main_notebook)
                # Clear the table and re-populate it.
                for i in r.treeview.get_children():
                    r.treeview.delete(i)

                # Update Results table once this has gone through.
                for i in range(len(comp_values)):
                    try:
                        r.treeview.insert('', tk.END,
                                             values=(comp_values_fetch[i][0], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4], comp_values_fetch[i][5],
                                                     comp_values_fetch[i][6], comp_values_fetch[i][7]))
                    except IndexError:
                        # Insert an empty string if this error is caught
                        r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
                    r.treeview.pack(pady=2, padx=2)


class Results():
    def __init__(self, master, main_notebook):
        self.master = master
        results_page = tk.Frame(main_notebook, bg=bg)
        main_notebook.add(results_page, text='Results')
        main_notebook.insert(6, results_page)

        # RESULTS PAGE
        treeview_frame = tk.Frame(results_page, relief=tk.GROOVE, bd=0, bg='gray15')
        treeview_frame.pack(side=tk.TOP, padx=10, pady=10)

        treeview_label = tk.Label(treeview_frame, relief=tk.GROOVE, bg='gray15')
        treeview_label.config(text='Components Submitted', font='System 6', fg='yellow')
        treeview_label.pack(side=tk.TOP, padx=10, pady=10)

        # Create the columns necessary to display the database in the GUI as a table.
        self.columns = ('ID', 'Type', 'Name', 'Area/Power/Volume', 'Quantity', 'Individual Cost', 'Quantity x Individual Cost')
        self.treeview = ttk.Treeview(treeview_frame, columns=self.columns, show='headings')
        # Makes the column titles
        self.treeview.column('ID', anchor=tk.CENTER, width=50)
        self.treeview.column('Type', anchor=tk.CENTER, width=250)
        self.treeview.column('Name', anchor=tk.CENTER, width=100)
        self.treeview.column('Area/Power/Volume', anchor=tk.CENTER, width=200)
        self.treeview.column('Quantity', anchor=tk.CENTER, width=100)
        self.treeview.column('Individual Cost', anchor=tk.CENTER, width=100)
        self.treeview.column('Quantity x Individual Cost', anchor=tk.CENTER, width=250)

        # Fetch values from database
        comp_values_fetch = c.execute('SELECT * FROM ComponentData').fetchall()
        comp_values = [x[0] for x in comp_values_fetch]

        for i in range(len(comp_values)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(comp_values_fetch[i][0], comp_values_fetch[i][1], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4],
                                             comp_values_fetch[i][5], comp_values_fetch[i][6]))
            except IndexError:
                # Insert an empty string if this error is caught
                self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
            self.treeview.pack(pady=2, padx=2)
        # For every column in the columns list, make the column able to be
        # sorted alphabetically or numerically by calling the
        # treeview_sort_column function for every column each time the column
        # heading is pressed.
        for col in self.columns:
            self.treeview.heading(col, text=col,
                                  command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))

        # Right Click Context Menu
        self.popup_menu = tk.Menu(treeview_frame, tearoff = 0)
        self.popup_menu.add_command(label="Delete", command=self.delete_selected)

        self.treeview.bind('<Button-3>', self.popup)
        self.treeview.bind('<1>',  self.edit_cell)

        # Results actions frame
        results_frame = tk.Frame(results_page)
        results_frame.pack(expand=True, fill=tk.X)

        results_label = tk.Label(results_frame, relief=tk.GROOVE, bg='gray15')
        results_label.config(text='Calculate System Total', font='System 6', fg='yellow')
        results_label.pack(pady=10)

        results_button = tk.Button(results_frame)
        results_button.config(relief=tk.RAISED, bd=5, text='    Calculate    ',
                                 command=self.total_cost_calculate)
        results_button.pack(side=tk.TOP, anchor=tk.S, pady=15, padx=15)

        total_system_cost = 0
        total_quantity = 0

        comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData').fetchall()
        comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
        for quantity in comp_values_quantity:
            total_quantity += quantity

        comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData').fetchall()
        comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
        for individual_cost in comp_values_individual_costs:
            total_system_cost += individual_cost

        self.results_label = tk.Label(results_frame, bg='gray15')
        self.results_label.config(bd=0, text='Total System Cost: £%.2f' % total_system_cost, font='System 6', fg='yellow')
        self.results_label.pack()

        self.results_quantity_total_label = tk.Label(results_frame, bg='gray15')
        self.results_quantity_total_label.config(bd=0, text='Across %d Components' % total_quantity, font='System 6', fg='yellow')
        self.results_quantity_total_label.pack()

        # Clear Database button
        clear_db_btn = tk.Button(results_frame)
        clear_db_btn.config(relief=tk.RAISED, bd=5, text='   Clear Database   ',
                                 command=self.clear_database)
        clear_db_btn.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        # HELP PAGE

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def edit_cell(self, event):
        # Get the rows that were selected
        if self.treeview.identify_region(event.x, event.y) == 'cell':
            # the user clicked on a cell

            def ok(event):
                if str(column) == '#4':
                    try:
                        float_entry = float(entry.get())
                        if float_entry == 0.0 or float_entry == 0 or float_entry == '':
                            ms.showerror('Invalid', 'Invalid Area/Power/Volume Input.')
                        else:
                            self.treeview.set(item, column, entry.get())
                            entry.destroy()

                            row_id = self.treeview.item(item)['values'][0]
                            row_type = self.treeview.item(item)['values'][1]
                            row_name = self.treeview.item(item)['values'][2]
                            row_metric = float(self.treeview.item(item)['values'][3])
                            row_quantity = int(self.treeview.item(item)['values'][4])

                            # Establish total cost values
                            self.total_turbine_cost = 0
                            self.total_snt_cost = 0
                            self.total_plate_cost = 0
                            self.total_acc_cost = 0
                            self.total_pump_cost = 0
                            self.total_expander_cost = 0
                            self.total_st_cost = 0

                            # Calculate the changes to the costs
                            self.total_turbine_cost = 0
                            # Determine which component type the row hosts.
                            if row_type == 'Turbine':
                                self.turbine_cost = (2984.9 * row_metric ** 0.5171)
                                self.turbine_quantity_cost = self.turbine_cost * row_quantity
                                self.total_turbine_cost += self.turbine_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.turbine_cost, 2)
                                comp_total_cost = round(self.total_turbine_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Shell and Tube':
                                self.snt_cost = (627.9 * row_metric ** 0.9199)
                                self.snt_quantity_cost = self.snt_cost * row_quantity
                                self.total_snt_cost += self.snt_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.snt_cost, 2)
                                comp_total_cost = round(self.total_snt_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Plate':
                                self.plate_cost = (2667.7 * row_metric ** 0.3472)
                                self.plate_quantity_cost = self.plate_cost * row_quantity
                                self.total_plate_cost += self.plate_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.plate_cost, 2)
                                comp_total_cost = round(self.total_plate_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Air-Cooled Condenser':
                                self.acc_cost = (1706.2 * row_metric ** 0.4301)
                                self.acc_quantity_cost = self.acc_cost * row_quantity
                                self.total_acc_cost += self.acc_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.acc_cost, 2)
                                comp_total_cost = round(self.total_acc_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Pump':
                                self.pump_cost = (1513.4 * row_metric ** 0.1946)
                                self.pump_quantity_cost = self.pump_cost * row_quantity
                                self.total_pump_cost += self.pump_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.pump_cost, 2)
                                comp_total_cost = round(self.total_pump_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Expander':
                                self.expander_cost = (544 * row_metric ** 0.8331)
                                self.expander_quantity_cost = self.expander_cost * row_quantity
                                self.total_expander_cost += self.expander_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.expander_cost, 2)
                                comp_total_cost = round(self.total_expander_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Storage Tank':
                                self.st_cost = (52.6 * row_metric ** 0.5531)
                                self.st_quantity_cost = self.st_cost * row_quantity
                                self.total_st_cost += self.st_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.st_cost, 2)
                                comp_total_cost = round(self.total_st_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            # Change the values in the database on the correct row.
                            c.execute('UPDATE ComponentData SET name=?, metric=?, quantity=?, individual_cost=?, total_cost=? WHERE id=?', (row_name, row_metric, row_quantity, comp_individual_cost, comp_total_cost, row_id,))
                            db.commit()

                            total_system_cost = 0
                            total_quantity = 0

                            comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData').fetchall()
                            comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
                            for quantity in comp_values_quantity:
                                total_quantity += quantity

                            comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData').fetchall()
                            comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
                            for individual_cost in comp_values_individual_costs:
                                total_system_cost += individual_cost

                            self.results_label["text"] = 'Total System Cost: £%.2f' % round(total_system_cost, 2)
                            self.results_quantity_total_label["text"] = 'Across %d Components' % total_quantity
                            ms.showinfo('Updated', 'Cost has been updated to £{total_system_cost}\nAcross {total_quantity} Components'.format(total_system_cost=round(total_system_cost, 2), total_quantity=total_quantity))

                    except ValueError:
                        ms.showerror('Invalid', 'Invalid Area/Power/Volume Input.')

                elif str(column) == '#5':
                    try:
                        int_entry = int(entry.get())
                        if int_entry == 0 or int_entry == '':
                            ms.showerror('Invalid', 'Invalid Quantity Input.')
                        else:
                            self.treeview.set(item, column, entry.get())
                            entry.destroy()

                            row_id = self.treeview.item(item)['values'][0]
                            row_type = self.treeview.item(item)['values'][1]
                            row_name = self.treeview.item(item)['values'][2]
                            row_metric = float(self.treeview.item(item)['values'][3])
                            row_quantity = int(self.treeview.item(item)['values'][4])

                            # Establish total cost values
                            self.total_turbine_cost = 0
                            self.total_snt_cost = 0
                            self.total_plate_cost = 0
                            self.total_acc_cost = 0
                            self.total_pump_cost = 0
                            self.total_expander_cost = 0
                            self.total_st_cost = 0

                            # Calculate the changes to the costs
                            # Determine which component type the row hosts.
                            if row_type == 'Turbine':
                                self.turbine_cost = (2984.9 * row_metric ** 0.5171)
                                self.turbine_quantity_cost = self.turbine_cost * row_quantity
                                self.total_turbine_cost += self.turbine_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.turbine_cost, 2)
                                comp_total_cost = round(self.total_turbine_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Shell and Tube':
                                self.snt_cost = (627.9 * row_metric ** 0.9199)
                                self.snt_quantity_cost = self.snt_cost * row_quantity
                                self.total_snt_cost += self.snt_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.snt_cost, 2)
                                comp_total_cost = round(self.total_snt_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Plate':
                                self.plate_cost = (2667.7 * row_metric ** 0.3472)
                                self.plate_quantity_cost = self.plate_cost * row_quantity
                                self.total_plate_cost += self.plate_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.plate_cost, 2)
                                comp_total_cost = round(self.total_plate_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Air-Cooled Condenser':
                                self.acc_cost = (1706.2 * row_metric ** 0.4301)
                                self.acc_quantity_cost = self.acc_cost * row_quantity
                                self.total_acc_cost += self.acc_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.acc_cost, 2)
                                comp_total_cost = round(self.total_acc_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Pump':
                                self.pump_cost = (1513.4 * row_metric ** 0.1946)
                                self.pump_quantity_cost = self.pump_cost * row_quantity
                                self.total_pump_cost += self.pump_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.pump_cost, 2)
                                comp_total_cost = round(self.total_pump_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Expander':
                                self.expander_cost = (544 * row_metric ** 0.8331)
                                self.expander_quantity_cost = self.expander_cost * row_quantity
                                self.total_expander_cost += self.expander_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.expander_cost, 2)
                                comp_total_cost = round(self.total_expander_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            elif row_type == 'Storage Tank':
                                self.st_cost = (52.6 * row_metric ** 0.5531)
                                self.st_quantity_cost = self.st_cost * row_quantity
                                self.total_st_cost += self.st_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.st_cost, 2)
                                comp_total_cost = round(self.total_st_cost, 2)

                                self.treeview.set(item, '#6', comp_individual_cost)
                                self.treeview.set(item, '#7', comp_total_cost)

                            # Change the values in the database on the correct row.
                            c.execute('UPDATE ComponentData SET name=?, metric=?, quantity=?, individual_cost=?, total_cost=? WHERE id=?', (row_name, row_metric, row_quantity, comp_individual_cost, comp_total_cost, row_id,))
                            db.commit()

                            total_system_cost = 0
                            total_quantity = 0

                            comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData').fetchall()
                            comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
                            for quantity in comp_values_quantity:
                                total_quantity += quantity

                            comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData').fetchall()
                            comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
                            for individual_cost in comp_values_individual_costs:
                                total_system_cost += individual_cost

                            self.results_label["text"] = 'Total System Cost: £%.2f' % round(total_system_cost, 2)
                            self.results_quantity_total_label["text"] = 'Across %d Components' % total_quantity
                            ms.showinfo('Updated', 'Cost has been updated to £{total_system_cost}\nAcross {total_quantity} Components'.format(total_system_cost=round(total_system_cost, 2), total_quantity=total_quantity))
                    except ValueError:
                        ms.showerror('Invalid', 'Invalid Quantity Input.')

                else:
                    self.treeview.set(item, column, entry.get())
                    entry.destroy()

                    row_id = self.treeview.item(item)['values'][0]
                    row_name = self.treeview.item(item)['values'][2]
                    row_metric = self.treeview.item(item)['values'][3]
                    row_quantity = self.treeview.item(item)['values'][4]

                    # Need to update the costs according to the changes too.
                    row_individual_cost = self.treeview.item(item)['values'][5]
                    row_total_cost = self.treeview.item(item)['values'][6]

                    # Change the values in the database on the correct row.
                    c.execute('UPDATE ComponentData SET name=?, metric=?, quantity=?, individual_cost=?, total_cost=? WHERE id=?', (row_name, row_metric, row_quantity, row_individual_cost, row_total_cost, row_id,))
                    db.commit()

            column = self.treeview.identify_column(event.x)
            column_str = str(column)
            if column_str != '#3' and column_str != '#4' and column_str != '#5':
                return
            else:
                item = self.treeview.identify_row(event.y)
                x, y, width, height = self.treeview.bbox(item, column)
                value = self.treeview.set(item, column)
        else:
            return

        # display the Entry field
        entry = ttk.Entry(self.treeview)
        entry.place(x=x, y=y, width=width, height=height,
                    anchor="nw")
        entry.insert(0, value)
        entry.bind('<FocusOut>', lambda e: entry.destroy())
        entry.bind('<Return>', ok)
        entry.focus_set()

    def delete_selected(self):
        # Deletes the item from the treeview.
        count = -1
        for i in self.treeview.selection()[::-1]:
            # Select the id seen on the treeview table
            count += 1
            tv_id = list(self.treeview.item(self.treeview.selection()[::-1][count]).values())[2][0]
            self.treeview.delete(i)
            count -= 1

            # Delete the row from the database as well.
            c.execute('DELETE FROM ComponentData WHERE id=?', (tv_id,))
            db.commit()

    def clear_database(self):
        confirm_clear = ms.askokcancel('WARNING', 'Clearing the database is permanent.\nAny components that were stored will be deleted forever.\nDo you wish to continue?')
        if confirm_clear:
            # Clear the database
            c.execute('DELETE FROM ComponentData')
            db.commit()

            ms.showinfo('Success', 'Database has been cleared.')

            # Clear the results treeview table.
            for i in self.treeview.get_children():
                self.treeview.delete(i)
        else:
            ms.showinfo('Aborted', 'Action Aborted')

    def total_cost_calculate(self):
        # Get all the total_cost values from the table.
        # Add them all together. BANG!
        total_system_cost = 0
        total_quantity = 0

        comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData').fetchall()
        comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
        for quantity in comp_values_quantity:
            total_quantity += quantity

        comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData').fetchall()
        comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
        for individual_cost in comp_values_individual_costs:
            total_system_cost += individual_cost

        self.results_label["text"] = 'Total System Cost: £%.2f' % round(total_system_cost, 2)
        self.results_quantity_total_label["text"] = 'Across %d Components' % total_quantity
        ms.showinfo('Updated', 'Cost has been updated to £{total_system_cost}\nAcross {total_quantity} Components'.format(total_system_cost=round(total_system_cost, 2), total_quantity=total_quantity))

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

        # About page
        about_frame = tk.Frame(about_page, bg='gray20')
        about_frame.pack(expand=True)

        title_label_1 = tk.Label(about_frame, bg='gray20')
        title_label_1.config(bd=0, text='Software Developed by Marco Fernandes', font='System 30', fg='yellow')
        title_label_1.pack(expand=True, fill=tk.X, anchor=tk.N)

        title_label_2 = tk.Label(about_frame, bg='gray20')
        title_label_2.config(bd=0, text='Component Cost Equations Developed by Robert Platica', font='System 30', fg='yellow')
        title_label_2.pack(expand=True, fill=tk.X, anchor=tk.N)


class MainApp():
    def __init__(self, master):
        self.master = master
        master.configure(bg='gray15')
        master.title('Component Cost Calculator')
        master.option_add('*Font', 'System 12')
        master.option_add('*Label.Font', 'System 14')
        master.geometry('1920x1080')
        master.wm_state('zoomed')

        master.protocol("WM_DELETE_WINDOW", self.on_close)

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

        fetch_all = c.execute("SELECT * FROM ComponentData").fetchall()

        if len(fetch_all) > 0:
            master.after(1, self.abort_database)

    def abort_database(self):
        abort_db = ms.askokcancel('Warning', 'There are currently values in the database that were saved from the previous session.\nDo you wish to reset the database or continue as is?', icon='warning')
        if abort_db:
            # Reset the database
            c.execute('DELETE FROM ComponentData')
            db.commit()

    def on_close(self):
        close = ms.askokcancel('Cancel', 'Would you like to close the program?')
        if close:
            self.master.destroy()


def main():
    root = tk.Tk()
    MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
