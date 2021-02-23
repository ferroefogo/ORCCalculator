# Heat Exchanges Page
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3

# External imports
from compcreate import ComponentCreation
from results import Results

# Connect to database
with sqlite3.connect('ComponentData.db') as db:
    c = db.cursor()


class HeatExchangers():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook
        hx_page = tk.Frame(self.main_notebook, bg='gray20')
        self.main_notebook.add(hx_page, text='Heat Exchangers')

        self.sub_notebook = ttk.Notebook(hx_page)
        self.sub_notebook.pack(expand=True, fill=tk.BOTH)

        self.snt(self.sub_notebook)
        self.plate(self.sub_notebook)
        self.acc(self.sub_notebook)

    def snt(self, sub_notebook):
        hx_snt_page = tk.Frame(sub_notebook, bg='gray20')
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

        self.snt_name_var_list = []
        self.snt_area_var_list = []
        self.snt_quantity_var_list = []

        self.snt_name_iter_list = []

    def plate(self, sub_notebook):
        hx_plate_page = tk.Frame(sub_notebook, bg='gray20')
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

        self.plate_name_var_list = []
        self.plate_area_var_list = []
        self.plate_quantity_var_list = []

        self.plate_name_iter_list = []

    def acc(self, sub_notebook):
        hx_acc_page = tk.Frame(sub_notebook, bg='gray20')
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

        self.acc_name_var_list = []
        self.acc_area_var_list = []
        self.acc_quantity_var_list = []

        self.acc_name_iter_list = []

    def snt_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.snt_top_frame, self.snt_mid1_frame, self.snt_mid2_frame, self.snt_mid3_frame, self.snt_bottom_frame, self.snt_name_var_list, self.snt_area_var_list, "Area (m²):", self.snt_quantity_var_list, self.i, self.snt_name_iter_list)

    def plate_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.plate_top_frame, self.plate_mid1_frame, self.plate_mid2_frame, self.plate_mid3_frame, self.plate_bottom_frame, self.plate_name_var_list, self.plate_area_var_list, "Area (m²):", self.plate_quantity_var_list, self.i, self.plate_name_iter_list)

    def acc_num_press(self):
        self.i += 1
        self.c = ComponentCreation(self.acc_top_frame, self.acc_mid1_frame, self.acc_mid2_frame, self.acc_mid3_frame, self.acc_bottom_frame, self.acc_name_var_list, self.acc_area_var_list, "Area (m²):", self.acc_quantity_var_list, self.i, self.acc_name_iter_list)

    def info_press(self):
        self.total_snt_cost = 0
        self.total_plate_cost = 0
        self.total_acc_cost = 0

        already_called = 0

        snt_invalid_entries = []
        plate_invalid_entries = []
        acc_invalid_entries = []

        _type_snt = 'Shell and Tube'
        _type_plate = 'Plate'
        _type_acc = 'Air-Cooled Condenser'

        # Find out which tab the user is on.
        if self.main_notebook.index(self.main_notebook.select()) == 2:
            if self.sub_notebook.index(self.sub_notebook.select()) == 0:
                # The user is on the SNT page.
                if len(self.snt_name_var_list) == 0:
                    ms.showerror('Error', 'No components entered.', icon='error')
                else:
                    # Calculate total cost of components within section using specialised formulae
                    for i in range(len(self.snt_name_var_list)):
                        if self.snt_name_var_list[i].get() == '':
                            ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                            snt_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break
                        try:
                            if self.snt_quantity_var_list[i].get() == '':
                                ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                                snt_invalid_entries.append(i)
                                already_called += 1
                                if already_called >= 1:
                                    break
                        except Exception:
                            ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                            snt_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break

                        try:
                            if self.snt_area_var_list[i].get() == '':
                                ms.showerror('Error', 'You left one or more Area Fields empty.', icon='error')
                                snt_invalid_entries.append(i)
                                already_called += 1
                                if already_called >= 1:
                                    break
                        except Exception:
                            ms.showerror('Error', 'Please enter a valid number in the Area Field.', icon='error')
                            snt_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break

                    if len(snt_invalid_entries) == 0:
                        # Check if the name of the component is equal to any other names in the database.
                        comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                        comp_names_db = [x[0] for x in comp_names_db_fetch]

                        duplicates_count = 0

                        for x in range(len(self.snt_name_var_list)):
                            if self.snt_name_var_list[x].get() in comp_names_db:
                                duplicates_count += 1

                        if duplicates_count > 0:
                            confirm_duplicate = ms.askquestion('Overwrite Warning', 'One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?')
                            if confirm_duplicate == 'no':
                                # Stop the adding of the items to the database
                                ms.showinfo('Success', 'The duplicates have not been added.')
                            else:
                                # Read from the txt file the highest config id and insert it with each component
                                f = open("config_id.txt", "r")
                                CURRENT_CONFIG_ID = f.read()
                                f.close()

                                # Continue letting the items go
                                # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                                for x in range(len(self.snt_name_var_list)):
                                    # Shell and Tube
                                    self.snt_cost = (627.6 * self.snt_area_var_list[x].get() ** 0.9199)
                                    self.snt_quantity_cost = self.snt_cost * int(self.quantity_var_list[x].get())
                                    self.total_snt_cost += self.snt_quantity_cost

                                    # Find next highest id
                                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                    highest_val = [x[0] for x in select_highest_val][0]

                                    if highest_val is None:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type_snt, self.snt_name_var_list[x].get(), round(self.snt_area_var_list[x].get(), 2), self.snt_quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                        db.commit()
                                    else:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type_snt, self.snt_name_var_list[x].get(), round(self.snt_area_var_list[x].get(), 2), self.snt_quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                        db.commit()
                                ms.showinfo('Success', 'System Cost Updated.')
                        else:
                            # Read from the txt file the config id and insert it with each component
                            f = open("config_id.txt", "r")
                            CURRENT_CONFIG_ID = f.read()
                            f.close()

                            # Continue letting the items go
                            # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                            for x in range(len(self.snt_name_var_list)):
                                # Shell and Tube
                                self.snt_cost = (627.6 * self.snt_area_var_list[x].get() ** 0.9199)
                                self.snt_quantity_cost = self.snt_cost * int(self.snt_quantity_var_list[x].get())
                                self.total_snt_cost += self.snt_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type_snt, self.snt_name_var_list[x].get(), round(self.snt_area_var_list[x].get(), 2), self.snt_quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type_snt, self.snt_name_var_list[x].get(), round(self.snt_area_var_list[x].get(), 2), self.snt_quantity_var_list[x].get(), round(self.snt_cost, 2), round(self.total_snt_cost, 2)))
                                    db.commit()
                            ms.showinfo('Success', 'System Cost Updated.')

            elif self.sub_notebook.index(self.sub_notebook.select()) == 1:
                # The user is on the plate page.
                if len(self.plate_name_var_list) == 0:
                    ms.showerror('Error', 'No components entered.', icon='error')
                else:
                    # Calculate total cost of components within section using specialised formulae
                    for i in range(len(self.plate_name_var_list)):
                        if self.plate_name_var_list[i].get() == '':
                            ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                            plate_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break
                        try:
                            if self.plate_quantity_var_list[i].get() == '':
                                ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                                plate_invalid_entries.append(i)
                                already_called += 1
                                if already_called >= 1:
                                    break
                        except Exception:
                            ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                            plate_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break

                        try:
                            if self.plate_area_var_list[i].get() == '':
                                ms.showerror('Error', 'You left one or more Area Fields empty.', icon='error')
                                plate_invalid_entries.append(i)
                                already_called += 1
                                if already_called >= 1:
                                    break
                        except Exception:
                            ms.showerror('Error', 'Please enter a valid number in the Area Field.', icon='error')
                            plate_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break

                    if len(plate_invalid_entries) == 0:
                        # Check if the name of the component is equal to any other names in the database.
                        comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                        comp_names_db = [x[0] for x in comp_names_db_fetch]

                        duplicates_count = 0

                        for x in range(len(self.plate_name_var_list)):
                            if self.plate_name_var_list[x].get() in comp_names_db:
                                duplicates_count += 1

                        if duplicates_count > 0:
                            confirm_duplicate = ms.askquestion('Overwrite Warning', 'One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?')
                            if confirm_duplicate == 'no':
                                # Stop the adding of the items to the database
                                ms.showinfo('Success', 'The duplicates have not been added.')
                            else:
                                # Read from the txt file the config id and insert it with each component
                                f = open("config_id.txt", "r")
                                CURRENT_CONFIG_ID = f.read()
                                f.close()

                                # Continue letting the items go
                                # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                                for x in range(len(self.plate_name_var_list)):
                                    # Shell and Tube
                                    self.plate_cost = (627.6 * self.plate_area_var_list[x].get() ** 0.9199)
                                    self.plate_quantity_cost = self.plate_cost * int(self.plate_quantity_var_list[x].get())
                                    self.total_plate_cost += self.plate_quantity_cost

                                    # Find next highest id
                                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                    highest_val = [x[0] for x in select_highest_val][0]

                                    if highest_val is None:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type_plate, self.plate_name_var_list[x].get(), round(self.plate_area_var_list[x].get(), 2), self.plate_quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                        db.commit()
                                    else:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type_plate, self.plate_name_var_list[x].get(), round(self.plate_area_var_list[x].get(), 2), self.plate_quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                        db.commit()
                                ms.showinfo('Success', 'System Cost Updated.')
                        else:
                            # Read from the txt file the config id and insert it with each component
                            f = open("config_id.txt", "r")
                            CURRENT_CONFIG_ID = f.read()
                            f.close()

                            # Continue letting the items go
                            # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                            for x in range(len(self.plate_name_var_list)):
                                # Shell and Tube
                                self.plate_cost = (627.6 * self.plate_area_var_list[x].get() ** 0.9199)
                                self.plate_quantity_cost = self.plate_cost * int(self.plate_quantity_var_list[x].get())
                                self.total_plate_cost += self.plate_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type_plate, self.plate_name_var_list[x].get(), round(self.plate_area_var_list[x].get(), 2), self.plate_quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type_plate, self.plate_name_var_list[x].get(), round(self.plate_area_var_list[x].get(), 2), self.plate_quantity_var_list[x].get(), round(self.plate_cost, 2), round(self.total_plate_cost, 2)))
                                    db.commit()
                            ms.showinfo('Success', 'System Cost Updated.')
            elif self.sub_notebook.index(self.sub_notebook.select()) == 2:
                 # The user is on the acc page.
                if len(self.acc_name_var_list) == 0:
                    ms.showerror('Error', 'No components entered.', icon='error')
                else:
                    # Calculate total cost of components within section using specialised formulae
                    for i in range(len(self.acc_name_var_list)):
                        if self.acc_name_var_list[i].get() == '':
                            ms.showerror('Error', 'You left one or more Name Fields empty.', icon='error')
                            acc_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break
                        try:
                            if self.acc_quantity_var_list[i].get() == '':
                                ms.showerror('Error', 'You left one or more Quantity Fields empty.', icon='error')
                                acc_invalid_entries.append(i)
                                already_called += 1
                                if already_called >= 1:
                                    break
                        except Exception:
                            ms.showerror('Error', 'Please enter a valid number in the Quantity Field.', icon='error')
                            acc_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break

                        try:
                            if self.acc_area_var_list[i].get() == '':
                                ms.showerror('Error', 'You left one or more Area Fields empty.', icon='error')
                                acc_invalid_entries.append(i)
                                already_called += 1
                                if already_called >= 1:
                                    break
                        except Exception:
                            ms.showerror('Error', 'Please enter a valid number in the Area Field.', icon='error')
                            acc_invalid_entries.append(i)
                            already_called += 1
                            if already_called >= 1:
                                break

                    if len(acc_invalid_entries) == 0:
                        # Check if the name of the component is equal to any other names in the database.
                        comp_names_db_fetch = c.execute('SELECT name FROM ComponentData').fetchall()
                        comp_names_db = [x[0] for x in comp_names_db_fetch]

                        duplicates_count = 0

                        for x in range(len(self.acc_name_var_list)):
                            if self.acc_name_var_list[x].get() in comp_names_db:
                                duplicates_count += 1

                        if duplicates_count > 0:
                            confirm_duplicate = ms.askquestion('Overwrite Warning', 'One or more duplicates have been found in the database matching this component name.\n\n Do you still want to add this component?')
                            if confirm_duplicate == 'no':
                                # Stop the adding of the items to the database
                                ms.showinfo('Success', 'The duplicates have not been added.')
                            else:
                                # Read from the txt file the config id and insert it with each component
                                f = open("config_id.txt", "r")
                                CURRENT_CONFIG_ID = f.read()
                                f.close()

                                # Continue letting the items go
                                # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                                for x in range(len(self.acc_name_var_list)):
                                    # Shell and Tube
                                    self.acc_cost = (627.6 * self.accarea_var_list[x].get() ** 0.9199)
                                    self.acc_quantity_cost = self.acc_cost * int(self.quantity_var_list[x].get())
                                    self.total_acc_cost += self.acc_quantity_cost

                                    # Find next highest id
                                    select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                    highest_val = [x[0] for x in select_highest_val][0]

                                    if highest_val is None:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type_acc, self.acc_name_var_list[x].get(), round(self.acc_area_var_list[x].get(), 2), self.acc_quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                        db.commit()
                                    else:
                                        # Write information to database
                                        c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type_acc, self.acc_name_var_list[x].get(), round(self.acc_area_var_list[x].get(), 2), self.acc_quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                        db.commit()
                                ms.showinfo('Success', 'System Cost Updated.')
                        else:
                            # Read from the txt file the config id and insert it with each component
                            f = open("config_id.txt", "r")
                            CURRENT_CONFIG_ID = f.read()
                            f.close()

                            # Continue letting the items go
                            # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                            for x in range(len(self.acc_name_var_list)):
                                # Shell and Tube
                                self.acc_cost = (627.6 * self.acc_area_var_list[x].get() ** 0.9199)
                                self.acc_quantity_cost = self.acc_cost * int(self.acc_quantity_var_list[x].get())
                                self.total_acc_cost += self.acc_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type_acc, self.acc_name_var_list[x].get(), round(self.acc_area_var_list[x].get(), 2), self.acc_quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type_acc, self.acc_name_var_list[x].get(), round(self.acc_area_var_list[x].get(), 2), self.acc_quantity_var_list[x].get(), round(self.acc_cost, 2), round(self.total_acc_cost, 2)))
                                    db.commit()
                            ms.showinfo('Success', 'System Cost Updated.')

            # Update Results table once this has gone through.
            # Get values from database
            comp_values_fetch = c.execute('SELECT * FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
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
                                             values=(comp_values_fetch[i][0], comp_values_fetch[i][1], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4],
                                                     comp_values_fetch[i][5], comp_values_fetch[i][6], comp_values_fetch[i][7]))
                except IndexError:
                    # Insert an empty string if this error is caught
                    r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', ''))
                r.treeview.pack(pady=2, padx=2)