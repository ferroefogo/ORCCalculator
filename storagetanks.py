# Storage Tanks Page
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


class StorageTanks():
    def __init__(self, master, main_notebook):
        self.master = master
        self.main_notebook = main_notebook
        self.st_page = tk.Frame(self.main_notebook, bg='gray20')
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
                        # Read from the txt file the config id and insert it with each component
                        f = open("config_id.txt", "r")
                        CURRENT_CONFIG_ID = f.read()
                        f.close()

                        # Continue letting the items go
                        # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                        for x in range(len(self.name_var_list)):
                            # Check if its the Turbine Page to calculate the correct results for the turbine costs.
                            if self.main_notebook.index(self.main_notebook.select()) == 5:
                                self.st_cost = (2984.9 * self.volume_var_list[i].get() ** 0.5171)
                                self.st_quantity_cost = self.st_cost * int(self.quantity_var_list[i].get())
                                self.total_st_cost += self.st_quantity_cost

                                # Find next highest id
                                select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                                highest_val = [x[0] for x in select_highest_val][0]

                                if highest_val is None:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                    db.commit()
                                else:
                                    # Write information to database
                                    c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                    db.commit()
                        ms.showinfo('Success', 'System Cost Updated.')
                else:
                    # Read from the txt file the config id and insert it with each component
                    f = open("config_id.txt", "r")
                    CURRENT_CONFIG_ID = f.read()
                    f.close()

                    # Continue letting the items go
                    # Another for loop to enter into the database, ONLY IF ALL THE ENTRY FIELDS ARE VALID.
                    for i in range(len(self.name_var_list)):
                        self.total_st_cost = 0
                        # Check if its the Turbine Page to calculate the correct results for the st costs.
                        if self.main_notebook.index(self.main_notebook.select()) == 5:
                            self.st_cost = (2984.9 * self.volume_var_list[i].get() ** 0.5171)
                            self.st_quantity_cost = self.st_cost * int(self.quantity_var_list[i].get())
                            self.total_st_cost += self.st_quantity_cost

                            # Find next highest id
                            select_highest_val = c.execute('SELECT MAX(id)+1 FROM ComponentData').fetchall()
                            highest_val = [x[0] for x in select_highest_val][0]

                            if highest_val is None: 
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(1,?,?,?,?,?,?,?)', (CURRENT_CONFIG_ID, _type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
                                db.commit()
                            else:
                                # Write information to database
                                c.execute('INSERT INTO ComponentData(id, config_id, type, name, metric, quantity, individual_cost, total_cost) VALUES(?,?,?,?,?,?,?,?)', (highest_val, CURRENT_CONFIG_ID, _type, self.name_var_list[i].get(), round(self.volume_var_list[i].get(), 2), self.quantity_var_list[i].get(), round(self.st_cost, 2), round(self.total_st_cost, 2)))
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
                        r.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', '', '', ''))
                    r.treeview.pack(pady=2, padx=2)