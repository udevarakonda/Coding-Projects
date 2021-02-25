from tkinter import *
import random

class ItemChoosingScreen (Frame):
    def __init__ (self, master, category_list, callback_on_selected):
        super(ItemChoosingScreen, self).__init__(master)

        self.categories_list = category_list
        self.category_item_dict = {}

        self.grid()
        self.create_widgets()
        self.callback_on_selected = callback_on_selected

    def create_widgets(self):

        for x in range(len(self.categories_list)):
	        self.category_item_dict[self.categories_list[x]] = {}

        Label(self, text = "Enter the Items: ", font = "Helvetica 20 bold").grid(row = 0, column = 0, sticky = W)
        
        self.item_name = Entry(self, font = "Times 15")
        self.item_name.grid(row = 0, column = 1, sticky = W)
        self.item_name.config(width = 20)


        self.ItemValue = StringVar()
        self.ItemValue.set(None)

        column = 0

        for x in range(len(self.categories_list)):
            Radiobutton(self, text = self.categories_list[x], variable = self.ItemValue, value = self.categories_list[x], fg = "black").grid(row = 1, column = column)
            column += 1

        
        Label(self, text = "Enter the Amount of the Item: ", font = "Helvetica 20 bold").grid(row = 2, column = 0)
        self.amount_button = Entry(self)
        self.amount_button.grid(row = 2, column = 1)

        self.submit_button = Button(self, text = "Submit", font = "Helvetica 20 bold", fg = "blue", command = self.adding_item_to_dict)
        self.submit_button.grid(row = 3, column = 1)

        self.view_list_button = Button(self, text = "View List", font = "Times 30 bold", fg = "blue", bg = "orange", command = self.callback_on_selected)
        self.view_list_button.grid(row = 4, column = 1)

    def adding_item_to_dict(self):
        amount_of_items = int(self.amount_button.get())
        item_category = str(self.ItemValue.get())
        item_name = str(self.item_name.get())
        self.category_item_dict[item_category][item_name] = amount_of_items

        # print(self.category_item_dict)

    def callback_on_selected(self):
        self.callback_on_selected(self.category_item_dict)




    

    


