from tkinter import *
import random

class CategoryAskingScreen (Frame):
    def __init__ (self, master, callback_on_selected):
        super(CategoryAskingScreen, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.categories_list = []
        self.callback_on_selected = callback_on_selected


    def create_widgets(self):

        Label(self, text = "Enter the Categories Below. Max 4: ", font = "Helvetica 20 bold").grid(row = 0, column = 0, sticky = W)
        
        self.categories = Entry(self, font = "Times 15")
        self.categories.grid(row = 0, column = 1, sticky = W)
        self.categories.config(width = 20)

        self.category_submit_button = Button(self, text = "Submit", font = "Helvetica 20 bold", fg = "black", command = self.submit_categories)
        self.category_submit_button.grid(row = 1, column = 1, sticky = W)

        self.finish_button = Button(self, text = "Start Choosing Items", font = "Helvetica 20 bold", fg = "black", command = self.callback_on_selected)
        self.finish_button.grid(row = 5, column = 5)

        self.row = 2
        self.column = 0

    def submit_categories(self):
        entered_category = self.categories.get()
        entered_category = str(entered_category)

        self.categories_list.append(entered_category)
        self.categories["text"] = ""

        self.print_categories()

    def print_categories(self):
            for x in range(len(self.categories_list)):
                Label(self, text = self.categories_list[x]).grid(row = self.row, column = self.column)
            
            self.column += 1

    def callback_on_selected(self):
        self.callback_on_selected(self.categories_list)




        