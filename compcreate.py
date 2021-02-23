# Component Creation
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms


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

            title_lbl = tk.Label(comp_canvas, text='Component Information %d' % count, fg='yellow', bg='gray25')
            title_lbl.pack()

            # Component Name
            name_frame = tk.Frame(comp_canvas, relief=tk.FLAT, bd=0, bg='gray15')
            name_frame.pack(side=tk.TOP, anchor=tk.N, fill=tk.X, expand=True)

            name_lbl = tk.Label(name_frame, relief=tk.FLAT, bd=0, bg='gray15')
            name_lbl.config(bd=0, text='Name: ', font='System 6', fg='yellow')
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
            metric_lbl.config(bd=0, text='%s' % metric_var_name, font='System 6', fg='yellow')
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
            quantity_lbl.config(bd=0, text='Quantity: ', font='System 6', fg='yellow')
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