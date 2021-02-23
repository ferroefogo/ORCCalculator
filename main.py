#  Main app launch
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
import sqlite3
from tkinter.simpledialog import askstring

# External imports
from home import Home
from turbines import Turbines
from heatexchangers import HeatExchangers
from pumps import Pumps
from expanders import Expanders
from storagetanks import StorageTanks
from results import Results
from about import About

# Connect to database
with sqlite3.connect('ComponentData.db') as db:
    c = db.cursor()


class ConfigChoice():
    def __init__(self, master):
        self.master = master
        # Window parameters
        self.master.title('Configuration Choice')
        self.master.configure(bg='gray20')
        self.master.option_add("*foreground", "yellow")
        self.master.option_add("*background", "gray15")
        self.master.geometry("500x500")

        self.config_name = ''

        main_frame = tk.Frame(self.master, relief=tk.FLAT)
        main_frame.pack(fill=tk.BOTH, side=tk.TOP)

        main_label = tk.Label(main_frame, text='ORC System Cost Calculator')
        main_label.pack(fill=tk.X, anchor=tk.N)

        header_frame = tk.Frame(self.master)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        header = tk.Label(header_frame, text='Configurations', font='System 30')
        header.pack(side=tk.TOP)

        header_description = tk.Label(header_frame, text='Create a new configuration or continue with a previous one.', font='System 8')
        header_description.pack(side=tk.TOP)

        # Choice options
        self.config_option_frame = tk.Frame(self.master, bg='gray20')
        self.config_option_frame.pack(side=tk.TOP, fill=tk.X)

        # Start New frame
        start_new_config_frame = tk.Frame(self.config_option_frame, bg='gray20')
        start_new_config_frame.pack(side=tk.LEFT, padx=5, pady=5)

        start_new_config_btn = tk.Button(start_new_config_frame)
        start_new_config_btn.config(relief=tk.RAISED, bd=5, text='Start a new Configuration',
                                 command=self.start_new_config)
        start_new_config_btn.pack(side=tk.LEFT, anchor=tk.N)

        # Existing frame
        self.existing_config_frame = tk.Frame(self.config_option_frame, bg='gray20')
        self.existing_config_frame.pack(side=tk.RIGHT, padx=5, pady=5)

        select_existing_config_btn = tk.Label(self.existing_config_frame)
        select_existing_config_btn.config(text='Select an existing Configuration')
        select_existing_config_btn.pack()

        # Create a combobox for hosting the configs.
        self.saved_config_combo = ttk.Combobox(self.existing_config_frame)

        # Fetch the existing configurations' names from the database
        existing_configs_fetch = c.execute('SELECT config_name FROM SavedConfigs').fetchall()
        self.existing_configs = [x[0] for x in existing_configs_fetch]

        self.saved_config_combo['values'] = self.existing_configs
        self.saved_config_combo.bind('<KeyRelease>', self.check_input)
        self.saved_config_combo.pack()

        # Bind combobox selection to open the program on a notice.
        master.bind("<<ComboboxSelected>>", self.existing_config)

    def existing_config(self, event):
        # Find the name of the current configuration selected
        config_name = self.saved_config_combo.get()
        confirm_choice = ms.askokcancel('Configuration Selected', 'Are you sure you want to open configuration {}?'.format(config_name))
        if confirm_choice:
            # Yes, they want to edit this one, continue.
            # Destroy all the widgets in the root window.
            for child in self.master.winfo_children():
                child.destroy()

            # The user wants to start a new configuration.
            select_next_highest_config_id = c.execute('SELECT config_id FROM SavedConfigs WHERE config_name=?', (config_name,)).fetchall()
            next_highest_config_id = [x[0] for x in select_next_highest_config_id][0]

            # Write it to a txt file and read it off when adding a new component
            with open("config_id.txt", "w") as f:
                f.write(str(next_highest_config_id))

            # Launch the MainApp page, along with the required data for the config.
            MainApp(self.master)

    def start_new_config(self):
        # Prompt user to enter config name
        config_name = askstring('Configuration Name', 'Enter the Configuration Name below')

        # Check all names in the database, and check if the input name matches any names in the database.
        config_names_fetch = c.execute('SELECT config_name FROM SavedConfigs')
        config_names = [x[0] for x in config_names_fetch]

        if config_name == '':
            ms.showerror('Error', 'Invalid configuration name.')
        elif config_name in config_names:
            ms.showerror('Error', 'Configuration name already exists.')
        elif config_name is not None:
            # The user wants to start a new configuration.
            select_next_highest_config_id = c.execute('SELECT MAX(config_id)+1 FROM SavedConfigs').fetchall()
            next_highest_config_id = [x[0] for x in select_next_highest_config_id][0]

            # Let the next inserted components into the database have a higher config_id (+1 from the current highest)
            # Write it to a txt file and read it off when adding a new component
            f = open("config_id.txt", "w")
            f.write(str(next_highest_config_id))
            f.close()

            # Insert the config_id into the SavedConfigs table.
            c.execute('INSERT INTO SavedConfigs(config_id, config_name) VALUES(?,?)', (next_highest_config_id, config_name))
            db.commit()

            # Destroy all the widgets in the root window.
            for child in self.master.winfo_children():
                child.destroy()

            MainApp(self.master)

    def check_input(self, event):
        value = event.widget.get()

        if value == '':
            self.saved_config_combo['values'] = self.existing_configs
        else:
            data = []
            for item in self.existing_configs:
                if value.lower() in item.lower():
                    data.append(item)

            self.saved_config_combo['values'] = data


class MainApp():
    def __init__(self, master):
        self.master = master
        master.configure(bg='gray15')
        master.title('Component Cost Calculator')
        master.option_add('*Font', 'System 12')
        master.option_add('*Label.Font', 'System 14')
        master.geometry('1920x1080')

        master.protocol("WM_DELETE_WINDOW", self.on_close)

        # Window Icon
        # master.iconbitmap('ocrbigger.ico')

        global_frame = tk.Frame(master, relief=tk.FLAT, bd=1, bg='gray15')
        global_frame.pack(fill=tk.BOTH, side=tk.TOP)

        global_label = tk.Label(global_frame, relief=tk.GROOVE, bd=1)
        global_label.config(text='Component Cost Calculator v5.0', font='System 12')
        global_label.pack(fill=tk.X, anchor=tk.N)

        # Have a global 'Exit Current Configuration' Button.
        # Sort of like a logout button, if you will.
        exit_current_config_button = ttk.Button(global_frame, text='Exit Configuration', command=self.exit_current_config)
        exit_current_config_button.pack(side=tk.RIGHT)

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

    def exit_current_config(self):
        exit_confirmation = ms.askquestion('Exit Current Configuration', 'Are you sure you want to exit the current configuration?\n\nAll your components entered so far will be saved automatically and can be accessed at any time.', icon='warning')
        if exit_confirmation == 'yes':
            # Destroy all the widgets in the root window.
            for child in self.master.winfo_children():
                child.destroy()

            # Launch the SignIn page to allow the user to login again.
            ConfigChoice(self.master)

    def on_close(self):
        close = ms.askokcancel('Cancel', 'Would you like to close the program?')
        if close:
            self.master.destroy()


def main():
    root = tk.Tk()
    ConfigChoice(root)
    root.mainloop()


if __name__ == "__main__":
    main()
