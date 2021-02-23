# Results Page
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
import sys
import os.path
from tkinter import filedialog

import pandas as pd
import anvil.server
import anvil.pdf
import anvil.media
from anvil.tables import app_tables
from anvil.pdf import PdfRenderer

# PDF Creation Connect
anvil.server.connect("56MWNLYPKSQFJRQPQ354X4FR-BLH3UYIWD3XTOSEJ")

# Connect to database
with sqlite3.connect('ComponentData.db') as db:
    c = db.cursor()


class Results():
    def __init__(self, master, main_notebook):
        self.master = master
        results_page = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(results_page, text='Results')
        main_notebook.insert(6, results_page)

        # RESULTS PAGE
        treeview_frame = tk.Frame(results_page, relief=tk.GROOVE, bd=0, bg='gray15')
        treeview_frame.pack(side=tk.TOP, padx=10, pady=10)

        treeview_label = tk.Label(treeview_frame, relief=tk.GROOVE, bg='gray15')
        treeview_label.config(text='Components Submitted', font='System 6', fg='yellow')
        treeview_label.pack(side=tk.TOP, padx=10, pady=10)

        # Create the columns necessary to display the database in the GUI as a table.
        self.columns = ('Component ID', 'Configuration ID', 'Type', 'Name', 'Area (㎡)/Power (kW)/Volume (L)', 'Quantity', 'Individual Cost (£)', 'Quantity x Individual Cost (£)')
        self.treeview = ttk.Treeview(treeview_frame, columns=self.columns, show='headings')
        # Makes the column titles
        self.treeview.column('Component ID', anchor=tk.CENTER, width=100)
        self.treeview.column('Configuration ID', anchor=tk.CENTER, width=100)
        self.treeview.column('Type', anchor=tk.CENTER, width=200)
        self.treeview.column('Name', anchor=tk.CENTER, width=100)
        self.treeview.column('Area (㎡)/Power (kW)/Volume (L)', anchor=tk.CENTER, width=200)
        self.treeview.column('Quantity', anchor=tk.CENTER, width=100)
        self.treeview.column('Individual Cost (£)', anchor=tk.CENTER, width=200)
        self.treeview.column('Quantity x Individual Cost (£)', anchor=tk.CENTER, width=250)

        # Get the current ID from the txt file
        f = open("config_id.txt", "r")
        CURRENT_CONFIG_ID = f.read()
        f.close()

        # Fetch values from database
        comp_values_fetch = c.execute('SELECT * FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
        comp_values = [x[0] for x in comp_values_fetch]

        for i in range(len(comp_values)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(comp_values_fetch[i][0], comp_values_fetch[i][1], comp_values_fetch[i][2], comp_values_fetch[i][3], comp_values_fetch[i][4], comp_values_fetch[i][5],
                                             comp_values_fetch[i][6], comp_values_fetch[i][7]))
            except IndexError:
                # Insert an empty string if this error is caught
                self.treeview.insert('', tk.END, values=('', '', '', '', '', '', '', ''))
        self.treeview.pack(pady=2, padx=2)
        # For every column in the columns list, make the column able to be
        # sorted alphabetically or numerically by calling the
        # treeview_sort_column function for every column each time the column
        # heading is pressed.
        for col in self.columns:
            self.treeview.heading(col, text=col,
                                  command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))

        # Right Click Context Menu
        self.popup_menu = tk.Menu(treeview_frame, tearoff=0)
        self.popup_menu.add_command(label="Delete", command=self.delete_selected)

        self.treeview.bind('<Button-3>', self.popup)
        self.treeview.bind('<1>',  self.edit_cell)

        # Results actions frame
        results_frame = tk.Frame(results_page, bg='gray15', bd=5)
        results_frame.pack(side=tk.LEFT, anchor=tk.N)

        results_label = tk.Label(results_frame, bg='gray15')
        results_label.config(bd=0, text='Database Info/Actions', font='System 10', fg='yellow')
        results_label.pack(side=tk.TOP, anchor=tk.N)

        results_button = tk.Button(results_frame)
        results_button.config(relief=tk.RAISED, bd=5, text='Calculate System\nTotal Cost',
                                 command=self.total_cost_calculate)
        results_button.pack(side=tk.TOP, anchor=tk.S, pady=15, padx=15)

        total_system_cost = 0
        total_quantity = 0

        comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
        comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
        for quantity in comp_values_quantity:
            total_quantity += quantity

        comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
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
        clear_db_btn.config(relief=tk.RAISED, bd=5, text='   Clear Current Configuration   ',
                                 command=self.clear_config)
        clear_db_btn.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        # Configuration Area
        config_frame = tk.Frame(results_page, bg='gray15')
        config_frame.pack(side=tk.LEFT, anchor=tk.N)

        results_label = tk.Label(config_frame, bg='gray15')
        results_label.config(bd=0, text='Configurations', font='System 10', fg='yellow')
        results_label.pack(side=tk.TOP, anchor=tk.N)

        # Present the current configurations' details
        # Config ID
        config_id_container = tk.Frame(config_frame, bg='gray15')
        config_id_container.pack(anchor=tk.W, fill=tk.X, expand=True, side=tk.TOP)

        id_label = tk.Label(config_id_container, text='ID: {}'.format(CURRENT_CONFIG_ID), bg='gray15')
        id_label.pack(side=tk.LEFT, anchor=tk.W, padx=8, pady=5)

        # Config container
        config_name_container = tk.Frame(config_frame, bg='gray15')
        config_name_container.pack(anchor=tk.W, fill=tk.X, expand=True, side=tk.TOP)

        # Find the config_name of the config at this ID
        config_name_fetch = c.execute('SELECT config_name FROM SavedConfigs WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
        self.config_name = [x[0] for x in config_name_fetch][0]

        config_name_label = tk.Label(config_name_container, text='Name: {}'.format(self.config_name), bg='gray15')
        config_name_label.pack(side=tk.LEFT, anchor=tk.W, padx=8, pady=5)

        # Delete current configuration.
        delete_config = tk.Button(config_frame)
        delete_config.config(relief=tk.RAISED, bd=5, text='    Delete Configuration?    ',
                                 command=self.delete_config_db)
        delete_config.pack(side=tk.TOP, anchor=tk.S, pady=15, padx=15)

        # Existing frame
        compare_configs = tk.Frame(config_frame, bg='gray15')
        compare_configs.pack(side=tk.RIGHT, padx=5, pady=5)

        config_compare = tk.Label(compare_configs)
        config_compare.config(text='Select Two Configurations to Compare')
        config_compare.pack()

        # Fetch the existing configurations' names from the database
        existing_configs_fetch = c.execute('SELECT config_name FROM SavedConfigs').fetchall()
        self.existing_configs = [x[0] for x in existing_configs_fetch]

        # Seperate frames for each selection
        current_config_container = tk.Frame(compare_configs, bg='gray15')
        current_config_container.pack(side=tk.LEFT, padx=5, pady=5)

        # Current Config
        current_config_label = tk.Label(current_config_container)
        current_config_label.config(text='Current Configuration')
        current_config_label.pack(anchor=tk.W)

        # Create a combobox for hosting the configs.
        self.current_config_combo = ttk.Combobox(current_config_container)

        self.current_config_combo['values'] = [self.config_name]
        self.current_config_combo.current(0)
        self.current_config_combo.pack()

        # Seperate frames for each selection
        compare_config_container = tk.Frame(compare_configs, bg='gray15')
        compare_config_container.pack(side=tk.LEFT, padx=5, pady=5)

        # Compare Config
        compare_config_label = tk.Label(compare_config_container)
        compare_config_label.config(text='Comparison Configuration')
        compare_config_label.pack(anchor=tk.E)

        # Create a combobox for hosting the configs.
        self.compare_config_combo = ttk.Combobox(compare_config_container)

        # Remove the current config from the list
        self.existing_configs.remove(str(self.config_name))

        self.compare_config_combo['values'] = self.existing_configs
        self.compare_config_combo.bind('<KeyRelease>', self.check_config_input)
        self.compare_config_combo.pack()

        # Bind combobox selection to open the program on a notice.
        master.bind("<<ComboboxSelected>>", self.compare_configs)

        # Comparison Report Directory Browse Frame
        directory_browse_container = tk.Frame(compare_configs, bg='gray15')
        directory_browse_container.pack(fill=tk.X, expand=True)

        # Display Comparison Report PDFs default directory and a button to change it.
        browsebutton = tk.Button(directory_browse_container, text="Browse", command=self.browsefunc)
        browsebutton.pack(anchor=tk.W)

        self.directory_default_var = tk.StringVar()
        self.directory_default_var.set('D:\Desktop\Programming\Heat Exchanger Avg Cost\main revamped\multi file structure\PDFReports')

        self.directory_display = ttk.Entry(directory_browse_container, textvariable=self.directory_default_var)
        self.directory_display.pack(anchor=tk.E)

    def browsefunc(self):
        filename = filedialog.askopenfilename(initialdir = "D:\Desktop\Programming\Heat Exchanger Avg Cost\main revamped\multi file structure\PDFReports")
        self.directory_default_var.set(filename)


    def compare_configs(self, event):
        if str(event.widget) != ".!notebook.!frame7.!frame3.!frame3.!frame.!combobox":
            # This is the comparison box, hence we prompt to ensure this is the correct one.
            confirm_compare = ms.askokcancel('WARNING', 'Are you sure you want to compare {} to {}?'.format(self.config_name, event.widget.get()))
            if confirm_compare:
                # Yes, they want to compare these two.

                # Create a new empty .pdf file in the PDFReport folder
                save_path = 'D:\Desktop\Programming\Heat Exchanger Avg Cost\main revamped\multi file structure\PDFReports'

                # The file name will be decided by the 1st config vs the 2nd config names.
                fused_file_name = str(self.current_config_combo.get()) + "v" + str(self.compare_config_combo.get())

                completeName = os.path.join(save_path, fused_file_name+".pdf")
                save_file = open(completeName, "w")
                save_file.close()



                # Get the current ID from the txt file
                f = open("config_id.txt", "r")
                CURRENT_CONFIG_ID = f.read()
                f.close()

                # Clear the Anvil Data Tables
                app_tables.componentdata.delete_all_rows()
                app_tables.savedconfigs.delete_all_rows()

                # Write data onto the Anvil Data Table - ComponentData
                # Current
                fetch_compdata_current = c.execute('SELECT id, config_id, type, name, metric, quantity, individual_cost, total_cost FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()

                for row in fetch_compdata_current:
                    app_tables.componentdata.add_row(id=row[0], config_id=row[1], type=row[2], name=row[3], metric=row[4], quantity=row[5], individual_cost=row[6], total_cost=row[7])

                # Write data onto the Anvil Data Table - SavedConfigs
                # Current
                fetch_savedconfigs_current = c.execute('SELECT config_id, config_name FROM SavedConfigs WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()

                for row in fetch_savedconfigs_current:
                    app_tables.savedconfigs.add_row(config_id=row[0], config_name=row[1])

                # Initiate the CSV process.
                # Must create 2 CSV files hosting both the configurations' data.

                # Load in the CurrentConfig.csv
                current_query = pd.read_sql_query("""
                    SELECT * FROM ComponentData
                    WHERE config_id=?
                    """
                    , db, params=(CURRENT_CONFIG_ID,))

                current_df = pd.DataFrame(current_query)
                current_df.to_csv(r'D:\Desktop\Programming\Heat Exchanger Avg Cost\main revamped\multi file structure\CurrentConfig.csv', index=False)

                # Load the corresponding SavedConfigs Table as well
                current_saved_query = pd.read_sql_query("""
                    SELECT * FROM SavedConfigs
                    WHERE config_id=?
                    """
                    , db, params=(CURRENT_CONFIG_ID,))

                current_saved_df = pd.DataFrame(current_saved_query)

                # Merge Tables
                current_merged_df = current_df.merge(current_saved_df, on='config_id', how='left')

                # Convert to csv
                current_merged_df.to_csv(r'D:\Desktop\Programming\Heat Exchanger Avg Cost\main revamped\multi file structure\CurrentConfig.csv', index=False)

                # Fetch the config_id that matches the config_name
                config_id_fetch = c.execute('SELECT config_id FROM SavedConfigs WHERE config_name=?', (event.widget.get(),)).fetchall()
                config_id = [x[0] for x in config_id_fetch][0]

                # Populate Data table with Target components
                # Target
                fetch_compdata_target = c.execute('SELECT id, config_id, type, name, metric, quantity, individual_cost, total_cost FROM ComponentData WHERE config_id=?', (config_id,)).fetchall()

                for row in fetch_compdata_target:
                    app_tables.componentdata.add_row(id=row[0], config_id=row[1], type=row[2], name=row[3], metric=row[4], quantity=row[5], individual_cost=row[6], total_cost=row[7])

                # Write data onto the Anvil Data Table - SavedConfigs
                # Target
                fetch_savedconfigs_target = c.execute('SELECT config_id, config_name FROM SavedConfigs WHERE config_id=?', (config_id,)).fetchall()

                for row in fetch_savedconfigs_target:
                    app_tables.savedconfigs.add_row(config_id=row[0], config_name=row[1])

                # Load in the TargetConfig.csv
                target_query = pd.read_sql_query("""
                    SELECT * FROM ComponentData
                    WHERE config_id=?
                    """
                    , db, params=(config_id,))

                target_df = pd.DataFrame(target_query)

                # Load the corresponding SavedConfigs Table as well
                target_saved_query = pd.read_sql_query("""
                    SELECT * FROM SavedConfigs
                    WHERE config_id=?
                    """
                    , db, params=(config_id,))

                target_saved_df = pd.DataFrame(target_saved_query)

                # Merge Tables
                target_merged_df = target_df.merge(target_saved_df, on='config_id', how='left')

                # Convert to csv
                target_merged_df.to_csv(r'D:\Desktop\Programming\Heat Exchanger Avg Cost\main revamped\multi file structure\TargetConfig.csv', index=False)

                # Read the CSVs
                current_config_csv = pd.read_csv("CurrentConfig.csv")
                target_config_csv = pd.read_csv("TargetConfig.csv")

                # Combine the CSVs
                combined_csv = pd.concat([current_config_csv, target_config_csv])

                # Pass the data
                records = combined_csv.to_dict('records')

                # Create the PDF
                pdf = PdfRenderer(filename="ORCSystemCompareReport.pdf", page_size='A4').render_form("CompareConfigReport", records)
                anvil.media.write_to_file(pdf, "ORCSystemCompareReport.pdf")

    def check_config_input(self, event):
        value = event.widget.get()

        if value == '':
            self.compare_config_combo['values'] = self.existing_configs
        elif value == self.current_config_combo.get():
            ms.showerror('Error', 'Cannot compare the same configurations!')
        else:
            data = []
            for item in self.existing_configs:
                if value.lower() in item.lower():
                    data.append(item)

            self.compare_config2_combo['values'] = data

    def delete_config_db(self):
        # Ask the user if they truly want to do this
        confirm_deletion = ms.askokcancel('Deletion', 'Deleting a configuration will removed all associated information within the configuration from the database permanently and irreversibly.\n\nDeleting the config will exit the system.\n\nAre you sure you want to continue?')
        if confirm_deletion:
            # Get the current ID from the txt file
            f = open("config_id.txt", "r")
            CURRENT_CONFIG_ID = f.read()
            f.close()

            # Delete the components from the database
            c.execute('DELETE FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,))
            db.commit()

            # Delete the config_id row from the SavedConfigs table.
            c.execute('DELETE FROM SavedConfigs WHERE config_id=?', (CURRENT_CONFIG_ID,))
            db.commit()

            # Exit the system
            sys.exit()

    def save_config_db(self):
        # Ask the user if they want to save the currently submitted components
        confirm_save = ms.askokcancel('Save', 'This will save the configuration of the set of components submitted.\nIt may be accessed for viewing/deleting/editing at any time using the Menu at startup.\n\nAre you sure you want to save this configuration?')
        if confirm_save == 'yes':
            # Go through with the saving process
            # Prepare the date using Pandas
            # Design the PDF layout
            # Display the data of the configuration on the PDF
            # Pass the data into Anvil ()
            # Display a table of the current components in the configuration
            # Display the total costs and component quantities among other possible factors.
            # Plot graphs and charts on the PDF using the data calculated.

            # Get the current ID from the txt file
            f = open("config_id.txt", "r")
            CURRENT_CONFIG_ID = f.read()
            f.close()

            # Save the current configuration to the list of configurations displayed.
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
                if str(column) == '#5':
                    try:
                        float_entry = float(entry.get())
                        print(float_entry)
                        if float_entry == 0.0 or float_entry == 0 or float_entry == '':
                            ms.showerror('Invalid', 'Invalid Area/Power/Volume Input.')
                        else:
                            self.treeview.set(item, column, entry.get())
                            entry.destroy()

                            row_id = self.treeview.item(item)['values'][0]
                            row_type = self.treeview.item(item)['values'][2]
                            row_name = self.treeview.item(item)['values'][3]
                            row_metric = float(self.treeview.item(item)['values'][4])
                            row_quantity = int(self.treeview.item(item)['values'][5])

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

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Shell and Tube':
                                self.snt_cost = (627.9 * row_metric ** 0.9199)
                                self.snt_quantity_cost = self.snt_cost * row_quantity
                                self.total_snt_cost += self.snt_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.snt_cost, 2)
                                comp_total_cost = round(self.total_snt_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Plate':
                                self.plate_cost = (2667.7 * row_metric ** 0.3472)
                                self.plate_quantity_cost = self.plate_cost * row_quantity
                                self.total_plate_cost += self.plate_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.plate_cost, 2)
                                comp_total_cost = round(self.total_plate_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Air-Cooled Condenser':
                                self.acc_cost = (1706.2 * row_metric ** 0.4301)
                                self.acc_quantity_cost = self.acc_cost * row_quantity
                                self.total_acc_cost += self.acc_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.acc_cost, 2)
                                comp_total_cost = round(self.total_acc_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Pump':
                                self.pump_cost = (1513.4 * row_metric ** 0.1946)
                                self.pump_quantity_cost = self.pump_cost * row_quantity
                                self.total_pump_cost += self.pump_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.pump_cost, 2)
                                comp_total_cost = round(self.total_pump_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Expander':
                                self.expander_cost = (544 * row_metric ** 0.8331)
                                self.expander_quantity_cost = self.expander_cost * row_quantity
                                self.total_expander_cost += self.expander_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.expander_cost, 2)
                                comp_total_cost = round(self.total_expander_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Storage Tank':
                                self.st_cost = (52.6 * row_metric ** 0.5531)
                                self.st_quantity_cost = self.st_cost * row_quantity
                                self.total_st_cost += self.st_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.st_cost, 2)
                                comp_total_cost = round(self.total_st_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            # Change the values in the database on the correct row.
                            c.execute('UPDATE ComponentData SET name=?, metric=?, quantity=?, individual_cost=?, total_cost=? WHERE id=?', (row_name, row_metric, row_quantity, comp_individual_cost, comp_total_cost, row_id,))
                            db.commit()

                            total_system_cost = 0
                            total_quantity = 0

                            # Write it to a txt file and read it off when adding a new component
                            f = open("config_id.txt", "r")
                            CURRENT_CONFIG_ID = f.read()
                            f.close()

                            comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
                            comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
                            for quantity in comp_values_quantity:
                                total_quantity += quantity

                            comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
                            comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
                            for individual_cost in comp_values_individual_costs:
                                total_system_cost += individual_cost

                            self.results_label["text"] = 'Total System Cost: £%.2f' % round(total_system_cost, 2)
                            self.results_quantity_total_label["text"] = 'Across %d Components' % total_quantity
                            ms.showinfo('Updated', 'Cost has been updated to £{total_system_cost}\nAcross {total_quantity} Components'.format(total_system_cost=round(total_system_cost, 2), total_quantity=total_quantity))

                    except ValueError:
                        ms.showerror('Invalid', 'Invalid Area/Power/Volume Input.')

                elif str(column) == '#6':
                    try:
                        int_entry = int(entry.get())
                        if int_entry == 0 or int_entry == '':
                            ms.showerror('Invalid', 'Invalid Quantity Input.')
                        else:
                            self.treeview.set(item, column, entry.get())
                            entry.destroy()

                            row_id = self.treeview.item(item)['values'][0]
                            row_type = self.treeview.item(item)['values'][2]
                            row_name = self.treeview.item(item)['values'][3]
                            row_metric = float(self.treeview.item(item)['values'][4])
                            row_quantity = int(self.treeview.item(item)['values'][5])

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

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Shell and Tube':
                                self.snt_cost = (627.9 * row_metric ** 0.9199)
                                self.snt_quantity_cost = self.snt_cost * row_quantity
                                self.total_snt_cost += self.snt_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.snt_cost, 2)
                                comp_total_cost = round(self.total_snt_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Plate':
                                self.plate_cost = (2667.7 * row_metric ** 0.3472)
                                self.plate_quantity_cost = self.plate_cost * row_quantity
                                self.total_plate_cost += self.plate_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.plate_cost, 2)
                                comp_total_cost = round(self.total_plate_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Air-Cooled Condenser':
                                self.acc_cost = (1706.2 * row_metric ** 0.4301)
                                self.acc_quantity_cost = self.acc_cost * row_quantity
                                self.total_acc_cost += self.acc_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.acc_cost, 2)
                                comp_total_cost = round(self.total_acc_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Pump':
                                self.pump_cost = (1513.4 * row_metric ** 0.1946)
                                self.pump_quantity_cost = self.pump_cost * row_quantity
                                self.total_pump_cost += self.pump_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.pump_cost, 2)
                                comp_total_cost = round(self.total_pump_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Expander':
                                self.expander_cost = (544 * row_metric ** 0.8331)
                                self.expander_quantity_cost = self.expander_cost * row_quantity
                                self.total_expander_cost += self.expander_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.expander_cost, 2)
                                comp_total_cost = round(self.total_expander_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            elif row_type == 'Storage Tank':
                                self.st_cost = (52.6 * row_metric ** 0.5531)
                                self.st_quantity_cost = self.st_cost * row_quantity
                                self.total_st_cost += self.st_quantity_cost

                                # Set them to a general variable to be used.
                                comp_individual_cost = round(self.st_cost, 2)
                                comp_total_cost = round(self.total_st_cost, 2)

                                self.treeview.set(item, '#7', comp_individual_cost)
                                self.treeview.set(item, '#8', comp_total_cost)

                            # Change the values in the database on the correct row.
                            c.execute('UPDATE ComponentData SET name=?, metric=?, quantity=?, individual_cost=?, total_cost=? WHERE id=?', (row_name, row_metric, row_quantity, comp_individual_cost, comp_total_cost, row_id,))
                            db.commit()

                            total_system_cost = 0
                            total_quantity = 0

                            # Write it to a txt file and read it off when adding a new component
                            f = open("config_id.txt", "r")
                            CURRENT_CONFIG_ID = f.read()
                            f.close()

                            comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
                            comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
                            for quantity in comp_values_quantity:
                                total_quantity += quantity

                            comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
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
                    row_name = self.treeview.item(item)['values'][3]
                    row_metric = float(self.treeview.item(item)['values'][4])
                    row_quantity = int(self.treeview.item(item)['values'][5])

                    # Need to update the costs according to the changes too.
                    row_individual_cost = self.treeview.item(item)['values'][5]
                    row_total_cost = self.treeview.item(item)['values'][6]

                    # Change the values in the database on the correct row.
                    c.execute('UPDATE ComponentData SET name=?, metric=?, quantity=?, individual_cost=?, total_cost=? WHERE id=?', (row_name, row_metric, row_quantity, row_individual_cost, row_total_cost, row_id,))
                    db.commit()

            column = self.treeview.identify_column(event.x)
            column_str = str(column)
            if column_str != '#4' and column_str != '#5' and column_str != '#6':
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

        # Write it to a txt file and read it off when adding a new component
        f = open("config_id.txt", "r")
        CURRENT_CONFIG_ID = f.read()
        f.close()

        total_system_cost = 0
        total_quantity = 0

        # Update total system cost upon deletion
        comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
        comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
        for quantity in comp_values_quantity:
            total_quantity += quantity

        comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
        comp_values_individual_costs = [x[0] for x in comp_values_individual_costs_fetch]
        for individual_cost in comp_values_individual_costs:
            total_system_cost += individual_cost

        self.results_label["text"] = 'Total System Cost: £%.2f' % round(total_system_cost, 2)
        self.results_quantity_total_label["text"] = 'Across %d Components' % total_quantity
        ms.showinfo('Updated', 'Cost has been updated to £{total_system_cost}\nAcross {total_quantity} Components'.format(total_system_cost=round(total_system_cost, 2), total_quantity=total_quantity))

    def clear_config(self):
        confirm_clear = ms.askokcancel('WARNING', 'Clearing the database is permanent.\nAny components that were stored will be deleted forever.\nDo you wish to continue?')
        if confirm_clear:
            # Write it to a txt file and read it off when adding a new component
            f = open("config_id.txt", "r")
            CURRENT_CONFIG_ID = f.read()
            f.close()

            # Clear the database
            c.execute('DELETE FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,))
            db.commit()

            ms.showinfo('Success', 'Configuration has been cleared.')

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

        # Write it to a txt file and read it off when adding a new component
        f = open("config_id.txt", "r")
        CURRENT_CONFIG_ID = f.read()
        f.close()

        comp_values_quantity_fetch = c.execute('SELECT quantity FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
        comp_values_quantity = [x[0] for x in comp_values_quantity_fetch]
        for quantity in comp_values_quantity:
            total_quantity += quantity

        comp_values_individual_costs_fetch = c.execute('SELECT total_cost FROM ComponentData WHERE config_id=?', (CURRENT_CONFIG_ID,)).fetchall()
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
