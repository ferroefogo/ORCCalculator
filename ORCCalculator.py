import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class NotebookTest():
    def __init__(self, master):
        #declaring variables
        self.total_comp_types = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.total_comp_names = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.total_comp_values = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.total_comp_quantities = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.total_comp_individual_costs = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.total_comp_quantity_cost = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        self.total_system_cost = 0

        
        # Turbine Costs
        self.turbs_cost_1 = 0
        self.turbs_cost_2 = 0
        self.turbs_cost_3 = 0
        self.turbs_cost_4 = 0
        self.turbs_cost_5 = 0

        # Heat Exchanger - Shell and Tube Costs
        self.snt_cost_1 = 0
        self.snt_cost_2 = 0
        self.snt_cost_3 = 0
        self.snt_cost_4 = 0
        self.snt_cost_5 = 0

        # Heat Exchanger - Plate Costs
        self.plate_cost_1 = 0
        self.plate_cost_2 = 0
        self.plate_cost_3 = 0
        self.plate_cost_4 = 0
        self.plate_cost_5 = 0

        # Heat Exchanger - ACC Costs
        self.acc_cost_1 = 0
        self.acc_cost_2 = 0
        self.acc_cost_3 = 0
        self.acc_cost_4 = 0
        self.acc_cost_5 = 0

        # Pump Costs
        self.pump_cost_1 = 0
        self.pump_cost_2 = 0
        self.pump_cost_3 = 0
        self.pump_cost_4 = 0
        self.pump_cost_5 = 0

        # Expander Costs
        self.expander_cost_1 = 0
        self.expander_cost_2 = 0
        self.expander_cost_3 = 0
        self.expander_cost_4 = 0
        self.expander_cost_5 = 0

        # Storage Tank Costs
        self.st_cost_1 = 0
        self.st_cost_2 = 0
        self.st_cost_3 = 0
        self.st_cost_4 = 0
        self.st_cost_5 = 0



        
        # Turbine Quantities
        self.turbine_quantity_1 = 0
        self.turbine_quantity_2 = 0
        self.turbine_quantity_3 = 0
        self.turbine_quantity_4 = 0
        self.turbine_quantity_5 = 0

        # Heat Exchanger - Shell and Tube Quantities
        self.snt_quantity_1 = 0
        self.snt_quantity_2 = 0
        self.snt_quantity_3 = 0
        self.snt_quantity_4 = 0
        self.snt_quantity_5 = 0

        # Heat Exchanger - Plate Quantities
        self.plate_quantity_1 = 0
        self.plate_quantity_2 = 0
        self.plate_quantity_3 = 0
        self.plate_quantity_4 = 0
        self.plate_quantity_5 = 0

        # Heat Exchanger - Air-Cooled Condenser Quantities
        self.acc_quantity_1 = 0
        self.acc_quantity_2 = 0
        self.acc_quantity_3 = 0
        self.acc_quantity_4 = 0
        self.acc_quantity_5 = 0

        #Pump Quantities
        self.pump_quantity_1 = 0
        self.pump_quantity_2 = 0
        self.pump_quantity_3 = 0
        self.pump_quantity_4 = 0
        self.pump_quantity_5 = 0

        #Expander Quantities
        self.expander_quantity_1 = 0
        self.expander_quantity_2 = 0
        self.expander_quantity_3 = 0
        self.expander_quantity_4 = 0
        self.expander_quantity_5 = 0

        #Storage Tank Quantities
        self.st_quantity_1 = 0
        self.st_quantity_2 = 0
        self.st_quantity_3 = 0
        self.st_quantity_4 = 0
        self.st_quantity_5 = 0



        ### Totals
        #Turbines Totals
        self.turbs_total_1 = 0
        self.turbs_total_2 = 0
        self.turbs_total_3 = 0
        self.turbs_total_3 = 0
        self.turbs_total_5 = 0
        self.turbs_total = 0

        #Heat Exchangers - SNT
        self.snt_total_1 = 0
        self.snt_total_2 = 0
        self.snt_total_3 = 0
        self.snt_total_4 = 0
        self.snt_total_5 = 0
        self.snt_total = 0

        #Heat Exchangers - Plate
        self.plate_total_1 = 0
        self.plate_total_2 = 0
        self.plate_total_3 = 0
        self.plate_total_4 = 0
        self.plate_total_5 = 0
        self.plate_total = 0

        #Heat Exchangers - ACC
        self.acc_total_1 = 0
        self.acc_total_2 = 0
        self.acc_total_3 = 0
        self.acc_total_4 = 0
        self.acc_total_5 = 0
        self.acc_total = 0

        #Pumps
        self.pump_total_1 = 0
        self.pump_total_2 = 0
        self.pump_total_3 = 0
        self.pump_total_4 = 0
        self.pump_total_5 = 0
        self.pump_total = 0

        #Expander
        self.expander_total_1 = 0
        self.expander_total_2 = 0
        self.expander_total_3 = 0
        self.expander_total_4 = 0
        self.expander_total_5 = 0
        self.expander_total = 0

        #Storage Tank
        self.st_total_1 = 0
        self.st_total_2 = 0
        self.st_total_3 = 0
        self.st_total_4 = 0
        self.st_total_5 = 0
        self.st_total = 0

        ### Values
        #Turbine Area Values
        self.turbine_power_1 = 0
        self.turbine_power_2 = 0
        self.turbine_power_3 = 0
        self.turbine_power_4 = 0
        self.turbine_power_5 = 0
        
        #SNT Area Values
        self.snt_area_1 = 0
        self.snt_area_2 = 0
        self.snt_area_3 = 0
        self.snt_area_4 = 0
        self.snt_area_5 = 0

        # Plate Area Values
        self.plate_area_1 = 0
        self.plate_area_2 = 0
        self.plate_area_3 = 0
        self.plate_area_4 = 0
        self.plate_area_5 = 0

        #ACC Area Values
        self.acc_area_1 = 0
        self.acc_area_2 = 0
        self.acc_area_3 = 0
        self.acc_area_4 = 0
        self.acc_area_5 = 0

        #Pump Power Values
        self.pump_power_1 = 0
        self.pump_power_2 = 0
        self.pump_power_3 = 0
        self.pump_power_4 = 0
        self.pump_power_5 = 0

        #Expander Power Values
        self.expander_power_1 = 0
        self.expander_power_2 = 0
        self.expander_power_3 = 0
        self.expander_power_4 = 0
        self.expander_power_5 = 0

        #Storage Tank Volumes
        self.st_volume_1 = 0
        self.st_volume_2 = 0
        self.st_volume_3 = 0
        self.st_volume_4 = 0
        self.st_volume_5 = 0
        


        
        # configuration
        master.configure(bg='gray15')
        master.title('Component Cost Calculator')
        master.option_add('*Font', 'System 12')
        master.option_add('*Label.Font', 'System 14')
        master.geometry('1920x1080')
        master.wm_state('zoomed')

        
        frame1_page1 = tk.Frame(master, relief=tk.FLAT, borderwidth=1, bg='gray15')
        frame1_page1.pack(side=tk.TOP, fill=tk.BOTH)

        logo_header = tk.Label(frame1_page1, relief=tk.GROOVE, borderwidth=1, bg='ghost white')
        logo_header.config(bd=0, text='Component Cost Calculator v2.16.5', font='System 12')
        logo_header.pack(fill=tk.X, anchor=tk.N)
        
        main_notebook = ttk.Notebook(master)
        main_notebook.pack(expand=True, fill=tk.BOTH)
        
        ### Making all 8 pages
        self.page0 = tk.Frame(main_notebook)
        main_notebook.add(self.page0, text='Home')
        
        self.page1 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page1, text="Turbine")
        
        self.page2 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page2, text="Heat Exchangers")

        self.page3 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page3, text="Pumps")

        self.page4 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page4, text="Expanders")

        self.page5 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page5, text="Storage Tanks")

        ### Making the Results page
        self.page6 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page6, text="Results")
        
        ### Making the Help page
        self.page7 = tk.Frame(main_notebook, bg='gray20')
        main_notebook.add(self.page7, text="About")


        home_frame = tk.Frame(self.page0, bg='gray20')
        home_frame.pack(expand=True)

        title_label = tk.Label(home_frame)
        title_label.config(bd=0, text='How to use this software', font='System 30')
        title_label.pack(expand=True, fill=tk.X,anchor=tk.N)

        howtouse_frame = tk.Frame(home_frame)
        howtouse_frame.pack(fill=tk.BOTH, expand=True)

        tip_label_1 = tk.Label(howtouse_frame)
        tip_label_1.config(bd=0, text="- Each tab shows each component and where said components' information must be entered.")
        tip_label_1.pack(side=tk.TOP)

        tip_label_2 = tk.Label(howtouse_frame)
        tip_label_2.config(bd=0, text='- Enter your information into any of the 5 (for now) given boxes accordingly.')
        tip_label_2.pack(side=tk.TOP)

        tip_label_3 = tk.Label(howtouse_frame)
        tip_label_3.config(bd=0, text="- Press the 'Enter Information' button once you have made sure all information entered is correct and you want to submit it into the final system cost calculation.")
        tip_label_3.pack(side=tk.TOP)

        tip_label_4 = tk.Label(howtouse_frame)
        tip_label_4.config(bd=0, text="- If you would like to go back and make a change, just edit the component information of the component in question and press the 'Enter Information' button again.")
        tip_label_4.pack(side=tk.TOP)

        tip_label_5 = tk.Label(howtouse_frame)
        tip_label_5.config(bd=0, text="- If you would like to remove a component from the final calculation, remove the components' NAME (leaving it as an empty field) and leave the AREA/POWER/VOLUME field as the value '0.0'.")
        tip_label_5.pack(side=tk.TOP)

        tip_label_6 = tk.Label(howtouse_frame)
        tip_label_6.config(bd=0, text="- You may press the column headings of the table at the 'Results' table to sort the information alphabetically or numerically.")
        tip_label_6.pack(side=tk.TOP)

        tip_label_7 = tk.Label(howtouse_frame)
        tip_label_7.config(bd=0, text="- When you are ready for the final total system calculation, press the 'Calculate' button in the 'Results' page and press OK on the prompt box. Your final value should update. At this point, you are free to go back and tinker any values prior.")
        tip_label_7.pack(side=tk.TOP)

        tip_label_8 = tk.Label(howtouse_frame)
        tip_label_8.config(bd=0, text="- It may sometimes appear that the 'Results' table is empty, though it is most likely that the component is at the bottom of the list. Simple scroll down to find it.")
        tip_label_8.pack(side=tk.TOP)


        ### About page
        about_frame = tk.Frame(self.page7, bg='gray20')
        about_frame.pack(expand=True)

        title_label_1 = tk.Label(about_frame, bg='gray20')
        title_label_1.config(bd=0, text='Software Developed by Marco Fernandes', font='System 30', fg='yellow')
        title_label_1.pack(expand=True, fill=tk.X,anchor=tk.N)

        title_label_2 = tk.Label(about_frame, bg='gray20')
        title_label_2.config(bd=0, text='Component Cost Equations Developed by Robert Platica', font='System 30', fg='yellow')
        title_label_2.pack(expand=True, fill=tk.X,anchor=tk.N)

        aboutme_frame = tk.Frame(about_frame)
        aboutme_frame.pack(fill=tk.BOTH, expand=True)

        about_label = tk.Label(aboutme_frame, bg='gray20')
        about_label.config(bd=0, text='- Support for 20+ components to be developed.', fg='yellow')
        about_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        

        


        # enter information button +frame
        enter_info_frame_page1 = tk.Frame(self.page1, bg='gray25')
        enter_info_frame_page1.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page4 = tk.Frame(enter_info_frame_page1, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page4.pack(side=tk.BOTTOM)

        enter_info_button_label_page4 = tk.Label(enter_info_frame_page1, relief=tk.GROOVE, bg='gray15')
        enter_info_button_label_page4.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_label_page4.pack(pady=10)

        enter_info_button_page4 = tk.Button(enter_info_frame_page1)
        enter_info_button_page4.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page4.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)



        ### Turbines GUI
        main_frame_page1_1 = tk.Frame(self.page1, bg='gray15')
        main_frame_page1_1.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page1_1 = tk.Frame(main_frame_page1_1, bg='gray15')
        info_canvas_title_frame_page1_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page1_1 = tk.Label(info_canvas_title_frame_page1_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page1_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page1_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page1_1 = tk.Canvas(info_canvas_title_frame_page1_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page1_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_turb_frame_1 = tk.Frame(infobox_canvas_page1_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_turb_label_1 = tk.Label(infobox_cname_turb_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_label_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_turb_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page1.register(self.cname_validate)

        self.entry_cname_turb_var_1 = tk.StringVar(self.page1)
        self.entry_cname_turb_var_1.set('')
        infobox_cname_turb_entry_1 = tk.Entry(infobox_cname_turb_frame_1)
        infobox_cname_turb_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_turb_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_turb_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_turb_frame_1 = tk.Frame(infobox_canvas_page1_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_turb_label_1 = tk.Label(infobox_power_turb_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_label_1.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_turb_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page1.register(self.power_validate)

        self.entry_power_turb_var_1 = tk.DoubleVar(self.page1)
        self.entry_power_turb_var_1.set('0.0')
        infobox_power_turb_entry_1 = tk.Entry(infobox_power_turb_frame_1)
        infobox_power_turb_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_turb_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_turb_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_turb_frame_1 = tk.Frame(infobox_canvas_page1_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_turb_label_1 = tk.Label(infobox_quantity_turb_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_label_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_turb_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page1.register(self.quantity_validate)

        self.entry_quantity_turb_var_1 = tk.IntVar(self.page1)
        self.entry_quantity_turb_var_1.set('1')
        infobox_quantity_turb_entry_1 = tk.Entry(infobox_quantity_turb_frame_1)
        infobox_quantity_turb_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_turb_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_turb_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        ### 2
        ### Turbines GUI
        main_frame_page1_2 = tk.Frame(self.page1, bg='gray15')
        main_frame_page1_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page1_2 = tk.Frame(main_frame_page1_2, bg='gray15')
        info_canvas_title_frame_page1_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page1_2 = tk.Label(info_canvas_title_frame_page1_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page1_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page1_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page1_2 = tk.Canvas(info_canvas_title_frame_page1_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page1_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_turb_frame_2 = tk.Frame(infobox_canvas_page1_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_turb_label_2 = tk.Label(infobox_cname_turb_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_label_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_turb_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page1.register(self.cname_validate)

        self.entry_cname_turb_var_2 = tk.StringVar(self.page1)
        self.entry_cname_turb_var_2.set('')
        infobox_cname_turb_entry_2 = tk.Entry(infobox_cname_turb_frame_2)
        infobox_cname_turb_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_turb_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_turb_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_turb_frame_2 = tk.Frame(infobox_canvas_page1_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_turb_label_2 = tk.Label(infobox_power_turb_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_label_2.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_turb_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page1.register(self.power_validate)

        self.entry_power_turb_var_2 = tk.DoubleVar(self.page1)
        self.entry_power_turb_var_2.set('0.0')
        infobox_power_turb_entry_2 = tk.Entry(infobox_power_turb_frame_2)
        infobox_power_turb_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_turb_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_turb_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_turb_frame_2 = tk.Frame(infobox_canvas_page1_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_turb_label_2 = tk.Label(infobox_quantity_turb_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_label_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_turb_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page1.register(self.quantity_validate)

        self.entry_quantity_turb_var_2 = tk.IntVar(self.page1)
        self.entry_quantity_turb_var_2.set('1')
        infobox_quantity_turb_entry_2 = tk.Entry(infobox_quantity_turb_frame_2)
        infobox_quantity_turb_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_turb_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_turb_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        ### 3
        ### Turbines GUI
        main_frame_page1_3 = tk.Frame(self.page1, bg='gray15')
        main_frame_page1_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page1_3 = tk.Frame(main_frame_page1_3, bg='gray15')
        info_canvas_title_frame_page1_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page1_3 = tk.Label(info_canvas_title_frame_page1_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page1_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page1_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page1_3 = tk.Canvas(info_canvas_title_frame_page1_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page1_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_turb_frame_3 = tk.Frame(infobox_canvas_page1_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_turb_label_3 = tk.Label(infobox_cname_turb_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_label_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_turb_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page1.register(self.cname_validate)

        self.entry_cname_turb_var_3 = tk.StringVar(self.page1)
        self.entry_cname_turb_var_3.set('')
        infobox_cname_turb_entry_3 = tk.Entry(infobox_cname_turb_frame_3)
        infobox_cname_turb_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_turb_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_turb_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_turb_frame_3 = tk.Frame(infobox_canvas_page1_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_turb_label_3 = tk.Label(infobox_power_turb_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_label_3.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_turb_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page1.register(self.power_validate)

        self.entry_power_turb_var_3 = tk.DoubleVar(self.page1)
        self.entry_power_turb_var_3.set('0.0')
        infobox_power_turb_entry_3 = tk.Entry(infobox_power_turb_frame_3)
        infobox_power_turb_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_turb_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_turb_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_turb_frame_3 = tk.Frame(infobox_canvas_page1_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_turb_label_3 = tk.Label(infobox_quantity_turb_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_label_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_turb_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page1.register(self.quantity_validate)

        self.entry_quantity_turb_var_3 = tk.IntVar(self.page1)
        self.entry_quantity_turb_var_3.set('1')
        infobox_quantity_turb_entry_3 = tk.Entry(infobox_quantity_turb_frame_3)
        infobox_quantity_turb_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_turb_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_turb_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)






        ### 4
        ### Turbines GUI
        main_frame_page1_4 = tk.Frame(self.page1, bg='gray15')
        main_frame_page1_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page1_4 = tk.Frame(main_frame_page1_4, bg='gray15')
        info_canvas_title_frame_page1_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page1_4 = tk.Label(info_canvas_title_frame_page1_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page1_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page1_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page1_4 = tk.Canvas(info_canvas_title_frame_page1_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page1_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_turb_frame_4 = tk.Frame(infobox_canvas_page1_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_turb_label_4 = tk.Label(infobox_cname_turb_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_label_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_turb_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page1.register(self.cname_validate)

        self.entry_cname_turb_var_4 = tk.StringVar(self.page1)
        self.entry_cname_turb_var_4.set('')
        infobox_cname_turb_entry_4 = tk.Entry(infobox_cname_turb_frame_4)
        infobox_cname_turb_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_turb_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_turb_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_turb_frame_4 = tk.Frame(infobox_canvas_page1_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_turb_label_4 = tk.Label(infobox_power_turb_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_label_4.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_turb_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page1.register(self.power_validate)

        self.entry_power_turb_var_4 = tk.DoubleVar(self.page1)
        self.entry_power_turb_var_4.set('0.0')
        infobox_power_turb_entry_4 = tk.Entry(infobox_power_turb_frame_4)
        infobox_power_turb_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_turb_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_turb_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_turb_frame_4 = tk.Frame(infobox_canvas_page1_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_turb_label_4 = tk.Label(infobox_quantity_turb_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_label_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_turb_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page1.register(self.quantity_validate)

        self.entry_quantity_turb_var_4 = tk.IntVar(self.page1)
        self.entry_quantity_turb_var_4.set('1')
        infobox_quantity_turb_entry_4 = tk.Entry(infobox_quantity_turb_frame_4)
        infobox_quantity_turb_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_turb_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_turb_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)





        ### 5
        ### Turbines GUI
        main_frame_page1_5 = tk.Frame(self.page1, bg='gray15')
        main_frame_page1_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page1_5 = tk.Frame(main_frame_page1_5, bg='gray15')
        info_canvas_title_frame_page1_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page1_5 = tk.Label(info_canvas_title_frame_page1_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page1_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page1_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page1_5 = tk.Canvas(info_canvas_title_frame_page1_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page1_5.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=15)

        # Component Name entry field
        infobox_cname_turb_frame_5 = tk.Frame(infobox_canvas_page1_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_turb_label_5 = tk.Label(infobox_cname_turb_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_turb_label_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_turb_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page1.register(self.cname_validate)

        self.entry_cname_turb_var_5 = tk.StringVar(self.page1)
        self.entry_cname_turb_var_5.set('')
        infobox_cname_turb_entry_5 = tk.Entry(infobox_cname_turb_frame_5)
        infobox_cname_turb_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_turb_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_turb_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_turb_frame_5 = tk.Frame(infobox_canvas_page1_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_turb_label_5 = tk.Label(infobox_power_turb_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_turb_label_5.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_turb_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page1.register(self.power_validate)

        self.entry_power_turb_var_5 = tk.DoubleVar(self.page1)
        self.entry_power_turb_var_5.set('0.0')
        infobox_power_turb_entry_5 = tk.Entry(infobox_power_turb_frame_5)
        infobox_power_turb_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_turb_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_turb_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_turb_frame_5 = tk.Frame(infobox_canvas_page1_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_turb_label_5 = tk.Label(infobox_quantity_turb_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_turb_label_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_turb_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page1.register(self.quantity_validate)

        self.entry_quantity_turb_var_5 = tk.IntVar(self.page1)
        self.entry_quantity_turb_var_5.set('1')
        infobox_quantity_turb_entry_5 = tk.Entry(infobox_quantity_turb_frame_5)
        infobox_quantity_turb_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_turb_var_5,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_turb_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)


        




        
        ### HEAT EXCHANGERS GUIs
        #Subheading of main page
        sub_notebook = ttk.Notebook(self.page2)
        sub_notebook.pack(expand=True, fill=tk.BOTH)

        page2a = tk.Frame(sub_notebook, bg='gray20')
        sub_notebook.add(page2a, text="Shell and Tube")

        page2b = tk.Frame(sub_notebook, bg='gray20')
        sub_notebook.add(page2b, text="Plate")

        page2c = tk.Frame(sub_notebook, bg='gray20')
        sub_notebook.add(page2c, text="Air-Cooled Condenser")

        # enter information button +frame
        enter_info_frame_page1_snt = tk.Frame(page2a, bg='gray25')
        enter_info_frame_page1_snt.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page4_snt = tk.Frame(enter_info_frame_page1_snt, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page4_snt.pack(side=tk.BOTTOM)

        enter_info_button_frame_page4_snt = tk.Label(enter_info_frame_page1_snt, relief=tk.GROOVE, bg='gray15')
        enter_info_button_frame_page4_snt.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_frame_page4_snt.pack(pady=10)

        enter_info_button_page4_snt = tk.Button(enter_info_frame_page1_snt)
        enter_info_button_page4_snt.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page4_snt.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)



        

        # enter information button +frame - plate
        enter_info_frame_page1_plate = tk.Frame(page2b, bg='gray25')
        enter_info_frame_page1_plate.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page4_plate = tk.Frame(enter_info_frame_page1_plate, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page4_plate.pack(side=tk.BOTTOM)

        enter_info_button_frame_page4_plate = tk.Label(enter_info_frame_page1_plate, relief=tk.GROOVE, bg='gray15')
        enter_info_button_frame_page4_plate.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_frame_page4_plate.pack(pady=10)

        enter_info_button_page4_plate = tk.Button(enter_info_frame_page1_plate)
        enter_info_button_page4_plate.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page4_plate.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)






        # enter information button +frame - acc
        enter_info_frame_page1_acc = tk.Frame(page2c, bg='gray25')
        enter_info_frame_page1_acc.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page4_acc = tk.Frame(enter_info_frame_page1_acc, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page4_acc.pack(side=tk.BOTTOM)

        enter_info_button_frame_page4_acc = tk.Label(enter_info_frame_page1_acc, relief=tk.GROOVE, bg='gray15')
        enter_info_button_frame_page4_acc.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_frame_page4_acc.pack(pady=10)

        enter_info_button_page4_acc = tk.Button(enter_info_frame_page1_acc)
        enter_info_button_page4_acc.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page4_acc.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)



        

        ### Shell n Tube GUI #1
        main_frame_page2a_1 = tk.Frame(page2a, bg='gray15')
        main_frame_page2a_1.pack(side=tk.LEFT, anchor=tk.N, padx=75, pady=10)

        info_canvas_title_frame_page2a_1 = tk.Frame(main_frame_page2a_1, bg='gray15')
        info_canvas_title_frame_page2a_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2a_1 = tk.Label(info_canvas_title_frame_page2a_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2a_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2a_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2a_1 = tk.Canvas(info_canvas_title_frame_page2a_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2a_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_snt_1 = tk.Frame(infobox_canvas_page2a_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_snt_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_snt_1 = tk.Label(infobox_cname_frame_snt_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_snt_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_snt_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2a.register(self.cname_validate)

        self.entry_cname_snt_var_1 = tk.StringVar(page2a)
        self.entry_cname_snt_var_1.set('')
        infobox_cname_snt_entry_1 = tk.Entry(infobox_cname_frame_snt_1)
        infobox_cname_snt_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_snt_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_snt_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_snt_frame_1 = tk.Frame(infobox_canvas_page2a_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_snt_label_1 = tk.Label(infobox_area_snt_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_label_1.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_snt_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2a.register(self.area_validate)

        self.entry_area_snt_var_1 = tk.DoubleVar(page2a)
        self.entry_area_snt_var_1.set('0.0')
        infobox_area_snt_entry_1 = tk.Entry(infobox_area_snt_frame_1)
        infobox_area_snt_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_snt_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_snt_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_snt_frame_1 = tk.Frame(infobox_canvas_page2a_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_snt_label_1 = tk.Label(infobox_quantity_snt_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_label_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_snt_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2a.register(self.quantity_validate)

        self.entry_quantity_snt_var_1 = tk.IntVar(page2a)
        self.entry_quantity_snt_var_1.set('1')
        infobox_quantity_snt_entry_1 = tk.Entry(infobox_quantity_snt_frame_1)
        infobox_quantity_snt_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_snt_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_snt_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)











        
        ### Plate GUI
        main_frame_page2b_1 = tk.Frame(page2b, bg='gray15')
        main_frame_page2b_1.pack(side=tk.LEFT, anchor=tk.N, padx=75, pady=10)

        info_canvas_title_frame_page2b_1 = tk.Frame(main_frame_page2b_1, bg='gray15')
        info_canvas_title_frame_page2b_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_plate_title_label_page2b_1 = tk.Label(info_canvas_title_frame_page2b_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_plate_title_label_page2b_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_plate_title_label_page2b_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2b_1 = tk.Canvas(info_canvas_title_frame_page2b_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2b_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_plate_frame_1 = tk.Frame(infobox_canvas_page2b_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_plate_label_1 = tk.Label(infobox_cname_plate_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_label_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_plate_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2b.register(self.cname_validate)

        self.entry_cname_plate_var_1 = tk.StringVar(page2b)
        self.entry_cname_plate_var_1.set('')
        infobox_cname_plate_entry_1 = tk.Entry(infobox_cname_plate_frame_1)
        infobox_cname_plate_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_plate_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_plate_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_plate_frame_1 = tk.Frame(infobox_canvas_page2b_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_plate_label_1 = tk.Label(infobox_area_plate_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_label_1.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_plate_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2b.register(self.area_validate)

        self.entry_area_plate_var_1 = tk.DoubleVar(page2b)
        self.entry_area_plate_var_1.set('0.0')
        infobox_area_plate_entry_1 = tk.Entry(infobox_area_plate_frame_1)
        infobox_area_plate_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_plate_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_plate_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_plate_frame_1 = tk.Frame(infobox_canvas_page2b_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_plate_label_1 = tk.Label(infobox_quantity_plate_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_label_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_plate_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2b.register(self.quantity_validate)

        self.entry_quantity_plate_var_1 = tk.IntVar(page2b)
        self.entry_quantity_plate_var_1.set('1')
        infobox_quantity_plate_entry_1 = tk.Entry(infobox_quantity_plate_frame_1)
        infobox_quantity_plate_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_plate_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_plate_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)





        
        ### Condenser
        main_frame_page2c_1 = tk.Frame(page2c, bg='gray15')
        main_frame_page2c_1.pack(side=tk.LEFT, anchor=tk.N, padx=75, pady=10)

        info_canvas_title_frame_page2c_1 = tk.Frame(main_frame_page2c_1, bg='gray15')
        info_canvas_title_frame_page2c_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2c_1 = tk.Label(info_canvas_title_frame_page2c_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2c_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2c_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2c_1 = tk.Canvas(info_canvas_title_frame_page2c_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2c_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_condenser_frame_1 = tk.Frame(infobox_canvas_page2c_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_condenser_label_1 = tk.Label(infobox_cname_condenser_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_label_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_condenser_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2c.register(self.cname_validate)

        self.entry_cname_condenser_var_1 = tk.StringVar(page2c)
        self.entry_cname_condenser_var_1.set('')
        infobox_cname_condenser_entry_1 = tk.Entry(infobox_cname_condenser_frame_1)
        infobox_cname_condenser_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_condenser_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_condenser_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_condenser_frame_1 = tk.Frame(infobox_canvas_page2c_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_condenser_label_1 = tk.Label(infobox_area_condenser_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_label_1.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_condenser_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2c.register(self.area_validate)

        self.entry_area_condenser_var_1 = tk.DoubleVar(page2c)
        self.entry_area_condenser_var_1.set('0.0')
        infobox_area_condenser_entry_1 = tk.Entry(infobox_area_condenser_frame_1)
        infobox_area_condenser_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_condenser_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_condenser_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_condenser_frame_1 = tk.Frame(infobox_canvas_page2c_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_condenser_label_1 = tk.Label(infobox_quantity_condenser_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_label_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_condenser_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2c.register(self.quantity_validate)

        self.entry_quantity_condenser_var_1 = tk.IntVar(page2c)
        self.entry_quantity_condenser_var_1.set('1')
        infobox_quantity_condenser_entry_1 = tk.Entry(infobox_quantity_condenser_frame_1)
        infobox_quantity_condenser_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_condenser_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_condenser_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)






        ### 2
        ### Shell n Tube GUI
        main_frame_page2a_2 = tk.Frame(page2a, bg='gray15')
        main_frame_page2a_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2a_2 = tk.Frame(main_frame_page2a_2, bg='gray15')
        info_canvas_title_frame_page2a_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2a_2 = tk.Label(info_canvas_title_frame_page2a_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2a_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2a_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2a_2 = tk.Canvas(info_canvas_title_frame_page2a_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2a_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_snt_2 = tk.Frame(infobox_canvas_page2a_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_snt_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_snt_2 = tk.Label(infobox_cname_frame_snt_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_snt_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_snt_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2a.register(self.cname_validate)

        self.entry_cname_snt_var_2 = tk.StringVar(page2a)
        self.entry_cname_snt_var_2.set('')
        infobox_cname_snt_entry_2 = tk.Entry(infobox_cname_frame_snt_2)
        infobox_cname_snt_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_snt_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_snt_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_snt_frame_2 = tk.Frame(infobox_canvas_page2a_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_snt_label_2 = tk.Label(infobox_area_snt_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_label_2.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_snt_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2a.register(self.area_validate)

        self.entry_area_snt_var_2 = tk.DoubleVar(page2a)
        self.entry_area_snt_var_2.set('0.0')
        infobox_area_snt_entry_2 = tk.Entry(infobox_area_snt_frame_2)
        infobox_area_snt_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_snt_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_snt_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_snt_frame_2 = tk.Frame(infobox_canvas_page2a_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_snt_label_2 = tk.Label(infobox_quantity_snt_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_label_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_snt_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2a.register(self.quantity_validate)

        self.entry_quantity_snt_var_2 = tk.IntVar(page2a)
        self.entry_quantity_snt_var_2.set('1')
        infobox_quantity_snt_entry_2 = tk.Entry(infobox_quantity_snt_frame_2)
        infobox_quantity_snt_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_snt_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_snt_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)










        
        ### Plate GUI
        main_frame_page2b_2 = tk.Frame(page2b, bg='gray15')
        main_frame_page2b_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2b_2 = tk.Frame(main_frame_page2b_2, bg='gray15')
        info_canvas_title_frame_page2b_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_plate_title_label_page2b_2 = tk.Label(info_canvas_title_frame_page2b_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_plate_title_label_page2b_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_plate_title_label_page2b_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2b_2 = tk.Canvas(info_canvas_title_frame_page2b_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2b_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_plate_frame_2 = tk.Frame(infobox_canvas_page2b_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_plate_label_2 = tk.Label(infobox_cname_plate_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_label_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_plate_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2b.register(self.cname_validate)

        self.entry_cname_plate_var_2 = tk.StringVar(page2b)
        self.entry_cname_plate_var_2.set('')
        infobox_cname_plate_entry_2 = tk.Entry(infobox_cname_plate_frame_2)
        infobox_cname_plate_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_plate_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_plate_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_plate_frame_2 = tk.Frame(infobox_canvas_page2b_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_plate_label_2 = tk.Label(infobox_area_plate_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_label_2.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_plate_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2b.register(self.area_validate)

        self.entry_area_plate_var_2 = tk.DoubleVar(page2b)
        self.entry_area_plate_var_2.set('0.0')
        infobox_area_plate_entry_2 = tk.Entry(infobox_area_plate_frame_2)
        infobox_area_plate_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_plate_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_plate_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_plate_frame_2 = tk.Frame(infobox_canvas_page2b_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_plate_label_2 = tk.Label(infobox_quantity_plate_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_label_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_plate_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2b.register(self.quantity_validate)

        self.entry_quantity_plate_var_2 = tk.IntVar(page2b)
        self.entry_quantity_plate_var_2.set('1')
        infobox_quantity_plate_entry_2 = tk.Entry(infobox_quantity_plate_frame_2)
        infobox_quantity_plate_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_plate_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_plate_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)








        
        ### Condenser
        main_frame_page2c_2 = tk.Frame(page2c, bg='gray15')
        main_frame_page2c_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2c_2 = tk.Frame(main_frame_page2c_2, bg='gray15')
        info_canvas_title_frame_page2c_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2c_2 = tk.Label(info_canvas_title_frame_page2c_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2c_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2c_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2c_2 = tk.Canvas(info_canvas_title_frame_page2c_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2c_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_condenser_frame_2 = tk.Frame(infobox_canvas_page2c_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_condenser_label_2 = tk.Label(infobox_cname_condenser_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_label_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_condenser_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2c.register(self.cname_validate)

        self.entry_cname_condenser_var_2 = tk.StringVar(page2c)
        self.entry_cname_condenser_var_2.set('')
        infobox_cname_condenser_entry_2 = tk.Entry(infobox_cname_condenser_frame_2)
        infobox_cname_condenser_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_condenser_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_condenser_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_condenser_frame_2 = tk.Frame(infobox_canvas_page2c_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_condenser_label_2 = tk.Label(infobox_area_condenser_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_label_2.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_condenser_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2c.register(self.area_validate)

        self.entry_area_condenser_var_2 = tk.DoubleVar(page2c)
        self.entry_area_condenser_var_2.set('0.0')
        infobox_area_condenser_entry_2 = tk.Entry(infobox_area_condenser_frame_2)
        infobox_area_condenser_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_condenser_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_condenser_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_condenser_frame_2 = tk.Frame(infobox_canvas_page2c_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_condenser_label_2 = tk.Label(infobox_quantity_condenser_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_label_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_condenser_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2c.register(self.quantity_validate)

        self.entry_quantity_condenser_var_2 = tk.IntVar(page2c)
        self.entry_quantity_condenser_var_2.set('1')
        infobox_quantity_condenser_entry_2 = tk.Entry(infobox_quantity_condenser_frame_2)
        infobox_quantity_condenser_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_condenser_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_condenser_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)





        ### 3
        ### Shell n Tube GUI
        main_frame_page2a_3 = tk.Frame(page2a, bg='gray15')
        main_frame_page2a_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2a_3 = tk.Frame(main_frame_page2a_3, bg='gray15')
        info_canvas_title_frame_page2a_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2a_3 = tk.Label(info_canvas_title_frame_page2a_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2a_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2a_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2a_3 = tk.Canvas(info_canvas_title_frame_page2a_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2a_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_snt_3 = tk.Frame(infobox_canvas_page2a_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_snt_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_snt_3 = tk.Label(infobox_cname_frame_snt_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_snt_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_snt_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2a.register(self.cname_validate)

        self.entry_cname_snt_var_3 = tk.StringVar(page2a)
        self.entry_cname_snt_var_3.set('')
        infobox_cname_snt_entry_3 = tk.Entry(infobox_cname_frame_snt_3)
        infobox_cname_snt_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_snt_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_snt_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_snt_frame_3 = tk.Frame(infobox_canvas_page2a_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_snt_label_3 = tk.Label(infobox_area_snt_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_label_3.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_snt_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2a.register(self.area_validate)

        self.entry_area_snt_var_3 = tk.DoubleVar(page2a)
        self.entry_area_snt_var_3.set('0.0')
        infobox_area_snt_entry_3 = tk.Entry(infobox_area_snt_frame_3)
        infobox_area_snt_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_snt_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_snt_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_snt_frame_3 = tk.Frame(infobox_canvas_page2a_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_snt_label_3 = tk.Label(infobox_quantity_snt_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_label_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_snt_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2a.register(self.quantity_validate)

        self.entry_quantity_snt_var_3 = tk.IntVar(page2a)
        self.entry_quantity_snt_var_3.set('1')
        infobox_quantity_snt_entry_3 = tk.Entry(infobox_quantity_snt_frame_3)
        infobox_quantity_snt_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_snt_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_snt_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)










        
        ### Plate GUI
        main_frame_page2b_3 = tk.Frame(page2b, bg='gray15')
        main_frame_page2b_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2b_3 = tk.Frame(main_frame_page2b_3, bg='gray15')
        info_canvas_title_frame_page2b_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_plate_title_label_page2b_3 = tk.Label(info_canvas_title_frame_page2b_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_plate_title_label_page2b_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_plate_title_label_page2b_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2b_3 = tk.Canvas(info_canvas_title_frame_page2b_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2b_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_plate_frame_3 = tk.Frame(infobox_canvas_page2b_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_plate_label_3 = tk.Label(infobox_cname_plate_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_label_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_plate_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2b.register(self.cname_validate)

        self.entry_cname_plate_var_3 = tk.StringVar(page2b)
        self.entry_cname_plate_var_3.set('')
        infobox_cname_plate_entry_3 = tk.Entry(infobox_cname_plate_frame_3)
        infobox_cname_plate_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_plate_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_plate_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_plate_frame_3 = tk.Frame(infobox_canvas_page2b_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_plate_label_3 = tk.Label(infobox_area_plate_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_label_3.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_plate_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2b.register(self.area_validate)

        self.entry_area_plate_var_3 = tk.DoubleVar(page2b)
        self.entry_area_plate_var_3.set('0.0')
        infobox_area_plate_entry_3 = tk.Entry(infobox_area_plate_frame_3)
        infobox_area_plate_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_plate_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_plate_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_plate_frame_3 = tk.Frame(infobox_canvas_page2b_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_plate_label_3 = tk.Label(infobox_quantity_plate_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_label_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_plate_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2b.register(self.quantity_validate)

        self.entry_quantity_plate_var_3 = tk.IntVar(page2b)
        self.entry_quantity_plate_var_3.set('1')
        infobox_quantity_plate_entry_3 = tk.Entry(infobox_quantity_plate_frame_3)
        infobox_quantity_plate_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_plate_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_plate_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)








        
        ### Condenser
        main_frame_page2c_3 = tk.Frame(page2c, bg='gray15')
        main_frame_page2c_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2c_3 = tk.Frame(main_frame_page2c_3, bg='gray15')
        info_canvas_title_frame_page2c_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2c_3 = tk.Label(info_canvas_title_frame_page2c_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2c_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2c_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2c_3 = tk.Canvas(info_canvas_title_frame_page2c_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2c_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_condenser_frame_3 = tk.Frame(infobox_canvas_page2c_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_condenser_label_3 = tk.Label(infobox_cname_condenser_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_label_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_condenser_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2c.register(self.cname_validate)

        self.entry_cname_condenser_var_3 = tk.StringVar(page2c)
        self.entry_cname_condenser_var_3.set('')
        infobox_cname_condenser_entry_3 = tk.Entry(infobox_cname_condenser_frame_3)
        infobox_cname_condenser_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_condenser_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_condenser_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_condenser_frame_3 = tk.Frame(infobox_canvas_page2c_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_condenser_label_3 = tk.Label(infobox_area_condenser_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_label_3.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_condenser_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2c.register(self.area_validate)

        self.entry_area_condenser_var_3 = tk.DoubleVar(page2c)
        self.entry_area_condenser_var_3.set('0.0')
        infobox_area_condenser_entry_3 = tk.Entry(infobox_area_condenser_frame_3)
        infobox_area_condenser_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_condenser_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_condenser_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_condenser_frame_3 = tk.Frame(infobox_canvas_page2c_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_condenser_label_3 = tk.Label(infobox_quantity_condenser_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_label_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_condenser_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2c.register(self.quantity_validate)

        self.entry_quantity_condenser_var_3 = tk.IntVar(page2c)
        self.entry_quantity_condenser_var_3.set('1')
        infobox_quantity_condenser_entry_3 = tk.Entry(infobox_quantity_condenser_frame_3)
        infobox_quantity_condenser_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_condenser_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_condenser_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)







        ### 4
        ### Shell n Tube GUI
        main_frame_page2a_4 = tk.Frame(page2a, bg='gray15')
        main_frame_page2a_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2a_4 = tk.Frame(main_frame_page2a_4, bg='gray15')
        info_canvas_title_frame_page2a_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2a_4 = tk.Label(info_canvas_title_frame_page2a_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2a_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2a_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2a_4 = tk.Canvas(info_canvas_title_frame_page2a_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2a_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_snt_4 = tk.Frame(infobox_canvas_page2a_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_snt_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_snt_4 = tk.Label(infobox_cname_frame_snt_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_snt_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_snt_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2a.register(self.cname_validate)

        self.entry_cname_snt_var_4 = tk.StringVar(page2a)
        self.entry_cname_snt_var_4.set('')
        infobox_cname_snt_entry_4 = tk.Entry(infobox_cname_frame_snt_4)
        infobox_cname_snt_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_snt_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_snt_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_snt_frame_4 = tk.Frame(infobox_canvas_page2a_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_snt_label_4 = tk.Label(infobox_area_snt_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_label_4.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_snt_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2a.register(self.area_validate)

        self.entry_area_snt_var_4 = tk.DoubleVar(page2a)
        self.entry_area_snt_var_4.set('0.0')
        infobox_area_snt_entry_4 = tk.Entry(infobox_area_snt_frame_4)
        infobox_area_snt_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_snt_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_snt_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_snt_frame_4 = tk.Frame(infobox_canvas_page2a_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_snt_label_4 = tk.Label(infobox_quantity_snt_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_label_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_snt_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2a.register(self.quantity_validate)

        self.entry_quantity_snt_var_4 = tk.IntVar(page2a)
        self.entry_quantity_snt_var_4.set('1')
        infobox_quantity_snt_entry_4 = tk.Entry(infobox_quantity_snt_frame_4)
        infobox_quantity_snt_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_snt_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_snt_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)










        
        ### Plate GUI
        main_frame_page2b_4 = tk.Frame(page2b, bg='gray15')
        main_frame_page2b_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2b_4 = tk.Frame(main_frame_page2b_4, bg='gray15')
        info_canvas_title_frame_page2b_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_plate_title_label_page2b_4 = tk.Label(info_canvas_title_frame_page2b_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_plate_title_label_page2b_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_plate_title_label_page2b_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2b_4 = tk.Canvas(info_canvas_title_frame_page2b_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2b_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_plate_frame_4 = tk.Frame(infobox_canvas_page2b_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_plate_label_4 = tk.Label(infobox_cname_plate_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_label_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_plate_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2b.register(self.cname_validate)

        self.entry_cname_plate_var_4 = tk.StringVar(page2b)
        self.entry_cname_plate_var_4.set('')
        infobox_cname_plate_entry_4 = tk.Entry(infobox_cname_plate_frame_4)
        infobox_cname_plate_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_plate_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_plate_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_plate_frame_4 = tk.Frame(infobox_canvas_page2b_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_plate_label_4 = tk.Label(infobox_area_plate_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_label_4.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_plate_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2b.register(self.area_validate)

        self.entry_area_plate_var_4 = tk.DoubleVar(page2b)
        self.entry_area_plate_var_4.set('0.0')
        infobox_area_plate_entry_4 = tk.Entry(infobox_area_plate_frame_4)
        infobox_area_plate_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_plate_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_plate_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_plate_frame_4 = tk.Frame(infobox_canvas_page2b_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_plate_label_4 = tk.Label(infobox_quantity_plate_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_label_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_plate_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2b.register(self.quantity_validate)

        self.entry_quantity_plate_var_4 = tk.IntVar(page2b)
        self.entry_quantity_plate_var_4.set('1')
        infobox_quantity_plate_entry_4 = tk.Entry(infobox_quantity_plate_frame_4)
        infobox_quantity_plate_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_plate_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_plate_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)








        
        ### Condenser
        main_frame_page2c_4 = tk.Frame(page2c, bg='gray15')
        main_frame_page2c_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2c_4 = tk.Frame(main_frame_page2c_4, bg='gray15')
        info_canvas_title_frame_page2c_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2c_4 = tk.Label(info_canvas_title_frame_page2c_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2c_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2c_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2c_4 = tk.Canvas(info_canvas_title_frame_page2c_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2c_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_condenser_frame_4 = tk.Frame(infobox_canvas_page2c_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_condenser_label_4 = tk.Label(infobox_cname_condenser_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_label_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_condenser_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2c.register(self.cname_validate)

        self.entry_cname_condenser_var_4 = tk.StringVar(page2c)
        self.entry_cname_condenser_var_4.set('')
        infobox_cname_condenser_entry_4 = tk.Entry(infobox_cname_condenser_frame_4)
        infobox_cname_condenser_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_condenser_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_condenser_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_condenser_frame_4 = tk.Frame(infobox_canvas_page2c_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_condenser_label_4 = tk.Label(infobox_area_condenser_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_label_4.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_condenser_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2c.register(self.area_validate)

        self.entry_area_condenser_var_4 = tk.DoubleVar(page2c)
        self.entry_area_condenser_var_4.set('0.0')
        infobox_area_condenser_entry_4 = tk.Entry(infobox_area_condenser_frame_4)
        infobox_area_condenser_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_condenser_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_condenser_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_condenser_frame_4 = tk.Frame(infobox_canvas_page2c_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_condenser_label_4 = tk.Label(infobox_quantity_condenser_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_label_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_condenser_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2c.register(self.quantity_validate)

        self.entry_quantity_condenser_var_4 = tk.IntVar(page2c)
        self.entry_quantity_condenser_var_4.set('1')
        infobox_quantity_condenser_entry_4 = tk.Entry(infobox_quantity_condenser_frame_4)
        infobox_quantity_condenser_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_condenser_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_condenser_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)











        ### 4
        ### Shell n Tube GUI
        main_frame_page2a_5 = tk.Frame(page2a, bg='gray15')
        main_frame_page2a_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2a_5 = tk.Frame(main_frame_page2a_5, bg='gray15')
        info_canvas_title_frame_page2a_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2a_5 = tk.Label(info_canvas_title_frame_page2a_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2a_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2a_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2a_5 = tk.Canvas(info_canvas_title_frame_page2a_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2a_5.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_snt_5 = tk.Frame(infobox_canvas_page2a_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_snt_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_snt_5 = tk.Label(infobox_cname_frame_snt_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_snt_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_snt_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2a.register(self.cname_validate)

        self.entry_cname_snt_var_5 = tk.StringVar(page2a)
        self.entry_cname_snt_var_5.set('')
        infobox_cname_snt_entry_5 = tk.Entry(infobox_cname_frame_snt_5)
        infobox_cname_snt_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_snt_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_snt_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_snt_frame_5 = tk.Frame(infobox_canvas_page2a_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_snt_label_5 = tk.Label(infobox_area_snt_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_snt_label_5.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_snt_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2a.register(self.area_validate)

        self.entry_area_snt_var_5 = tk.DoubleVar(page2a)
        self.entry_area_snt_var_5.set('0.0')
        infobox_area_snt_entry_5 = tk.Entry(infobox_area_snt_frame_5)
        infobox_area_snt_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_snt_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_snt_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_snt_frame_5 = tk.Frame(infobox_canvas_page2a_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_snt_label_5 = tk.Label(infobox_quantity_snt_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_snt_label_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_snt_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2a.register(self.quantity_validate)

        self.entry_quantity_snt_var_5 = tk.IntVar(page2a)
        self.entry_quantity_snt_var_5.set('1')
        infobox_quantity_snt_entry_5 = tk.Entry(infobox_quantity_snt_frame_5)
        infobox_quantity_snt_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_snt_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_snt_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)










        
        ### Plate GUI
        main_frame_page2b_5 = tk.Frame(page2b, bg='gray15')
        main_frame_page2b_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2b_5 = tk.Frame(main_frame_page2b_5, bg='gray15')
        info_canvas_title_frame_page2b_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_plate_title_label_page2b_5 = tk.Label(info_canvas_title_frame_page2b_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_plate_title_label_page2b_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_plate_title_label_page2b_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2b_5 = tk.Canvas(info_canvas_title_frame_page2b_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2b_5.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_plate_frame_5 = tk.Frame(infobox_canvas_page2b_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_plate_label_5 = tk.Label(infobox_cname_plate_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_plate_label_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_plate_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2b.register(self.cname_validate)

        self.entry_cname_plate_var_5 = tk.StringVar(page2b)
        self.entry_cname_plate_var_5.set('')
        infobox_cname_plate_entry_5 = tk.Entry(infobox_cname_plate_frame_5)
        infobox_cname_plate_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_plate_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_plate_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_plate_frame_5 = tk.Frame(infobox_canvas_page2b_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_plate_label_5 = tk.Label(infobox_area_plate_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_plate_label_5.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_plate_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2b.register(self.area_validate)

        self.entry_area_plate_var_5 = tk.DoubleVar(page2b)
        self.entry_area_plate_var_5.set('0.0')
        infobox_area_plate_entry_5 = tk.Entry(infobox_area_plate_frame_5)
        infobox_area_plate_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_plate_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_plate_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_plate_frame_5 = tk.Frame(infobox_canvas_page2b_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_plate_label_5 = tk.Label(infobox_quantity_plate_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_plate_label_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_plate_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2b.register(self.quantity_validate)

        self.entry_quantity_plate_var_5 = tk.IntVar(page2b)
        self.entry_quantity_plate_var_5.set('1')
        infobox_quantity_plate_entry_5 = tk.Entry(infobox_quantity_plate_frame_5)
        infobox_quantity_plate_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_plate_var_5,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_plate_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)








        
        ### Condenser
        main_frame_page2c_5 = tk.Frame(page2c, bg='gray15')
        main_frame_page2c_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page2c_5 = tk.Frame(main_frame_page2c_5, bg='gray15')
        info_canvas_title_frame_page2c_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page2c_5 = tk.Label(info_canvas_title_frame_page2c_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page2c_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page2c_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page2c_5 = tk.Canvas(info_canvas_title_frame_page2c_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page2c_5.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_condenser_frame_5 = tk.Frame(infobox_canvas_page2c_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_condenser_label_5 = tk.Label(infobox_cname_condenser_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_condenser_label_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_condenser_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = page2c.register(self.cname_validate)

        self.entry_cname_condenser_var_5 = tk.StringVar(page2c)
        self.entry_cname_condenser_var_5.set('')
        infobox_cname_condenser_entry_5 = tk.Entry(infobox_cname_condenser_frame_5)
        infobox_cname_condenser_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_condenser_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_condenser_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_area_condenser_frame_5 = tk.Frame(infobox_canvas_page2c_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_area_condenser_label_5 = tk.Label(infobox_area_condenser_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_area_condenser_label_5.config(bd=0, text='Area (㎡): ', font='System 6', fg='yellow')
        infobox_area_condenser_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        area_reg = page2c.register(self.area_validate)

        self.entry_area_condenser_var_5 = tk.DoubleVar(page2c)
        self.entry_area_condenser_var_5.set('0.0')
        infobox_area_condenser_entry_5 = tk.Entry(infobox_area_condenser_frame_5)
        infobox_area_condenser_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_area_condenser_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(area_reg, "%P"))
        infobox_area_condenser_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_condenser_frame_5 = tk.Frame(infobox_canvas_page2c_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_condenser_label_5 = tk.Label(infobox_quantity_condenser_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_condenser_label_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_condenser_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = page2c.register(self.quantity_validate)

        self.entry_quantity_condenser_var_5 = tk.IntVar(page2c)
        self.entry_quantity_condenser_var_5.set('1')
        infobox_quantity_condenser_entry_5 = tk.Entry(infobox_quantity_condenser_frame_5)
        infobox_quantity_condenser_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_condenser_var_5,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_condenser_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)


        # enter information button +framE
        enter_info_frame_page3 = tk.Frame(self.page3, bg='gray25')
        enter_info_frame_page3.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page3 = tk.Frame(enter_info_frame_page3, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page3.pack(side=tk.BOTTOM)

        enter_info_button_frame_page3 = tk.Label(enter_info_frame_page3, relief=tk.GROOVE, bg='gray15')
        enter_info_button_frame_page3.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_frame_page3.pack(pady=10)

        enter_info_button_page3 = tk.Button(enter_info_frame_page3)
        enter_info_button_page3.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page3.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        ### 1
        ### PUMPS
        main_frame_page3_1 = tk.Frame(self.page3, bg='gray15')
        main_frame_page3_1.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_1 = tk.Frame(main_frame_page3_1, bg='gray15')
        info_canvas_title_frame_page3_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_1 = tk.Label(info_canvas_title_frame_page3_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_1 = tk.Canvas(info_canvas_title_frame_page3_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_page3_1 = tk.Frame(infobox_canvas_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_page3_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_page3_1 = tk.Label(infobox_cname_frame_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_page3_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_page3_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page3.register(self.cname_validate)

        self.entry_cname_pump_var_1 = tk.StringVar(self.page3)
        self.entry_cname_pump_var_1.set('')
        infobox_cname_entry_page3_1 = tk.Entry(infobox_cname_frame_page3_1)
        infobox_cname_entry_page3_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_pump_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_entry_page3_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_frame_page3_1 = tk.Frame(infobox_canvas_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_frame_page3_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_label_page3_1 = tk.Label(infobox_power_frame_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_label_page3_1.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_label_page3_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page3.register(self.power_validate)

        self.entry_power_pump_var_1 = tk.DoubleVar(self.page3)
        self.entry_power_pump_var_1.set('0.0')
        infobox_power_entry_page3_1 = tk.Entry(infobox_power_frame_page3_1)
        infobox_power_entry_page3_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_pump_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_page3_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_frame_page3_1 = tk.Frame(infobox_canvas_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_frame_page3_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_label_page3_1 = tk.Label(infobox_quantity_frame_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_label_page3_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_label_page3_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page3.register(self.quantity_validate)

        self.entry_quantity_pump_var_1 = tk.IntVar(self.page3)
        self.entry_quantity_pump_var_1.set('1')
        infobox_quantity_entry_page3_1 = tk.Entry(infobox_quantity_frame_page3_1)
        infobox_quantity_entry_page3_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_pump_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_entry_page3_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)




        ### 2
        main_frame_page3_2 = tk.Frame(self.page3, bg='gray15')
        main_frame_page3_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_2 = tk.Frame(main_frame_page3_2, bg='gray15')
        info_canvas_title_frame_page3_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_2 = tk.Label(info_canvas_title_frame_page3_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_2 = tk.Canvas(info_canvas_title_frame_page3_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_page3_2 = tk.Frame(infobox_canvas_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_page3_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_page3_2 = tk.Label(infobox_cname_frame_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_page3_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_page3_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page3.register(self.cname_validate)

        self.entry_cname_pump_var_2 = tk.StringVar(self.page3)
        self.entry_cname_pump_var_2.set('')
        infobox_cname_entry_page3_2 = tk.Entry(infobox_cname_frame_page3_2)
        infobox_cname_entry_page3_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_pump_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_entry_page3_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_frame_page3_2 = tk.Frame(infobox_canvas_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_frame_page3_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_label_page3_2 = tk.Label(infobox_power_frame_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_label_page3_2.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_label_page3_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page3.register(self.power_validate)

        self.entry_power_pump_var_2 = tk.DoubleVar(self.page3)
        self.entry_power_pump_var_2.set('0.0')
        infobox_power_entry_page3_2 = tk.Entry(infobox_power_frame_page3_2)
        infobox_power_entry_page3_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_pump_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_page3_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_frame_page3_2 = tk.Frame(infobox_canvas_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_frame_page3_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_label_page3_2 = tk.Label(infobox_quantity_frame_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_label_page3_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_label_page3_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page3.register(self.quantity_validate)

        self.entry_quantity_pump_var_2 = tk.IntVar(self.page3)
        self.entry_quantity_pump_var_2.set('1')
        infobox_quantity_entry_page3_2 = tk.Entry(infobox_quantity_frame_page3_2)
        infobox_quantity_entry_page3_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_pump_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_entry_page3_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)


        ### 3
        main_frame_page3_3 = tk.Frame(self.page3, bg='gray15')
        main_frame_page3_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_3 = tk.Frame(main_frame_page3_3, bg='gray15')
        info_canvas_title_frame_page3_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_3 = tk.Label(info_canvas_title_frame_page3_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_3 = tk.Canvas(info_canvas_title_frame_page3_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_page3_3 = tk.Frame(infobox_canvas_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_page3_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_page3_3 = tk.Label(infobox_cname_frame_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_page3_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_page3_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page3.register(self.cname_validate)

        self.entry_cname_pump_var_3 = tk.StringVar(self.page3)
        self.entry_cname_pump_var_3.set('')
        infobox_cname_entry_page3_3 = tk.Entry(infobox_cname_frame_page3_3)
        infobox_cname_entry_page3_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_pump_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_entry_page3_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_frame_page3_3 = tk.Frame(infobox_canvas_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_frame_page3_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_label_page3_3 = tk.Label(infobox_power_frame_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_label_page3_3.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_label_page3_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page3.register(self.power_validate)

        self.entry_power_pump_var_3 = tk.DoubleVar(self.page3)
        self.entry_power_pump_var_3.set('0.0')
        infobox_power_entry_page3_3 = tk.Entry(infobox_power_frame_page3_3)
        infobox_power_entry_page3_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_pump_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_page3_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_frame_page3_3 = tk.Frame(infobox_canvas_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_frame_page3_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_label_page3_3 = tk.Label(infobox_quantity_frame_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_label_page3_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_label_page3_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page3.register(self.quantity_validate)

        self.entry_quantity_pump_var_3 = tk.IntVar(self.page3)
        self.entry_quantity_pump_var_3.set('1')
        infobox_quantity_entry_page3_3 = tk.Entry(infobox_quantity_frame_page3_3)
        infobox_quantity_entry_page3_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_pump_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_entry_page3_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        ### 4
        main_frame_page3_4 = tk.Frame(self.page3, bg='gray15')
        main_frame_page3_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_4 = tk.Frame(main_frame_page3_4, bg='gray15')
        info_canvas_title_frame_page3_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_4 = tk.Label(info_canvas_title_frame_page3_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_4 = tk.Canvas(info_canvas_title_frame_page3_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_page3_4 = tk.Frame(infobox_canvas_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_page3_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_page3_4 = tk.Label(infobox_cname_frame_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_page3_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_page3_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page3.register(self.cname_validate)

        self.entry_cname_pump_var_4 = tk.StringVar(self.page3)
        self.entry_cname_pump_var_4.set('')
        infobox_cname_entry_page3_4 = tk.Entry(infobox_cname_frame_page3_4)
        infobox_cname_entry_page3_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_pump_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_entry_page3_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_frame_page3_4 = tk.Frame(infobox_canvas_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_frame_page3_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_label_page3_4 = tk.Label(infobox_power_frame_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_label_page3_4.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_label_page3_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page3.register(self.power_validate)

        self.entry_power_pump_var_4 = tk.DoubleVar(self.page3)
        self.entry_power_pump_var_4.set('0.0')
        infobox_power_entry_page3_4 = tk.Entry(infobox_power_frame_page3_4)
        infobox_power_entry_page3_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_pump_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_page3_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_frame_page3_4 = tk.Frame(infobox_canvas_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_frame_page3_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_label_page3_4 = tk.Label(infobox_quantity_frame_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_label_page3_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_label_page3_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page3.register(self.quantity_validate)

        self.entry_quantity_pump_var_4 = tk.IntVar(self.page3)
        self.entry_quantity_pump_var_4.set('1')
        infobox_quantity_entry_page3_4 = tk.Entry(infobox_quantity_frame_page3_4)
        infobox_quantity_entry_page3_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_pump_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_entry_page3_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)






        ### 5
        main_frame_page3_5 = tk.Frame(self.page3, bg='gray15')
        main_frame_page3_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_5 = tk.Frame(main_frame_page3_5, bg='gray15')
        info_canvas_title_frame_page3_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_5 = tk.Label(info_canvas_title_frame_page3_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_5 = tk.Canvas(info_canvas_title_frame_page3_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_5.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_frame_page3_5 = tk.Frame(infobox_canvas_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_frame_page3_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_label_page3_5 = tk.Label(infobox_cname_frame_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_label_page3_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_label_page3_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page3.register(self.cname_validate)

        self.entry_cname_pump_var_5 = tk.StringVar(self.page3)
        self.entry_cname_pump_var_5.set('')
        infobox_cname_entry_page3_5 = tk.Entry(infobox_cname_frame_page3_5)
        infobox_cname_entry_page3_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_pump_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_entry_page3_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Power entry field
        infobox_power_frame_page3_5 = tk.Frame(infobox_canvas_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_frame_page3_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_label_page3_5 = tk.Label(infobox_power_frame_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_label_page3_5.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_label_page3_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page3.register(self.power_validate)

        self.entry_power_pump_var_5 = tk.DoubleVar(self.page3)
        self.entry_power_pump_var_5.set('0.0')
        infobox_power_entry_page3_5 = tk.Entry(infobox_power_frame_page3_5)
        infobox_power_entry_page3_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_pump_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_page3_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_frame_page3_5 = tk.Frame(infobox_canvas_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_frame_page3_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_label_page3_5 = tk.Label(infobox_quantity_frame_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_label_page3_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_label_page3_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page3.register(self.quantity_validate)

        self.entry_quantity_pump_var_5 = tk.IntVar(self.page3)
        self.entry_quantity_pump_var_5.set('1')
        infobox_quantity_entry_page3_5 = tk.Entry(infobox_quantity_frame_page3_5)
        infobox_quantity_entry_page3_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_pump_var_5,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_entry_page3_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        # enter information button +framE
        enter_info_frame_page4 = tk.Frame(self.page4, bg='gray25')
        enter_info_frame_page4.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page4 = tk.Frame(enter_info_frame_page4, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page4.pack(side=tk.BOTTOM)

        enter_info_button_frame_page4 = tk.Label(enter_info_frame_page4, relief=tk.GROOVE, bg='gray15')
        enter_info_button_frame_page4.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_frame_page4.pack(pady=10)

        enter_info_button_page4 = tk.Button(enter_info_frame_page4)
        enter_info_button_page4.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page4.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        ### 1
        ### EXPANDERS GUI
        main_frame_page3_1 = tk.Frame(self.page4, bg='gray15')
        main_frame_page3_1.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_1 = tk.Frame(main_frame_page3_1, bg='gray15')
        info_canvas_title_frame_page3_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_1 = tk.Label(info_canvas_title_frame_page3_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_1 = tk.Canvas(info_canvas_title_frame_page3_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_expander_frame_1 = tk.Frame(infobox_canvas_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_expander_label_1 = tk.Label(infobox_cname_expander_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_label_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_expander_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page4.register(self.cname_validate)

        self.entry_cname_expander_var_1 = tk.StringVar(self.page4)
        self.entry_cname_expander_var_1.set('')
        infobox_cname_expander_entry_1 = tk.Entry(infobox_cname_expander_frame_1)
        infobox_cname_expander_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_expander_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_expander_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_power_expander_frame_1 = tk.Frame(infobox_canvas_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_expander_label_1 = tk.Label(infobox_power_expander_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_label_1.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_expander_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page4.register(self.power_validate)

        self.entry_power_expander_var_1 = tk.DoubleVar(self.page4)
        self.entry_power_expander_var_1.set('0.0')
        infobox_power_entry_1 = tk.Entry(infobox_power_expander_frame_1)
        infobox_power_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_expander_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_expander_frame_1 = tk.Frame(infobox_canvas_page3_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_expander_label_1 = tk.Label(infobox_quantity_expander_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_label_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_expander_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page4.register(self.quantity_validate)

        self.entry_quantity_expander_var_1 = tk.IntVar(self.page4)
        self.entry_quantity_expander_var_1.set('1')
        infobox_quantity_expander_entry_1 = tk.Entry(infobox_quantity_expander_frame_1)
        infobox_quantity_expander_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_expander_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_expander_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        ### 2
        ### EXPANDERS GUI
        main_frame_page3_2 = tk.Frame(self.page4, bg='gray15')
        main_frame_page3_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_2 = tk.Frame(main_frame_page3_2, bg='gray15')
        info_canvas_title_frame_page3_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_2 = tk.Label(info_canvas_title_frame_page3_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_2 = tk.Canvas(info_canvas_title_frame_page3_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_expander_frame_2 = tk.Frame(infobox_canvas_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_expander_label_2 = tk.Label(infobox_cname_expander_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_label_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_expander_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page4.register(self.cname_validate)

        self.entry_cname_expander_var_2 = tk.StringVar(self.page4)
        self.entry_cname_expander_var_2.set('')
        infobox_cname_expander_entry_2 = tk.Entry(infobox_cname_expander_frame_2)
        infobox_cname_expander_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_expander_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_expander_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_power_expander_frame_2 = tk.Frame(infobox_canvas_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_expander_label_2 = tk.Label(infobox_power_expander_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_label_2.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_expander_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page4.register(self.power_validate)

        self.entry_power_expander_var_2 = tk.DoubleVar(self.page4)
        self.entry_power_expander_var_2.set('0.0')
        infobox_power_entry_2 = tk.Entry(infobox_power_expander_frame_2)
        infobox_power_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_expander_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_expander_frame_2 = tk.Frame(infobox_canvas_page3_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_expander_label_2 = tk.Label(infobox_quantity_expander_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_label_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_expander_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page4.register(self.quantity_validate)

        self.entry_quantity_expander_var_2 = tk.IntVar(self.page4)
        self.entry_quantity_expander_var_2.set('1')
        infobox_quantity_expander_entry_2 = tk.Entry(infobox_quantity_expander_frame_2)
        infobox_quantity_expander_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_expander_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_expander_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)




        ### 3
        ### EXPANDERS GUI
        main_frame_page3_3 = tk.Frame(self.page4, bg='gray15')
        main_frame_page3_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_3 = tk.Frame(main_frame_page3_3, bg='gray15')
        info_canvas_title_frame_page3_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_3 = tk.Label(info_canvas_title_frame_page3_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_3 = tk.Canvas(info_canvas_title_frame_page3_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_expander_frame_3 = tk.Frame(infobox_canvas_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_expander_label_3 = tk.Label(infobox_cname_expander_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_label_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_expander_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page4.register(self.cname_validate)

        self.entry_cname_expander_var_3 = tk.StringVar(self.page4)
        self.entry_cname_expander_var_3.set('')
        infobox_cname_expander_entry_3 = tk.Entry(infobox_cname_expander_frame_3)
        infobox_cname_expander_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_expander_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_expander_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_power_expander_frame_3 = tk.Frame(infobox_canvas_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_expander_label_3 = tk.Label(infobox_power_expander_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_label_3.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_expander_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page4.register(self.power_validate)

        self.entry_power_expander_var_3 = tk.DoubleVar(self.page4)
        self.entry_power_expander_var_3.set('0.0')
        infobox_power_entry_3 = tk.Entry(infobox_power_expander_frame_3)
        infobox_power_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_expander_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_expander_frame_3 = tk.Frame(infobox_canvas_page3_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_expander_label_3 = tk.Label(infobox_quantity_expander_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_label_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_expander_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page4.register(self.quantity_validate)

        self.entry_quantity_expander_var_3 = tk.IntVar(self.page4)
        self.entry_quantity_expander_var_3.set('1')
        infobox_quantity_expander_entry_3 = tk.Entry(infobox_quantity_expander_frame_3)
        infobox_quantity_expander_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_expander_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_expander_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        ### 4
        ### EXPANDERS GUI
        main_frame_page3_4 = tk.Frame(self.page4, bg='gray15')
        main_frame_page3_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_4 = tk.Frame(main_frame_page3_4, bg='gray15')
        info_canvas_title_frame_page3_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_4 = tk.Label(info_canvas_title_frame_page3_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_4 = tk.Canvas(info_canvas_title_frame_page3_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_expander_frame_4 = tk.Frame(infobox_canvas_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_expander_label_4 = tk.Label(infobox_cname_expander_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_label_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_expander_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page4.register(self.cname_validate)

        self.entry_cname_expander_var_4 = tk.StringVar(self.page4)
        self.entry_cname_expander_var_4.set('')
        infobox_cname_expander_entry_4 = tk.Entry(infobox_cname_expander_frame_4)
        infobox_cname_expander_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_expander_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_expander_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_power_expander_frame_4 = tk.Frame(infobox_canvas_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_expander_label_4 = tk.Label(infobox_power_expander_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_label_4.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_expander_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page4.register(self.power_validate)

        self.entry_power_expander_var_4 = tk.DoubleVar(self.page4)
        self.entry_power_expander_var_4.set('0.0')
        infobox_power_entry_4 = tk.Entry(infobox_power_expander_frame_4)
        infobox_power_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_expander_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_expander_frame_4 = tk.Frame(infobox_canvas_page3_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_expander_label_4 = tk.Label(infobox_quantity_expander_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_label_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_expander_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page4.register(self.quantity_validate)

        self.entry_quantity_expander_var_4 = tk.IntVar(self.page4)
        self.entry_quantity_expander_var_4.set('1')
        infobox_quantity_expander_frame_4 = tk.Entry(infobox_quantity_expander_frame_4)
        infobox_quantity_expander_frame_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_expander_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_expander_frame_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)


        



        ### 5
        ### EXPANDERS GUI
        main_frame_page3_5 = tk.Frame(self.page4, bg='gray15')
        main_frame_page3_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page3_5 = tk.Frame(main_frame_page3_5, bg='gray15')
        info_canvas_title_frame_page3_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page3_5 = tk.Label(info_canvas_title_frame_page3_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page3_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page3_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page3_5 = tk.Canvas(info_canvas_title_frame_page3_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page3_5.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_expander_frame_5 = tk.Frame(infobox_canvas_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_expander_label_5 = tk.Label(infobox_cname_expander_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_expander_label_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_expander_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page4.register(self.cname_validate)

        self.entry_cname_expander_var_5 = tk.StringVar(self.page4)
        self.entry_cname_expander_var_5.set('')
        infobox_cname_expander_entry_5 = tk.Entry(infobox_cname_expander_frame_5)
        infobox_cname_expander_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_expander_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_expander_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_power_expander_frame_5 = tk.Frame(infobox_canvas_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_power_expander_label_5 = tk.Label(infobox_power_expander_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_power_expander_label_5.config(bd=0, text='Power (kW): ', font='System 6', fg='yellow')
        infobox_power_expander_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        power_reg = self.page4.register(self.power_validate)

        self.entry_power_expander_var_5 = tk.DoubleVar(self.page4)
        self.entry_power_expander_var_5.set('0.0')
        infobox_power_entry_5 = tk.Entry(infobox_power_expander_frame_5)
        infobox_power_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_power_expander_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(power_reg, "%P"))
        infobox_power_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_expander_frame_5 = tk.Frame(infobox_canvas_page3_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_expander_label_5 = tk.Label(infobox_quantity_expander_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_expander_label_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_expander_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page4.register(self.quantity_validate)

        self.entry_quantity_expander_var_5 = tk.IntVar(self.page4)
        self.entry_quantity_expander_var_5.set('1')
        infobox_quantity_expander_frame_5 = tk.Entry(infobox_quantity_expander_frame_5)
        infobox_quantity_expander_frame_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_expander_var_5,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_expander_frame_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)



        # enter information button +framE
        enter_info_frame_page5 = tk.Frame(self.page5, bg='gray25')
        enter_info_frame_page5.pack(side=tk.BOTTOM, anchor=tk.N, expand=True, fill=tk.X)

        ### Making Enter Information Button.
        enter_info_button_frame_page5 = tk.Frame(enter_info_frame_page5, relief=tk.GROOVE, bd=0, bg='gray15')
        enter_info_button_frame_page5.pack(side=tk.BOTTOM)

        enter_info_button_frame_page5 = tk.Label(enter_info_frame_page5, relief=tk.GROOVE, bg='gray15')
        enter_info_button_frame_page5.config(text='Confirm Information:', font='System 6', fg='yellow')
        enter_info_button_frame_page5.pack(pady=10)

        enter_info_button_page5 = tk.Button(enter_info_frame_page5)
        enter_info_button_page5.config(relief=tk.RAISED, bd=5, text='    Enter Information    ',
                                 command=self.info_button_get)
        enter_info_button_page5.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)



        ### 1
        ### STORAGE TANKS GUI
        main_frame_page4_1 = tk.Frame(self.page5, bg='gray15')
        main_frame_page4_1.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page4_1 = tk.Frame(main_frame_page4_1, bg='gray15')
        info_canvas_title_frame_page4_1.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page4_1 = tk.Label(info_canvas_title_frame_page4_1, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page4_1.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page4_1.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page4_1 = tk.Canvas(info_canvas_title_frame_page4_1, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page4_1.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_st_frame_1 = tk.Frame(infobox_canvas_page4_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_st_label_1 = tk.Label(infobox_cname_st_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_label_1.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_st_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page5.register(self.cname_validate)

        self.entry_cname_st_var_1 = tk.StringVar(self.page5)
        self.entry_cname_st_var_1.set('')
        infobox_cname_st_entry_1 = tk.Entry(infobox_cname_st_frame_1)
        infobox_cname_st_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_st_var_1,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_st_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_volume_st_frame_1 = tk.Frame(infobox_canvas_page4_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_volume_st_label_1 = tk.Label(infobox_volume_st_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_label_1.config(bd=0, text='Volume (L): ', font='System 6', fg='yellow')
        infobox_volume_st_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        volume_reg = self.page5.register(self.volume_validate)

        self.entry_volume_st_var_1 = tk.DoubleVar(self.page5)
        self.entry_volume_st_var_1.set('0.0')
        infobox_volume_st_entry_1 = tk.Entry(infobox_volume_st_frame_1)
        infobox_volume_st_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_volume_st_var_1,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(volume_reg, "%P"))
        infobox_volume_st_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_st_frame_1 = tk.Frame(infobox_canvas_page4_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_frame_1.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_st_label_1 = tk.Label(infobox_quantity_st_frame_1, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_label_1.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_st_label_1.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page5.register(self.quantity_validate)

        self.entry_quantity_st_var_1 = tk.IntVar(self.page5)
        self.entry_quantity_st_var_1.set('1')
        infobox_quantity_st_entry_1 = tk.Entry(infobox_quantity_st_frame_1)
        infobox_quantity_st_entry_1.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_st_var_1,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_st_entry_1.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)




        ### 2
        ### STORAGE TANKS GUI
        main_frame_page4_2 = tk.Frame(self.page5, bg='gray15')
        main_frame_page4_2.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page4_2 = tk.Frame(main_frame_page4_2, bg='gray15')
        info_canvas_title_frame_page4_2.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page4_2 = tk.Label(info_canvas_title_frame_page4_2, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page4_2.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page4_2.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page4_2 = tk.Canvas(info_canvas_title_frame_page4_2, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page4_2.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_st_frame_2 = tk.Frame(infobox_canvas_page4_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_st_label_2 = tk.Label(infobox_cname_st_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_label_2.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_st_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page5.register(self.cname_validate)

        self.entry_cname_st_var_2 = tk.StringVar(self.page5)
        self.entry_cname_st_var_2.set('')
        infobox_cname_st_entry_2 = tk.Entry(infobox_cname_st_frame_2)
        infobox_cname_st_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_st_var_2,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_st_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_volume_st_frame_2 = tk.Frame(infobox_canvas_page4_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_volume_st_label_2 = tk.Label(infobox_volume_st_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_label_2.config(bd=0, text='Volume (L): ', font='System 6', fg='yellow')
        infobox_volume_st_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        volume_reg = self.page5.register(self.volume_validate)

        self.entry_volume_st_var_2 = tk.DoubleVar(self.page5)
        self.entry_volume_st_var_2.set('0.0')
        infobox_volume_st_entry_2 = tk.Entry(infobox_volume_st_frame_2)
        infobox_volume_st_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_volume_st_var_2,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(volume_reg, "%P"))
        infobox_volume_st_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_st_frame_2 = tk.Frame(infobox_canvas_page4_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_frame_2.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_st_label_2 = tk.Label(infobox_quantity_st_frame_2, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_label_2.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_st_label_2.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page5.register(self.quantity_validate)

        self.entry_quantity_st_var_2 = tk.IntVar(self.page5)
        self.entry_quantity_st_var_2.set('1')
        infobox_quantity_st_entry_2 = tk.Entry(infobox_quantity_st_frame_2)
        infobox_quantity_st_entry_2.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_st_var_2,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_st_entry_2.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)




        ### 3
        ### STORAGE TANKS GUI
        main_frame_page4_3 = tk.Frame(self.page5, bg='gray15')
        main_frame_page4_3.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page4_3 = tk.Frame(main_frame_page4_3, bg='gray15')
        info_canvas_title_frame_page4_3.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page4_3 = tk.Label(info_canvas_title_frame_page4_3, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page4_3.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page4_3.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page4_3 = tk.Canvas(info_canvas_title_frame_page4_3, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page4_3.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_st_frame_3 = tk.Frame(infobox_canvas_page4_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_st_label_3 = tk.Label(infobox_cname_st_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_label_3.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_st_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page5.register(self.cname_validate)

        self.entry_cname_st_var_3 = tk.StringVar(self.page5)
        self.entry_cname_st_var_3.set('')
        infobox_cname_st_entry_3 = tk.Entry(infobox_cname_st_frame_3)
        infobox_cname_st_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_st_var_3,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_st_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_volume_st_frame_3 = tk.Frame(infobox_canvas_page4_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_volume_st_label_3 = tk.Label(infobox_volume_st_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_label_3.config(bd=0, text='Volume (L): ', font='System 6', fg='yellow')
        infobox_volume_st_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        volume_reg = self.page5.register(self.volume_validate)

        self.entry_volume_st_var_3 = tk.DoubleVar(self.page5)
        self.entry_volume_st_var_3.set('0.0')
        infobox_volume_st_entry_3 = tk.Entry(infobox_volume_st_frame_3)
        infobox_volume_st_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_volume_st_var_3,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(volume_reg, "%P"))
        infobox_volume_st_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_st_frame_3 = tk.Frame(infobox_canvas_page4_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_frame_3.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_st_label_3 = tk.Label(infobox_quantity_st_frame_3, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_label_3.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_st_label_3.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page5.register(self.quantity_validate)

        self.entry_quantity_st_var_3 = tk.IntVar(self.page5)
        self.entry_quantity_st_var_3.set('1')
        infobox_quantity_st_entry_3 = tk.Entry(infobox_quantity_st_frame_3)
        infobox_quantity_st_entry_3.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_st_var_3,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_st_entry_3.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)




        ### 4
        ### STORAGE TANKS GUI
        main_frame_page4_4 = tk.Frame(self.page5, bg='gray15')
        main_frame_page4_4.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page4_4 = tk.Frame(main_frame_page4_4, bg='gray15')
        info_canvas_title_frame_page4_4.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page4_4 = tk.Label(info_canvas_title_frame_page4_4, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page4_4.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page4_4.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page4_4 = tk.Canvas(info_canvas_title_frame_page4_4, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page4_4.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_st_frame_4 = tk.Frame(infobox_canvas_page4_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_st_label_4 = tk.Label(infobox_cname_st_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_label_4.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_st_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page5.register(self.cname_validate)

        self.entry_cname_st_var_4 = tk.StringVar(self.page5)
        self.entry_cname_st_var_4.set('')
        infobox_cname_st_entry_4 = tk.Entry(infobox_cname_st_frame_4)
        infobox_cname_st_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_st_var_4,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_st_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_volume_st_frame_4 = tk.Frame(infobox_canvas_page4_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_volume_st_label_4 = tk.Label(infobox_volume_st_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_label_4.config(bd=0, text='Volume (L): ', font='System 6', fg='yellow')
        infobox_volume_st_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        volume_reg = self.page5.register(self.volume_validate)

        self.entry_volume_st_var_4 = tk.DoubleVar(self.page5)
        self.entry_volume_st_var_4.set('0.0')
        infobox_volume_st_entry_4 = tk.Entry(infobox_volume_st_frame_4)
        infobox_volume_st_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_volume_st_var_4,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(volume_reg, "%P"))
        infobox_volume_st_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_st_frame_4 = tk.Frame(infobox_canvas_page4_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_frame_4.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_st_label_4 = tk.Label(infobox_quantity_st_frame_4, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_label_4.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_st_label_4.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page5.register(self.quantity_validate)

        self.entry_quantity_st_var_4 = tk.IntVar(self.page5)
        self.entry_quantity_st_var_4.set('1')
        infobox_quantity_st_entry_4 = tk.Entry(infobox_quantity_st_frame_4)
        infobox_quantity_st_entry_4.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_st_var_4,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_st_entry_4.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)





        ### 5
        ### STORAGE TANKS GUI
        main_frame_page4_5 = tk.Frame(self.page5, bg='gray15')
        main_frame_page4_5.pack(side=tk.LEFT, anchor=tk.N, padx=35, pady=10)

        info_canvas_title_frame_page4_5 = tk.Frame(main_frame_page4_5, bg='gray15')
        info_canvas_title_frame_page4_5.pack(side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

        info_canvas_title_label_page4_5 = tk.Label(info_canvas_title_frame_page4_5, relief=tk.GROOVE, borderwidth=1,
                                                bg='gray15')
        info_canvas_title_label_page4_5.config(bd=0, text='Component Information', font='System 12', fg='yellow')
        info_canvas_title_label_page4_5.pack(fill=tk.X, anchor=tk.N)

        
        infobox_canvas_page4_5 = tk.Canvas(info_canvas_title_frame_page4_5, width=200, height=200, relief=tk.RIDGE, bd=1,
                                        bg='gray15')
        infobox_canvas_page4_5.pack(side=tk.TOP, anchor=tk.NW, padx=15, pady=15)

        # Component Name entry field
        infobox_cname_st_frame_5 = tk.Frame(infobox_canvas_page4_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_cname_st_label_5 = tk.Label(infobox_cname_st_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_cname_st_label_5.config(bd=0, text='Name: ', font='System 6', fg='yellow')
        infobox_cname_st_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        cname_reg = self.page5.register(self.cname_validate)

        self.entry_cname_st_var_5 = tk.StringVar(self.page5)
        self.entry_cname_st_var_5.set('')
        infobox_cname_st_entry_5 = tk.Entry(infobox_cname_st_frame_5)
        infobox_cname_st_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_cname_st_var_5,
                                        font='System 6', fg='yellow', validate="key", validatecommand=(cname_reg, '%P'))
        infobox_cname_st_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Component Area entry field
        infobox_volume_st_frame_5 = tk.Frame(infobox_canvas_page4_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_volume_st_label_5 = tk.Label(infobox_volume_st_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_volume_st_label_5.config(bd=0, text='Volume (L): ', font='System 6', fg='yellow')
        infobox_volume_st_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        volume_reg = self.page5.register(self.volume_validate)

        self.entry_volume_st_var_5 = tk.DoubleVar(self.page5)
        self.entry_volume_st_var_5.set('0.0')
        infobox_volume_st_entry_5 = tk.Entry(infobox_volume_st_frame_5)
        infobox_volume_st_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15', textvariable=self.entry_volume_st_var_5,
                                          font='System 6', fg='yellow', validate="key",
                                          validatecommand=(volume_reg, "%P"))
        infobox_volume_st_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)

        # Quantity entry field
        infobox_quantity_st_frame_5 = tk.Frame(infobox_canvas_page4_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_frame_5.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

        infobox_quantity_st_label_5 = tk.Label(infobox_quantity_st_frame_5, relief=tk.FLAT, bd=0, bg='gray15')
        infobox_quantity_st_label_5.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
        infobox_quantity_st_label_5.pack(side=tk.LEFT, anchor=tk.W, padx=2, pady=2)

        quantity_reg = self.page5.register(self.quantity_validate)

        self.entry_quantity_st_var_5 = tk.IntVar(self.page5)
        self.entry_quantity_st_var_5.set('1')
        infobox_quantity_st_entry_5 = tk.Entry(infobox_quantity_st_frame_5)
        infobox_quantity_st_entry_5.config(bd=1, relief=tk.GROOVE, bg='gray15',
                                              textvariable=self.entry_quantity_st_var_5,
                                              font='System 6', fg='yellow', validate="key",
                                              validatecommand=(quantity_reg, "%P"))
        infobox_quantity_st_entry_5.pack(side=tk.RIGHT, anchor=tk.E, padx=2, pady=2)




        
        ### RESULTS PAGE
        
        treeview_frame = tk.Frame(self.page6, relief=tk.GROOVE, bd=0, bg='gray15')
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
        

        for i in range(len(self.total_comp_names)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(self.total_comp_types[i], self.total_comp_names[i], self.total_comp_values[i], self.total_comp_quantities[i],
                                             self.total_comp_individual_costs[i], self.total_comp_quantity_cost[i]))
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


        results_frame = tk.Frame(self.page6)
        results_frame.pack(expand=True, fill=tk.X)

        results_label = tk.Label(results_frame, relief=tk.GROOVE, bg='gray15')
        results_label.config(text='Calculate System Total', font='System 6', fg='yellow')
        results_label.pack(pady=10)

        results_button = tk.Button(results_frame)
        results_button.config(relief=tk.RAISED, bd=5, text='    Calculate    ',
                                 command=self.total_cost_calculate)
        results_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=15, padx=15)

        self.results_label = tk.Label(results_frame, bg='gray15')
        self.results_label.config(bd=0, text='Total System Cost: £{}'.format(self.total_system_cost), font='System 6', fg='yellow')
        self.results_label.pack()


        ### HELP PAGE  

    ### Treeview sorting algorithm
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
        
    def info_button_get(self):
        #FETCH ALL VALUES
        ### Turbines
        turbine_type = 'Turbine'
        # Turbines Names
        turbine_name_1 = self.entry_cname_turb_var_1.get()
        turbine_name_2 = self.entry_cname_turb_var_2.get()
        turbine_name_3 = self.entry_cname_turb_var_3.get()
        turbine_name_4 = self.entry_cname_turb_var_4.get()
        turbine_name_5 = self.entry_cname_turb_var_5.get()

        # Turbine Power Values
        try:
            self.turbine_power_1 = self.entry_power_turb_var_1.get()
        except Exception:
            self.entry_power_turb_var_1.set('0.0')
        try:
            self.turbine_power_2 = self.entry_power_turb_var_2.get()
        except Exception:
            self.entry_power_turb_var_2.set('0.0')
        try:
            self.turbine_power_3 = self.entry_power_turb_var_3.get()
        except Exception:
            self.entry_power_turb_var_3.set('0.0')
        try:
            self.turbine_power_4 = self.entry_power_turb_var_4.get()
        except Exception:
            self.entry_power_turb_var_4.set('0.0')
        try:
            self.turbine_power_5 = self.entry_power_turb_var_5.get()
        except Exception:
            self.entry_power_turb_var_5.set('0.0')
            
        if self.turbine_power_1 == '':
            self.turbine_power_1=0
        elif self.turbine_power_2 == '':
            self.turbine_power_2=0
        elif self.turbine_power_3 == '':
            self.turbine_power_3=0
        elif self.turbine_power_4 == '':
            self.turbine_power_4=0
        elif self.turbine_power_5 == '':
            self.turbine_power_5=0

        # Turbine Quantities
        self.turbine_quantity_1 = self.entry_quantity_turb_var_1.get()
        self.turbine_quantity_2 = self.entry_quantity_turb_var_2.get()
        self.turbine_quantity_3 = self.entry_quantity_turb_var_3.get()
        self.turbine_quantity_4 = self.entry_quantity_turb_var_4.get()
        self.turbine_quantity_5 = self.entry_quantity_turb_var_5.get()
        try:
            self.turbine_quantity_1 = self.entry_quantity_turb_var_1.get()
        except Exception:
            self.entry_quantity_turb_var_1.set('1')
        try:
            self.turbine_quantity_2 = self.entry_quantity_turb_var_2.get()
        except Exception:
            self.entry_quantity_turb_var_2.set('1')
        try:
            self.turbine_quantity_3 = self.entry_quantity_turb_var_3.get()
        except Exception:
            self.entry_quantity_turb_var_3.set('1')
        try:
            self.turbine_quantity_4 = self.entry_quantity_turb_var_4.get()
        except Exception:
            self.entry_quantity_turb_var_4.set('1')
        try:
            self.turbine_quantity_5 = self.entry_quantity_turb_var_5.get()
        except Exception:
            self.entry_quantity_turb_var_5.set('1')
        

        # Turbine Costs
        self.turbs_cost_1 = (2984.9 * self.turbine_power_1 ** 0.5171)
        self.turbs_cost_2 = (2984.9 * self.turbine_power_2 ** 0.5171)
        self.turbs_cost_3 = (2984.9 * self.turbine_power_3 ** 0.5171)
        self.turbs_cost_4 = (2984.9 * self.turbine_power_4 ** 0.5171)
        self.turbs_cost_5 = (2984.9 * self.turbine_power_5 ** 0.5171)

        #Turbines Quantity * Individual Cost Totals
        self.turbs_total_1 = (self.turbs_cost_1 * self.turbine_quantity_1)
        self.turbs_total_2 = (self.turbs_cost_2 * self.turbine_quantity_2)
        self.turbs_total_3 = (self.turbs_cost_3 * self.turbine_quantity_3)
        self.turbs_total_4 = (self.turbs_cost_4 * self.turbine_quantity_4)
        self.turbs_total_5 = (self.turbs_cost_5 * self.turbine_quantity_5)
        self.turbs_total = self.turbs_total_1 + self.turbs_total_2 + self.turbs_total_3 + self.turbs_total_3 + self.turbs_total_3 + self.turbs_total_5





        ### Heat Exchangers
        hx_type_snt = 'Heat Exchanger - Shell and Tube'
        hx_type_plate = 'Heat Exchanger - Plate'
        hx_type_acc = 'Heat Exchanger - Air-Cooled Condenser'

        # Heat Exchanger - Shell and Tube Names
        snt_name_1 = self.entry_cname_snt_var_1.get()
        snt_name_2 = self.entry_cname_snt_var_2.get()
        snt_name_3 = self.entry_cname_snt_var_3.get()
        snt_name_4 = self.entry_cname_snt_var_4.get()
        snt_name_5 = self.entry_cname_snt_var_5.get()

        # Heat Exchanger - Plate Names
        plate_name_1 = self.entry_cname_plate_var_1.get()
        plate_name_2 = self.entry_cname_plate_var_2.get()
        plate_name_3 = self.entry_cname_plate_var_3.get()
        plate_name_4 = self.entry_cname_plate_var_4.get()
        plate_name_5 = self.entry_cname_plate_var_5.get()

        # Heat Exchanger - Air-Cooled Condenser Names
        acc_name_1 = self.entry_cname_condenser_var_1.get()
        acc_name_2 = self.entry_cname_condenser_var_2.get()
        acc_name_3 = self.entry_cname_condenser_var_3.get()
        acc_name_4 = self.entry_cname_condenser_var_4.get()
        acc_name_5 = self.entry_cname_condenser_var_5.get()

        # Heat Exchanger - Shell and Tube Area Values
        try:
            self.snt_area_1 = self.entry_area_snt_var_1.get()
        except Exception:
            self.entry_area_snt_var_1.set('0.0')
        try:
            self.snt_area_2 = self.entry_area_snt_var_2.get()
        except Exception:
            self.entry_area_snt_var_2.set('0.0')
        try:
            self.snt_area_3 = self.entry_area_snt_var_3.get()
        except Exception:
            self.entry_area_snt_var_3.set('0.0')
        try:
            self.snt_area_4 = self.entry_area_snt_var_4.get()
        except Exception:
            self.entry_area_snt_var_4.set('0.0')
        try:
            self.snt_area_5 = self.entry_area_snt_var_5.get()
        except Exception:
            self.entry_area_snt_var_5.set('0.0')

        if self.snt_area_1 == '':
            self.snt_area_1=0
        elif self.snt_area_2 == '':
            self.snt_area_2=0
        elif self.snt_area_3 == '':
            self.snt_area_3=0
        elif self.snt_area_4 == '':
            self.snt_area_4=0
        elif self.snt_area_5 == '':
            self.snt_area_5=0

        # Heat Exchanger - Plate Area Values
        try:
            self.plate_area_1 = self.entry_area_plate_var_1.get()
        except Exception:
            self.entry_area_plate_var_1.set('0.0')
        try:
            self.plate_area_2 = self.entry_area_plate_var_2.get()
        except Exception:
            self.entry_area_plate_var_2.set('0.0')
        try:
            self.plate_area_3 = self.entry_area_plate_var_3.get()
        except Exception:
            self.entry_area_plate_var_3.set('0.0')
        try:
            self.plate_area_4 = self.entry_area_plate_var_4.get()
        except Exception:
            self.entry_area_plate_var_4.set('0.0')
        try:
            self.plate_area_5 = self.entry_area_plate_var_5.get()
        except Exception:
            self.entry_area_plate_var_5.set('0.0')

        if self.plate_area_1 == '':
            self.plate_area_1=0
        elif self.plate_area_2 == '':
            self.plate_area_2=0
        elif self.plate_area_3 == '':
            self.plate_area_3=0
        elif self.plate_area_4 == '':
            self.plate_area_4=0
        elif self.plate_area_5 == '':
            self.plate_area_5=0


        # Heat Exchanger - Air-Cooled Condenser Area Values
        try:
            self.acc_area_1 = self.entry_area_condenser_var_1.get()
        except Exception:
            self.entry_area_condenser_var_1.set('0.0')
        try:
            self.acc_area_2 = self.entry_area_condenser_var_2.get()
        except Exception:
            self.entry_area_condenser_var_2.set('0.0')
        try:
            self.acc_area_3 = self.entry_area_condenser_var_3.get()
        except Exception:
            self.entry_area_condenser_var_3.set('0.0')
        try:
            self.acc_area_4 = self.entry_area_condenser_var_4.get()
        except Exception:
            self.entry_area_condenser_var_4.set('0.0')
        try:
            self.acc_area_5 = self.entry_area_condenser_var_5.get()
        except Exception:
            self.entry_area_condenser_var_5.set('0.0')
            
        if self.acc_area_1 == '':
            self.acc_area_1=0
        elif self.acc_area_2 == '':
            self.acc_area_2=0
        elif self.acc_area_3 == '':
            self.acc_area_3=0
        elif self.acc_area_4 == '':
            self.acc_area_4=0
        elif self.acc_area_5 == '':
            self.acc_area_5=0

        
        # Heat Exchanger - Shell and Tube Quantities
        try:
            self.snt_quantity_1 = self.entry_quantity_snt_var_1.get()
        except Exception:
            self.entry_quantity_snt_var_1.set('1')
        try:
            self.snt_quantity_2 = self.entry_quantity_snt_var_2.get()
        except Exception:
            self.entry_quantity_snt_var_2.set('1')
        try:
            self.snt_quantity_3 = self.entry_quantity_snt_var_3.get()
        except Exception:
            self.entry_quantity_snt_var_3.set('1')
        try:
            self.snt_quantity_4 = self.entry_quantity_snt_var_4.get()
        except Exception:
            self.entry_quantity_snt_var_4.set('1')
        try:
            self.snt_quantity_5 = self.entry_quantity_snt_var_5.get()
        except Exception:
            self.entry_quantity_snt_var_5.set('1')
            
            

        # Heat Exchanger - Plate Quantities
        try:
            self.plate_quantity_1 = self.entry_quantity_plate_var_1.get()
        except Exception:
            self.entry_quantity_plate_var_1.set('1')
        try:
            self.plate_quantity_2 = self.entry_quantity_plate_var_2.get()
        except Exception:
            self.entry_quantity_plate_var_2.set('1')
        try:
            self.plate_quantity_3 = self.entry_quantity_plate_var_3.get()
        except Exception:
            self.entry_quantity_plate_var_3.set('1')
        try:
            self.plate_quantity_4 = self.entry_quantity_plate_var_4.get()
        except Exception:
            self.entry_quantity_plate_var_4.set('1')
        try:
            self.plate_quantity_5 = self.entry_quantity_plate_var_5.get()
        except Exception:
            self.entry_quantity_plate_var_5.set('1')

        # Heat Exchanger - Air-Cooled Condenser Quantities
        try:
            self.acc_quantity_1 = self.entry_quantity_condenser_var_1.get()
        except Exception:
            self.entry_quantity_condenser_var_1.set('1')
        try:
            self.acc_quantity_2 = self.entry_quantity_condenser_var_2.get()
        except Exception:
            self.entry_quantity_condenser_var_2.set('1')
        try:
            self.acc_quantity_3 = self.entry_quantity_condenser_var_3.get()
        except Exception:
            self.entry_quantity_condenser_var_3.set('1')
        try:
            self.acc_quantity_4 = self.entry_quantity_condenser_var_4.get()
        except Exception:
            self.entry_quantity_condenser_var_4.set('1')
        try:
            self.acc_quantity_5 = self.entry_quantity_condenser_var_5.get()
        except Exception:
            self.entry_quantity_condenser_var_5.set('1')

        # Heat Exchanger - Shell and Tube Costs
        self.snt_cost_1 = (627.6 * self.snt_area_1 ** 0.9199)
        self.snt_cost_2 = (627.6 * self.snt_area_2 ** 0.9199)
        self.snt_cost_3 = (627.6 * self.snt_area_3 ** 0.9199)
        self.snt_cost_4 = (627.6 * self.snt_area_4 ** 0.9199)
        self.snt_cost_5 = (627.6 * self.snt_area_5 ** 0.9199)

        # Heat Exchanger - Plate Costs
        self.plate_cost_1 = (2667.7 * self.plate_area_1 ** 0.3472)
        self.plate_cost_2 = (2667.7 * self.plate_area_2 ** 0.3472)
        self.plate_cost_3 = (2667.7 * self.plate_area_3 ** 0.3472)
        self.plate_cost_4 = (2667.7 * self.plate_area_4 ** 0.3472)
        self.plate_cost_5 = (2667.7 * self.plate_area_5 ** 0.3472)

        # Heat Exchanger - ACC Costs
        self.acc_cost_1 = (1706.2 * self.acc_area_1 ** 0.4301)
        self.acc_cost_2 = (1706.2 * self.acc_area_2 ** 0.4301)
        self.acc_cost_3 = (1706.2 * self.acc_area_3 ** 0.4301)
        self.acc_cost_4 = (1706.2 * self.acc_area_4 ** 0.4301)
        self.acc_cost_5 = (1706.2 * self.acc_area_5 ** 0.4301)



        #Heat Exchangers - SNT - Individual * Quantity Costs
        self.snt_total_1 = (self.snt_cost_1 * self.snt_quantity_1)
        self.snt_total_2 = (self.snt_cost_2 * self.snt_quantity_2)
        self.snt_total_3 = (self.snt_cost_3 * self.snt_quantity_3)
        self.snt_total_4 = (self.snt_cost_4 * self.snt_quantity_4)
        self.snt_total_5 = (self.snt_cost_5 * self.snt_quantity_5)
        self.snt_total = self.snt_total_1 + self.snt_total_2 + self.snt_total_3 + self.snt_total_4 + self.snt_total_5
        

        #Heat Exchangers - Plate - Individual * Quantity Costs
        self.plate_total_1 = (self.plate_cost_1 * self.plate_quantity_1)
        self.plate_total_2 = (self.plate_cost_2 * self.plate_quantity_2)
        self.plate_total_3 = (self.plate_cost_3 * self.plate_quantity_3)
        self.plate_total_4 = (self.plate_cost_4 * self.plate_quantity_4)
        self.plate_total_5 = (self.plate_cost_5 * self.plate_quantity_5)
        self.plate_total = self.plate_total_1 + self.plate_total_2 + self.plate_total_3 + self.plate_total_4 + self.plate_total_5

        #Heat Exchangers - ACC - Individual * Quantity Costs
        self.acc_total_1 = (self.acc_cost_1 * self.acc_quantity_1)
        self.acc_total_2 = (self.acc_cost_2 * self.acc_quantity_2)
        self.acc_total_3 = (self.acc_cost_3 * self.acc_quantity_3)
        self.acc_total_4 = (self.acc_cost_4 * self.acc_quantity_4)
        self.acc_total_5 = (self.acc_cost_5 * self.acc_quantity_5)
        self.acc_total = self.acc_total_1 + self.acc_total_2 + self.acc_total_3 + self.acc_total_4 + self.acc_total_5





        ### Pumps
        pump_type = 'Pump'
        # Pump Names
        pump_name_1 = self.entry_cname_pump_var_1.get()
        pump_name_2 = self.entry_cname_pump_var_2.get()
        pump_name_3 = self.entry_cname_pump_var_3.get()
        pump_name_4 = self.entry_cname_pump_var_4.get()
        pump_name_5 = self.entry_cname_pump_var_5.get()

        #Pump Power Values
        try:
            self.pump_power_1 = self.entry_power_pump_var_1.get()
        except Exception:
            self.entry_power_pump_var_1.set('0.0')
        try:
            self.pump_power_2 = self.entry_power_pump_var_2.get()
        except Exception:
            self.entry_power_pump_var_2.set('0.0')
        try:
            self.pump_power_3 = self.entry_power_pump_var_3.get()
        except Exception:
            self.entry_power_pump_var_3.set('0.0')
        try:
            self.pump_power_4 = self.entry_power_pump_var_4.get()
        except Exception:
            self.entry_power_pump_var_4.set('0.0')
        try:
            self.pump_power_5 = self.entry_power_pump_var_5.get()
        except Exception:
            self.entry_power_pump_var_5.set('0.0')
            
        
        if self.pump_power_1 == '':
            self.pump_power_1=0
        elif self.pump_power_2 == '':
            self.pump_power_2=0
        elif self.pump_power_3 == '':
            self.pump_power_3=0
        elif self.pump_power_4 == '':
            self.pump_power_4=0
        elif self.pump_power_5 == '':
            self.pump_power_5=0

        #Pump Quantities
        try:
            self.pump_quantity_1 = self.entry_quantity_pump_var_1.get()
        except Exception:
            self.entry_quantity_pump_var_1.set('1')    
        try:
            self.pump_quantity_2 = self.entry_quantity_pump_var_2.get()
        except Exception:
            self.entry_quantity_pump_var_2.set('1')   
        try:
            self.pump_quantity_3 = self.entry_quantity_pump_var_3.get()
        except Exception:
            self.entry_quantity_pump_var_3.set('1')
        try:
            self.pump_quantity_4 = self.entry_quantity_pump_var_4.get()
        except Exception:
            self.entry_quantity_pump_var_4.set('1')
        try:
            self.pump_quantity_5 = self.entry_quantity_pump_var_5.get()
        except Exception:
            self.entry_quantity_pump_var_5.set('1')

        # Pump Costs
        self.pump_cost_1 = (1513.4 * self.pump_power_1 ** 0.1946)
        self.pump_cost_2 = (1513.4 * self.pump_power_2 ** 0.1946)
        self.pump_cost_3 = (1513.4 * self.pump_power_3 ** 0.1946)
        self.pump_cost_4 = (1513.4 * self.pump_power_4 ** 0.1946)
        self.pump_cost_5 = (1513.4 * self.pump_power_5 ** 0.1946)


        #Pump - Individual * Quantity Costs
        self.pump_total_1 = (self.pump_cost_1 * self.pump_quantity_1)
        self.pump_total_2 = (self.pump_cost_2 * self.pump_quantity_2)
        self.pump_total_3 = (self.pump_cost_3 * self.pump_quantity_3)
        self.pump_total_4 = (self.pump_cost_4 * self.pump_quantity_4)
        self.pump_total_5 = (self.pump_cost_5 * self.pump_quantity_5)
        self.pump_total = self.acc_total_1 + self.pump_total_2 + self.pump_total_3 + self.pump_total_4 + self.pump_total_5





        ### Expander
        expander_type = 'Expander'
        # Expander Names
        expander_name_1 = self.entry_cname_expander_var_1.get()
        expander_name_2 = self.entry_cname_expander_var_2.get()
        expander_name_3 = self.entry_cname_expander_var_3.get()
        expander_name_4 = self.entry_cname_expander_var_4.get()
        expander_name_5 = self.entry_cname_expander_var_5.get()
        
        #Expander Power Values
        try:
            self.expander_power_1 = self.entry_power_expander_var_1.get()
        except Exception:
            self.entry_power_expander_var_1.set('0.0')
        try:
            self.expander_power_2 = self.entry_power_expander_var_2.get()
        except Exception:
            self.entry_power_expander_var_2.set('0.0')
        try:
            self.expander_power_3 = self.entry_power_expander_var_3.get()
        except Exception:
            self.entry_power_expander_var_3.set('0.0')
        try:
            self.expander_power_4 = self.entry_power_expander_var_4.get()
        except Exception:
            self.entry_power_expander_var_4.set('0.0')
        try:
            self.expander_power_5 = self.entry_power_expander_var_5.get()
        except Exception:
            self.entry_power_expander_var_5.set('0.0')
            
        if self.expander_power_1 == '':
            self.expander_power_1=0
        elif self.expander_power_2 == '':
            self.expander_power_2=0
        elif self.expander_power_3 == '':
            self.expander_power_3=0
        elif self.expander_power_4 == '':
            self.expander_power_4=0
        elif self.expander_power_5 == '':
            self.expander_power_5=0
        
        #Expander Quantities
        try:
            self.expander_quantity_1 = self.entry_quantity_expander_var_1.get()
        except Exception:
            self.entry_quantity_expander_var_1.set('1')
        try:
            self.expander_quantity_2 = self.entry_quantity_expander_var_2.get()
        except Exception:
            self.entry_quantity_expander_var_2.set('1')
        try:
            self.expander_quantity_3 = self.entry_quantity_expander_var_3.get()
        except Exception:
            self.entry_quantity_expander_var_3.set('1')
        try:
            self.expander_quantity_4 = self.entry_quantity_expander_var_4.get()
        except Exception:
            self.entry_quantity_expander_var_4.set('1')
        try:
            self.expander_quantity_5 = self.entry_quantity_expander_var_5.get()
        except Exception:
            self.entry_quantity_expander_var_5.set('1')
        # Expander Costs
        self.expander_cost_1 = (544 * self.expander_power_1 ** 0.8331)
        self.expander_cost_2 = (544 * self.expander_power_2 ** 0.8331)
        self.expander_cost_3 = (544 * self.expander_power_3 ** 0.8331)
        self.expander_cost_4 = (544 * self.expander_power_4 ** 0.8331)
        self.expander_cost_5 = (544 * self.expander_power_5 ** 0.8331)


        #Expander Individual * Quantities Costs
        self.expander_total_1 = (self.expander_cost_1 * self.expander_quantity_1)
        self.expander_total_2 = (self.expander_cost_2 * self.expander_quantity_2)
        self.expander_total_3 = (self.expander_cost_3 * self.expander_quantity_3)
        self.expander_total_4 = (self.expander_cost_4 * self.expander_quantity_4)
        self.expander_total_5 = (self.expander_cost_5 * self.expander_quantity_5)
        self.expander_total = self.expander_total_1 + self.expander_total_2 + self.expander_total_3 + self.expander_total_4 + self.expander_total_5


        ### Storage Tank
        st_type = 'Storage Tank'
        # Storage Tank Names
        st_name_1 = self.entry_cname_st_var_1.get()
        st_name_2 = self.entry_cname_st_var_2.get()
        st_name_3 = self.entry_cname_st_var_3.get()
        st_name_4 = self.entry_cname_st_var_4.get()
        st_name_5 = self.entry_cname_st_var_5.get()
        
        #Storage Tank Volume Values
        try:
            self.st_volume_1 = self.entry_volume_st_var_1.get()
        except Exception:
            self.entry_volume_st_var_1.set('0.0')
        try:
            self.st_volume_2 = self.entry_volume_st_var_2.get()
        except Exception:
            self.entry_volume_st_var_2.set('0.0')
        try:
            self.st_volume_3 = self.entry_volume_st_var_3.get()
        except Exception:
            self.entry_volume_st_var_3.set('0.0')
        try:
            self.st_volume_4 = self.entry_volume_st_var_4.get()
        except Exception:
            self.entry_volume_st_var_4.set('0.0')
        try:
            self.st_volume_5 = self.entry_volume_st_var_5.get()
        except Exception:
            self.entry_volume_st_var_5.set('0.0')
            
        if self.st_volume_1 == '':
            self.st_volume_1=0
        elif self.st_volume_2 == '':
            self.st_volume_2=0
        elif self.st_volume_3 == '':
            self.st_volume_3=0
        elif self.st_volume_4 == '':
            self.st_volume_4=0
        elif self.st_volume_5 == '':
            self.st_volume_5=0
            
        #Storage Tank Quantities
        try:
            self.st_quantity_1 = self.entry_quantity_st_var_1.get()
        except Exception:
            self.entry_quantity_st_var_1.set('1')
        try:
            self.st_quantity_2 = self.entry_quantity_st_var_2.get()
        except Exception:
            self.entry_quantity_st_var_2.set('1')
        try:
            self.st_quantity_3 = self.entry_quantity_st_var_3.get()
        except Exception:
            self.entry_quantity_st_var_3.set('1')
        try:
            self.st_quantity_4 = self.entry_quantity_st_var_4.get()
        except Exception:
            self.entry_quantity_st_var_4.set('1')
        try:
            self.st_quantity_5 = self.entry_quantity_st_var_5.get()
        except Exception:
            self.entry_quantity_st_var_5.set('1')


        # Storage Tank Costs
        self.st_cost_1 = (52.6 * self.st_volume_1 ** 0.5531)
        self.st_cost_2 = (52.6 * self.st_volume_2 ** 0.5531)
        self.st_cost_3 = (52.6 * self.st_volume_3 ** 0.5531)
        self.st_cost_4 = (52.6 * self.st_volume_4 ** 0.5531)
        self.st_cost_5 = (52.6 * self.st_volume_5 ** 0.5531)


        #Storage Tank Individual * Quantities Costs
        self.st_total_1 = (self.st_cost_1 * self.st_quantity_1)
        self.st_total_2 = (self.st_cost_2 * self.st_quantity_2)
        self.st_total_3 = (self.st_cost_3 * self.st_quantity_3)
        self.st_total_4 = (self.st_cost_4 * self.st_quantity_4)
        self.st_total_5 = (self.st_cost_5 * self.st_quantity_5)
        self.st_total = self.st_total_1 + self.st_total_2 + self.st_total_3 + self.st_total_4 + self.st_total_5




        if turbine_name_1 != '':
            self.total_comp_types[0]=turbine_type
            self.total_comp_names[0]=turbine_name_1
            self.total_comp_values[0]=self.turbine_power_1
            self.total_comp_quantities[0]=self.turbine_quantity_1
            self.total_comp_individual_costs[0]=self.turbs_cost_1
            self.total_comp_quantity_cost[0]=self.turbs_total_1
        elif turbine_name_1 == '':
            self.total_comp_types[0]=''
            self.total_comp_names[0]=''
            self.total_comp_values[0]=''
            self.total_comp_quantities[0]=''
            self.total_comp_individual_costs[0]=''
            self.total_comp_quantity_cost[0]=''
        
        if turbine_name_2 != '':
            self.total_comp_types[1]=turbine_type
            self.total_comp_names[1]=turbine_name_2
            self.total_comp_values[1]=self.turbine_power_2
            self.total_comp_quantities[1]=self.turbine_quantity_2
            self.total_comp_individual_costs[1]=self.turbs_cost_2
            self.total_comp_quantity_cost[1]=self.turbs_total_2
        else:
            self.total_comp_types[1]=''
            self.total_comp_names[1]=''
            self.total_comp_values[1]=''
            self.total_comp_quantities[1]=''
            self.total_comp_individual_costs[1]=''
            self.total_comp_quantity_cost[1]=''
            
        if turbine_name_3 != '':
            self.total_comp_types[2]=turbine_type
            self.total_comp_names[2]=turbine_name_3
            self.total_comp_values[2]=self.turbine_power_3
            self.total_comp_quantities[2]=self.turbine_quantity_3
            self.total_comp_individual_costs[2]=self.turbs_cost_3
            self.total_comp_quantity_cost[2]=self.turbs_total_3
        else:
            self.total_comp_types[2]=''
            self.total_comp_names[2]=''
            self.total_comp_values[2]=''
            self.total_comp_quantities[2]=''
            self.total_comp_individual_costs[2]=''
            self.total_comp_quantity_cost[2]=''
            
        if turbine_name_4 != '':
            self.total_comp_types[3]=turbine_type
            self.total_comp_names[3]=turbine_name_4
            self.total_comp_values[3]=self.turbine_power_4
            self.total_comp_quantities[3]=self.turbine_quantity_4
            self.total_comp_individual_costs[3]=self.turbs_cost_4
            self.total_comp_quantity_cost[3]=self.turbs_total_4
        else:
            self.total_comp_types[3]=''
            self.total_comp_names[3]=''
            self.total_comp_values[3]=''
            self.total_comp_quantities[3]=''
            self.total_comp_individual_costs[3]=''
            self.total_comp_quantity_cost[3]=''
            
        if turbine_name_5 != '':
            self.total_comp_types[4]=turbine_type
            self.total_comp_names[4]=turbine_name_5
            self.total_comp_values[4]=self.turbine_power_5
            self.total_comp_quantities[4]=self.turbine_quantity_5
            self.total_comp_individual_costs[4]=self.turbs_cost_5
            self.total_comp_quantity_cost[4]=self.turbs_total_5
        else:
            self.total_comp_types[4]=''
            self.total_comp_names[4]=''
            self.total_comp_values[4]=''
            self.total_comp_quantities[4]=''
            self.total_comp_individual_costs[4]=''
            self.total_comp_quantity_cost[4]=''
            
        if snt_name_1 != '':
            self.total_comp_types[5]=hx_type_snt
            self.total_comp_names[5]=snt_name_1
            self.total_comp_values[5]=self.snt_area_1
            self.total_comp_quantities[5]=self.snt_quantity_1
            self.total_comp_individual_costs[5]=self.snt_cost_1
            self.total_comp_quantity_cost[5]=self.snt_total_1
        else:
            self.total_comp_types[5]=''
            self.total_comp_names[5]=''
            self.total_comp_values[5]=''
            self.total_comp_quantities[5]=''
            self.total_comp_individual_costs[5]=''
            self.total_comp_quantity_cost[5]=''
            
        if snt_name_2 != '':
            self.total_comp_types[6]=hx_type_snt
            self.total_comp_names[6]=snt_name_2
            self.total_comp_values[6]=self.snt_area_2
            self.total_comp_quantities[6]=self.snt_quantity_2
            self.total_comp_individual_costs[6]=self.snt_cost_2
            self.total_comp_quantity_cost[6]=self.snt_total_2
        else:
            self.total_comp_types[6]=''
            self.total_comp_names[6]=''
            self.total_comp_values[6]=''
            self.total_comp_quantities[6]=''
            self.total_comp_individual_costs[6]=''
            self.total_comp_quantity_cost[6]=''
            
        if snt_name_3 != '':
            self.total_comp_types[7]=hx_type_snt
            self.total_comp_names[7]=snt_name_3
            self.total_comp_values[7]=self.snt_area_3
            self.total_comp_quantities[7]=self.snt_quantity_3
            self.total_comp_individual_costs[7]=self.snt_cost_3
            self.total_comp_quantity_cost[7]=self.snt_total_3
        else:
            self.total_comp_types[7]=''
            self.total_comp_names[7]=''
            self.total_comp_values[7]=''
            self.total_comp_quantities[7]=''
            self.total_comp_individual_costs[7]=''
            self.total_comp_quantity_cost[7]=''
            
        if snt_name_4 != '':
            self.total_comp_types[8]=hx_type_snt
            self.total_comp_names[8]=snt_name_4
            self.total_comp_values[8]=self.snt_area_4
            self.total_comp_quantities[8]=self.snt_quantity_4
            self.total_comp_individual_costs[8]=self.snt_cost_4
            self.total_comp_quantity_cost[8]=self.snt_total_4
        else:
            self.total_comp_types[8]=''
            self.total_comp_names[8]=''
            self.total_comp_values[8]=''
            self.total_comp_quantities[8]=''
            self.total_comp_individual_costs[8]=''
            self.total_comp_quantity_cost[8]=''

        if snt_name_5 != '':
            self.total_comp_types[9]=hx_type_snt
            self.total_comp_names[9]=snt_name_5
            self.total_comp_values[9]=self.snt_area_5
            self.total_comp_quantities[9]=self.snt_quantity_5
            self.total_comp_individual_costs[9]=self.snt_cost_5
            self.total_comp_quantity_cost[9]=self.snt_total_5
        else:
            self.total_comp_types[9]=''
            self.total_comp_names[9]=''
            self.total_comp_values[9]=''
            self.total_comp_quantities[9]=''
            self.total_comp_individual_costs[9]=''
            self.total_comp_quantity_cost[9]=''
        
            
        if plate_name_1 != '':
            self.total_comp_types[10]=hx_type_plate
            self.total_comp_names[10]=plate_name_1
            self.total_comp_values[10]=self.plate_area_1
            self.total_comp_quantities[10]=self.plate_quantity_1
            self.total_comp_individual_costs[10]=self.plate_cost_1
            self.total_comp_quantity_cost[10]=self.plate_total_1
        else:
            self.total_comp_types[10]=''
            self.total_comp_names[10]=''
            self.total_comp_values[10]=''
            self.total_comp_quantities[10]=''
            self.total_comp_individual_costs[10]=''
            self.total_comp_quantity_cost[10]=''
            
        if plate_name_2 != '':
            self.total_comp_types[11]=hx_type_plate
            self.total_comp_names[11]=plate_name_2
            self.total_comp_values[11]=self.plate_area_2
            self.total_comp_quantities[11]=self.plate_quantity_2
            self.total_comp_individual_costs[11]=self.plate_cost_2
            self.total_comp_quantity_cost[11]=self.plate_total_2
        else:
            self.total_comp_types[11]=''
            self.total_comp_names[11]=''
            self.total_comp_values[11]=''
            self.total_comp_quantities[11]=''
            self.total_comp_individual_costs[11]=''
            self.total_comp_quantity_cost[11]=''
        if plate_name_3 != '':
            self.total_comp_types[12]=hx_type_plate
            self.total_comp_names[12]=plate_name_3
            self.total_comp_values[12]=self.plate_area_3
            self.total_comp_quantities[12]=self.plate_quantity_3
            self.total_comp_individual_costs[12]=self.plate_cost_3
            self.total_comp_quantity_cost[12]=self.plate_total_3
        else:
            self.total_comp_types[12]=''
            self.total_comp_names[12]=''
            self.total_comp_values[12]=''
            self.total_comp_quantities[12]=''
            self.total_comp_individual_costs[12]=''
            self.total_comp_quantity_cost[12]=''
        if plate_name_4 != '':
            self.total_comp_types[13]=hx_type_plate
            self.total_comp_names[13]=plate_name_4
            self.total_comp_values[13]=self.plate_area_4
            self.total_comp_quantities[13]=self.plate_quantity_4
            self.total_comp_individual_costs[13]=self.plate_cost_4
            self.total_comp_quantity_cost[13]=self.plate_total_4
        else:
            self.total_comp_types[13]=''
            self.total_comp_names[13]=''
            self.total_comp_values[13]=''
            self.total_comp_quantities[13]=''
            self.total_comp_individual_costs[13]=''
            self.total_comp_quantity_cost[13]=''
        if plate_name_5 != '':
            self.total_comp_types[14]=hx_type_plate
            self.total_comp_names[14]=plate_name_5
            self.total_comp_values[14]=self.plate_area_5
            self.total_comp_quantities[14]=self.plate_quantity_5
            self.total_comp_individual_costs[14]=self.plate_cost_5
            self.total_comp_quantity_cost[14]=self.plate_total_5
        else:
            self.total_comp_types[14]=''
            self.total_comp_names[14]=''
            self.total_comp_values[14]=''
            self.total_comp_quantities[14]=''
            self.total_comp_individual_costs[14]=''
            self.total_comp_quantity_cost[14]=''
                            
            
        if acc_name_1 != '':
            self.total_comp_types[15]=hx_type_acc
            self.total_comp_names[15]=acc_name_1
            self.total_comp_values[15]=self.acc_area_1
            self.total_comp_quantities[15]=self.acc_quantity_1
            self.total_comp_individual_costs[15]=self.acc_cost_1
            self.total_comp_quantity_cost[15]=self.acc_total_1
        else:
            self.total_comp_types[15]=''
            self.total_comp_names[15]=''
            self.total_comp_values[15]=''
            self.total_comp_quantities[15]=''
            self.total_comp_individual_costs[15]=''
            self.total_comp_quantity_cost[15]=''
            
        if acc_name_2 != '':
            self.total_comp_types[16]=hx_type_acc
            self.total_comp_names[16]=acc_name_2
            self.total_comp_values[16]=self.acc_area_2
            self.total_comp_quantities[16]=self.acc_quantity_2
            self.total_comp_individual_costs[16]=self.acc_cost_2
            self.total_comp_quantity_cost[16]=self.acc_total_2
        else:
            self.total_comp_types[16]=''
            self.total_comp_names[16]=''
            self.total_comp_values[16]=''
            self.total_comp_quantities[16]=''
            self.total_comp_individual_costs[16]=''
            self.total_comp_quantity_cost[16]=''
        if acc_name_3 != '':
            self.total_comp_types[17]=hx_type_acc
            self.total_comp_names[17]=acc_name_3
            self.total_comp_values[17]=self.acc_area_3
            self.total_comp_quantities[17]=self.acc_quantity_3
            self.total_comp_individual_costs[17]=self.acc_cost_3
            self.total_comp_quantity_cost[17]=self.acc_total_3
        else:
            self.total_comp_types[17]=''
            self.total_comp_names[17]=''
            self.total_comp_values[17]=''
            self.total_comp_quantities[17]=''
            self.total_comp_individual_costs[17]=''
            self.total_comp_quantity_cost[17]=''
        if acc_name_4 != '':
            self.total_comp_types[18]=hx_type_acc
            self.total_comp_names[18]=acc_name_4
            self.total_comp_values[18]=self.acc_area_4
            self.total_comp_quantities[18]=self.acc_quantity_4
            self.total_comp_individual_costs[18]=self.acc_cost_4
            self.total_comp_quantity_cost[18]=self.acc_total_4
        else:
            self.total_comp_types[18]=''
            self.total_comp_names[18]=''
            self.total_comp_values[18]=''
            self.total_comp_quantities[18]=''
            self.total_comp_individual_costs[18]=''
            self.total_comp_quantity_cost[18]=''
        if acc_name_5 != '':
            self.total_comp_types[19]=hx_type_acc
            self.total_comp_names[19]=acc_name_5
            self.total_comp_values[19]=acc_area_5
            self.total_comp_quantities[19]=self.acc_quantity_5
            self.total_comp_individual_costs[19]=self.acc_cost_5
            self.total_comp_quantity_cost[19]=self.acc_total_5
        else:
            self.total_comp_types[19]=''
            self.total_comp_names[19]=''
            self.total_comp_values[19]=''
            self.total_comp_quantities[19]=''
            self.total_comp_individual_costs[19]=''
            self.total_comp_quantity_cost[19]=''


            
        if pump_name_1 != '':
            self.total_comp_types[20]=pump_type
            self.total_comp_names[20]=pump_name_1
            self.total_comp_values[20]=self.pump_power_1
            self.total_comp_quantities[20]=self.pump_quantity_1
            self.total_comp_individual_costs[20]=self.pump_cost_1
            self.total_comp_quantity_cost[20]=self.pump_total_1
        else:
            self.total_comp_types[20]=''
            self.total_comp_names[20]=''
            self.total_comp_values[20]=''
            self.total_comp_quantities[20]=''
            self.total_comp_individual_costs[20]=''
            self.total_comp_quantity_cost[20]=''
            
        if pump_name_2 != '':
            self.total_comp_types[21]=pump_type
            self.total_comp_names[21]=pump_name_2
            self.total_comp_values[21]=self.pump_power_2
            self.total_comp_quantities[21]=self.pump_quantity_2
            self.total_comp_individual_costs[21]=self.pump_cost_2
            self.total_comp_quantity_cost[21]=self.pump_total_2
        else:
            self.total_comp_types[21]=''
            self.total_comp_names[21]=''
            self.total_comp_values[21]=''
            self.total_comp_quantities[21]=''
            self.total_comp_individual_costs[21]=''
            self.total_comp_quantity_cost[21]=''
        if pump_name_3 != '':
            self.total_comp_types[22]=pump_type
            self.total_comp_names[22]=pump_name_3
            self.total_comp_values[22]=self.pump_power_3
            self.total_comp_quantities[22]=self.pump_quantity_3
            self.total_comp_individual_costs[22]=self.pump_cost_3
            self.total_comp_quantity_cost[22]=self.pump_total_3
        else:
            self.total_comp_types[22]=''
            self.total_comp_names[22]=''
            self.total_comp_values[22]=''
            self.total_comp_quantities[22]=''
            self.total_comp_individual_costs[22]=''
            self.total_comp_quantity_cost[22]=''
        if pump_name_4 != '':
            self.total_comp_types[23]=pump_type
            self.total_comp_names[23]=pump_name_4
            self.total_comp_values[23]=self.pump_power_4
            self.total_comp_quantities[23]=self.pump_quantity_4
            self.total_comp_individual_costs[23]=self.pump_cost_4
            self.total_comp_quantity_cost[23]=self.pump_total_4
        else:
            self.total_comp_types[23]=''
            self.total_comp_names[23]=''
            self.total_comp_values[23]=''
            self.total_comp_quantities[23]=''
            self.total_comp_individual_costs[23]=''
            self.total_comp_quantity_cost[23]=''
        if pump_name_5 != '':
            self.total_comp_types[24]=pump_type
            self.total_comp_names[24]=pump_name_5
            self.total_comp_values[24]=self.pump_power_5
            self.total_comp_quantities[24]=self.pump_quantity_5
            self.total_comp_individual_costs[24]=self.pump_cost_5
            self.total_comp_quantity_cost[24]=self.pump_total_5
        else:
            self.total_comp_types[24]=''
            self.total_comp_names[24]=''
            self.total_comp_values[24]=''
            self.total_comp_quantities[24]=''
            self.total_comp_individual_costs[24]=''
            self.total_comp_quantity_cost[24]=''

            
        if expander_name_1 != '':
            self.total_comp_types[25]=expander_type
            self.total_comp_names[25]=expander_name_1
            self.total_comp_values[25]=self.expander_power_1
            self.total_comp_quantities[25]=self.expander_quantity_1
            self.total_comp_individual_costs[25]=self.expander_cost_1
            self.total_comp_quantity_cost[25]=self.expander_total_1
        else:
            self.total_comp_types[25]=''
            self.total_comp_names[25]=''
            self.total_comp_values[25]=''
            self.total_comp_quantities[25]=''
            self.total_comp_individual_costs[25]=''
            self.total_comp_quantity_cost[25]=''
            
        if expander_name_2 != '':
            self.total_comp_types[26]=expander_type
            self.total_comp_names[26]=expander_name_2
            self.total_comp_values[26]=self.expander_power_2
            self.total_comp_quantities[26]=self.expander_quantity_2
            self.total_comp_individual_costs[26]=self.expander_cost_2
            self.total_comp_quantity_cost[26]=self.expander_total_2
        else:
            self.total_comp_types[26]=''
            self.total_comp_names[26]=''
            self.total_comp_values[26]=''
            self.total_comp_quantities[26]=''
            self.total_comp_individual_costs[26]=''
            self.total_comp_quantity_cost[26]=''
        if expander_name_3 != '':
            self.total_comp_types[27]=expander_type
            self.total_comp_names[27]=expander_name_3
            self.total_comp_values[27]=self.expander_power_3
            self.total_comp_quantities[27]=self.expander_quantity_3
            self.total_comp_individual_costs[27]=self.expander_cost_3
            self.total_comp_quantity_cost[27]=self.expander_total_3
        else:
            self.total_comp_types[27]=''
            self.total_comp_names[27]=''
            self.total_comp_values[27]=''
            self.total_comp_quantities[27]=''
            self.total_comp_individual_costs[27]=''
            self.total_comp_quantity_cost[27]=''
        if expander_name_4 != '':
            self.total_comp_types[28]=expander_type
            self.total_comp_names[28]=expander_name_4
            self.total_comp_values[28]=self.expander_power_4
            self.total_comp_quantities[28]=self.expander_quantity_4
            self.total_comp_individual_costs[28]=self.expander_cost_4
            self.total_comp_quantity_cost[28]=self.expander_total_4
        else:
            self.total_comp_types[28]=''
            self.total_comp_names[28]=''
            self.total_comp_values[28]=''
            self.total_comp_quantities[28]=''
            self.total_comp_individual_costs[28]=''
            self.total_comp_quantity_cost[28]=''
        if expander_name_5 != '':
            self.total_comp_types[29]=expander_type
            self.total_comp_names[29]=expander_name_5
            self.total_comp_values[29]=self.expander_power_5
            self.total_comp_quantities[29]=self.expander_quantity_5
            self.total_comp_individual_costs[29]=self.expander_cost_5
            self.total_comp_quantity_cost[29]=self.expander_total_5
        else:
            self.total_comp_types[29]=''
            self.total_comp_names[29]=''
            self.total_comp_values[29]=''
            self.total_comp_quantities[29]=''
            self.total_comp_individual_costs[29]=''
            self.total_comp_quantity_cost[29]=''
                            
        if expander_name_1 == '':
            self.total_comp_types[25]=''
            self.total_comp_names[25]=''
            self.total_comp_values[25]=''
            self.total_comp_quantities[25]=''
            self.total_comp_individual_costs[25]=''
            self.total_comp_quantity_cost[25]=''
        else:
            self.total_comp_types[30]=''
            self.total_comp_names[30]=''
            self.total_comp_values[30]=''
            self.total_comp_quantities[30]=''
            self.total_comp_individual_costs[30]=''
            self.total_comp_quantity_cost[30]=''
            
        if st_name_1 != '':
            self.total_comp_types[30]=st_type
            self.total_comp_names[30]=st_name_1
            self.total_comp_values[30]=self.st_volume_1
            self.total_comp_quantities[30]=self.st_quantity_1
            self.total_comp_individual_costs[30]=self.st_cost_1
            self.total_comp_quantity_cost[30]=self.st_total_1
        else:
            self.total_comp_types[30]=''
            self.total_comp_names[30]=''
            self.total_comp_values[30]=''
            self.total_comp_quantities[30]=''
            self.total_comp_individual_costs[30]=''
            self.total_comp_quantity_cost[30]=''
        if st_name_2 != '':
            self.total_comp_types[31]=st_type
            self.total_comp_names[31]=st_name_2
            self.total_comp_values[31]=self.st_volume_2
            self.total_comp_quantities[31]=self.st_quantity_2
            self.total_comp_individual_costs[31]=self.st_cost_2
            self.total_comp_quantity_cost[31]=self.st_total_2
        else:
            self.total_comp_types[31]=''
            self.total_comp_names[31]=''
            self.total_comp_values[31]=''
            self.total_comp_quantities[31]=''
            self.total_comp_individual_costs[31]=''
            self.total_comp_quantity_cost[31]=''
        if st_name_3 != '':
            self.total_comp_types[32]=st_type
            self.total_comp_names[32]=st_name_3
            self.total_comp_values[32]=self.st_volume_3
            self.total_comp_quantities[32]=self.st_quantity_3
            self.total_comp_individual_costs[32]=self.st_cost_3
            self.total_comp_quantity_cost[32]=self.st_total_3
        else:
            self.total_comp_types[32]=''
            self.total_comp_names[32]=''
            self.total_comp_values[32]=''
            self.total_comp_quantities[32]=''
            self.total_comp_individual_costs[32]=''
            self.total_comp_quantity_cost[32]=''
        if st_name_4 != '':
            self.total_comp_types[33]=st_type
            self.total_comp_names[33]=st_name_4
            self.total_comp_values[33]=self.st_volume_4
            self.total_comp_quantities[33]=self.st_quantity_4
            self.total_comp_individual_costs[33]=self.st_cost_4
            self.total_comp_quantity_cost[33]=self.st_total_4
        else:
            self.total_comp_types[33]=''
            self.total_comp_names[33]=''
            self.total_comp_values[33]=''
            self.total_comp_quantities[33]=''
            self.total_comp_individual_costs[33]=''
            self.total_comp_quantity_cost[33]=''
        if st_name_5 != '':
            self.total_comp_types[34]=st_type
            self.total_comp_names[34]=st_name_5
            self.total_comp_values[34]=self.st_volume_5
            self.total_comp_quantities[34]=self.st_quantity_5
            self.total_comp_individual_costs[34]=self.st_cost_5
            self.total_comp_quantity_cost[34]=self.st_total_5
        else:
            self.total_comp_types[34]=''
            self.total_comp_names[34]=''
            self.total_comp_values[34]=''
            self.total_comp_quantities[34]=''
            self.total_comp_individual_costs[34]=''
            self.total_comp_quantity_cost[34]=''



        ### Update TreeView
        for k in self.treeview.get_children():
            self.treeview.delete(k)

        for i in range(len(self.total_comp_names)):
            try:
                self.treeview.insert('', tk.END,
                                     values=(self.total_comp_types[i], self.total_comp_names[i], self.total_comp_values[i], self.total_comp_quantities[i],
                                             f"{self.total_comp_individual_costs[i]:.2f}", f"{self.total_comp_quantity_cost[i]:.2f}"))
                i += 1
            except IndexError:
                self.treeview.insert('', tk.END, values=('', '', '', '', '', ''))
                i += 1
            except ValueError:
                self.treeview.insert('', tk.END, values=('', '', '', '', '', ''))
                i += 1
            self.treeview.pack(pady=2, padx=2)
        for col in self.columns:
            self.treeview.heading(col, text=col,
                                  command=lambda c=col: self.treeview_sort_column(self.treeview, c, False))

        



    def total_cost_calculate(self):
        # multiply quantities with individual costs to get total of each
        # then add up each of the results together to get the total overall result for the system.
        #FETCH INDIVIDUAL COSTS
        ### TOTAL SYSTEM COST
        self.total_system_cost = self.turbs_total + self.snt_total + self.plate_total + self.acc_total + self.pump_total + self.expander_total + self.st_total
        messagebox.showinfo(title='Results',message='Calculations Complete.')

        print("Turbines:",self.turbs_total)
        print("SNT:",self.snt_total)
        print("Plate:",self.plate_total)
        print("ACC:",self.acc_total)
        print("Pump:",self.pump_total)
        print("Expander:",self.expander_total)
        print("ST:",self.st_total)

        ### Update the TreeView table.
        ### Show results below the table.
        self.results_label['text'] = f"Total System Cost: £{self.total_system_cost:.2f}"

    def add_remove_validate(self, add_remove_inp):
        if add_remove_inp.isdigit():
            return True
        elif add_remove_inp is "":
            return True
        else:
            return False
    
    def cname_validate(self, cname_inp):
        if cname_inp is "":
            return True
        elif cname_inp is None:
            return False
        else:
            return True

    def area_validate(self, area_inp):
        if area_inp is "":
            return True
        elif area_inp is None:
            return False
        else:
            return True

    def power_validate(self, power_inp):
        if power_inp is "":
            return True
        elif power_inp is None:
            return False
        else:
            return True

    def volume_validate(self, volume_inp):
        if volume_inp.isdigit():
            return True
        elif volume_inp is "":
            return False
        elif volume_inp is None:
            return True
        else:
            return False

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
        
### Driver Code: Runs code above
def main():
    root = tk.Tk()
    app = NotebookTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()





