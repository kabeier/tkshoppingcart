from tkinter import Tk
from tkinter.ttk import Frame, Button
import tkinter as tk
from PIL import Image, ImageTk
import json
import os.path
from os import path
import csv
from Item import Item
import gc
#Its not pretty but it add and removes from list displays the list and has a quit button


class ShoppingCart(Frame):
    def __init__(self):
        super().__init__()
        self.shoppinglist = []
        self.adding = True
        self.itemlist = []
        self.notgarbage = []
        self.initUI()


    def initUI(self):
        def press():
            sc.delete("1.0", tk.END)
            sc.insert(tk.END, getList(self))

        def addpress():
            self.adding = not self.adding
            if self.adding == True:
                ar['text'] = "Click to Start \r Removing"
                press()
            else:
                ar['text'] = "Click to Start \r Adding"
                press()

        def shop(s):
            if(self.adding == True):
                self.shoppinglist.append(s)
            else:
                if s in self.shoppinglist:
                    self.shoppinglist.remove(s)
        
        def make_items():
            with open('items.csv', newline='') as csvfile:
                item_reader = csv.reader(csvfile, delimiter=',')
                next(item_reader)
                for row in item_reader:
                    newitem=Item(row[0],row[1],row[2])
                    self.itemlist.append(newitem)

        def make_item_buttons():
            row_position=2
            col_position=1
            i=2
            but=tk.Button()
            for newitem in self.itemlist:
                if(col_position > 4):
                    i+=1
                    col_position=1
                    row_position=i
                but = tk.Button(self, name=newitem.get_name().lower(), command=lambda i=newitem.get_name():[ shop(i),press()])
                but.config(image=newitem.get_tkImage(), width=200, height=200, bg="black")
                but.image = newitem.get_tkImage()
                but.grid(row=row_position, column=col_position)
                newitem.set_button(but)
                newitem.setimagelbl(but.image)
                col_position+=1

        self.master.title("Kevin's Fried Rice Store")
        restore(self)
        
        make_items()
        make_item_buttons()

        sc = tk.Text(self, height=13, width=30)
        sc.insert(tk.END, getList(self))
        sc.grid(row=2, column=5)

        ar = tk.Button(self, text="Click to start \r Removing", bg="darkblue", fg="white",
                       font='Helvetica 18 bold', width=10, height=5, command=lambda: [addpress()])
        ar.grid(row=3, column=5)

        quit = tk.Button(self, text="QUIT", fg="black", bg="red", font='Helvetica 18 bold', command=lambda: [
                         save(self), self.master.destroy()], width=10, height=5)
        quit.grid(row=4, column=5)

        self.pack()


def getList(self):
    items = 'Your Shopping Cart Contains: \n'
    total=0
    for item in set(self.shoppinglist):
        price=0
        for itemobj in self.itemlist:
            if(item==itemobj.get_name()):
                price = itemobj.get_price()
        total += self.shoppinglist.count(item)*price
        items += f"{item} [{self.shoppinglist.count(item)}] ${price*self.shoppinglist.count(item)} \n"
    items+="-"*25 +"\n"
    items+=f'Your total is ${total:,.2f}'


    return items


def main():
    root = Tk()
    root.configure(background="black")
    app = ShoppingCart()
    root.mainloop()


def restore(self):
    if path.isfile("save.json"):
        with open("save.json", "r") as save_file:
            data = json.load(save_file)
            self.shoppinglist = data
        pass


def save(self):
    with open("save.json", "w") as save_file:
        json.dump(self.shoppinglist, save_file)


if __name__ == '__main__':
    main()
