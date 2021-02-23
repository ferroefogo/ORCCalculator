# Home Page
import tkinter as tk


class Home():
    def __init__(self, master, main_notebook):
        self.master = master
        home_page = tk.Frame(main_notebook, bg='gray20')
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