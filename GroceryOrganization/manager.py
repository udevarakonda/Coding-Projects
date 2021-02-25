from tkinter import *
from CategoryAskerScreen import CategoryAskingScreen
from ItemChooser import ItemChoosingScreen
from ItemLists import ItemListing

class GroceryManager (object):

    def __init__ (self):

        self.root = Tk()
        self.root.geometry("2000x1000")
        self.current_screen = None  
        self.countries_roster = None
        

    def setup_startScreen (self):

        self.root.title ("Choosing Categories: ")

        self.current_screen = CategoryAskingScreen(master = self.root, callback_on_selected = self.item_chooser)

    def item_chooser (self, list_of_categories):

        self.list_of_categories = list_of_categories

        self.root.title ("Choosing items: ")

        self.current_screen.destroy()
        self.current_screen = ItemChoosingScreen(master = self.root, category_list = self.list_of_categories, callback_on_selected = self.print_list)


    def print_list (self, dictionary):

        self.item_cat_amt_dict = dictionary

        self.root.title("Item List:")

        self.current_screen.destroy()
        self.current_screen = ItemListing(master = self.root, cat_itm_amt_dict = self.item_cat_amt_dict)

        

        

def main():
    grocery_manager = GroceryManager()

    grocery_manager.setup_startScreen()

    grocery_manager.root.mainloop()

main()


    

    