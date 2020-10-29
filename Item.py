from PIL import Image, ImageTk
class Item:

    def __init__(self, name, imagefile, price):
        self.imagefile=imagefile
        self.button=None
        self.name=name
        self.price=price
        self.tkImage = ImageTk.PhotoImage(file=self.imagefile)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
    
    def get_tkImage(self):
        return self.tkImage

    def get_name(self):
        return self.name
    
    def get_price(self):
        return float(self.price)
    
    def change_price(self,newprice):
        self.price=newprice
    
    def set_button(self,button):
        self.button=button
    
    def setimagelbl(self,image):
        self.imagelbl=image

    
    
