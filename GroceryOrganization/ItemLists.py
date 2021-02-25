from tkinter import *
import random

class ItemListing (Frame):
    def __init__ (self, master, cat_itm_amt_dict):
        super(ItemListing, self).__init__(master)

        self.main_dict = cat_itm_amt_dict

        
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.list_of_categories = list(self.main_dict.keys())

        column = 0
        for x in range(len(self.list_of_categories)):
            
            Label(self, text = self.list_of_categories[x], font = "Helvetica 40 bold", fg = "black").grid(row = 0, column = column)
            Label(self, text = "         ", font = "Helvetica 40 bold", fg = "black").grid(row = 0, column = column+1)
            Label(self, text = "         ", font = "Helvetica 40 bold", fg = "black").grid(row = 0, column = column+2)
            
            list_of_cat_items = list(self.main_dict[self.list_of_categories[x]].keys())
            list_of_itm_amt = list(self.main_dict[self.list_of_categories[x]].values())
            
            row = 1     
            for y in range(len(list_of_cat_items)):
                
                amount = list_of_itm_amt[y]
                name = list_of_cat_items[y]

                Label(self, 
                      text = "%s: %d" % (name, amount), 
                      font = "Times 25").grid(row = row, column = column)

                row += 1

            column += 3

            