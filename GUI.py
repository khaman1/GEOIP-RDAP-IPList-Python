from Tkinter import *
import Tkinter as tk
import tkFont
import ttk
import numpy

class GUI(Frame):

    def __init__(self, header, mylist):
        Frame.__init__(self)

        self.header = header
        self.mylist = mylist
        self.tree = None

        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self, ):
        # Create a search bar to input
        self.search_var = StringVar()
        # When the user types in any character, the function self.update_list() will be called
        self.search_var.trace("w", lambda name, index, search_var=self.search_var: self.update_list())
        # Visualize it
        e = Entry(self.tree, textvariable=self.search_var)
        e.pack()
        
        container = ttk.Frame()
        container.pack(fill='both', expand=True)
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=self.header, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)


    def _build_tree(self):
        # Set the header for each column
        for col in self.header:
            # The heading can be sorted by the function self.sortby()
            self.tree.heading(col, text=col.title(),
                command=lambda c=col: self.sortby(c, 0))
            # adjust the column's width to the header string
            self.tree.column(col,
                width=tkFont.Font().measure(col.title()))

        # Sequentially insert each item in the list into the table
        for item in self.mylist:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(self.header[ix],width=None)<col_w:
                    self.tree.column(self.header[ix], width=col_w)

    # This function will be called whenever the user types
    # Firstly It will clear the entire table
    # Check if in any column, its content contains the text or not
    # Collect all the rows satisfied the conditioned
    # This process can speed up by letting the user choose what column to search
    def update_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        #search_item is the text read from the box search_var
        search_term = self.search_var.get()

        for item in self.mylist:

            flag=0
            for i in item:
                # Convert the term into string
                if ~isinstance(i,unicode):
                    if isinstance(i, numpy.float64) or isinstance(i, numpy.int64):
                        i = str(i)
                    else:
                        i = i.encode('utf-8')

                # The term should be compared to the text of any column in the lowercase form
                # If there exists a column that contains the text, accept the entire row and stop the seaerch
                if search_term.lower() in str(i).lower():
                    flag=1
                    break

            # If the row is accepted, print out all the values to the end line    
            if flag==1:
                self.tree.insert('', 'end', values=item)
                # adjust column's width if necessary to fit each value
                for ix, val in enumerate(item):
                    col_w = tkFont.Font().measure(val)
                    if self.tree.column(self.header[ix],width=None)<col_w:
                        self.tree.column(self.header[ix], width=col_w)   

    def sortby(self, col, descending):
        """sort tree contents when a column header is clicked on"""
        # grab values to sort
        data = [(self.tree.set(child, col), child) \
            for child in self.tree.get_children('')]
        # if the data to be sorted is numeric change to float
        #data =  change_numeric(data)
        # now sort the data in place
        data.sort(reverse=descending)
        for ix, item in enumerate(data):
            self.tree.move(item[1], '', ix)
        # switch the heading so it will sort in the opposite direction
        self.tree.heading(col, command=lambda col=col: self.sortby(col, \
            int(not descending)))
