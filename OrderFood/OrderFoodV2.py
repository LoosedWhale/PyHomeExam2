from tkinter import *
import tkinter as tk

size = "400x400"
app = tk.Tk()
app.title("Order Food")
app.geometry(size)




class orderableItem:
    def __init__(self, name, price, frame, quantity = 0):
        self.name = name
        self.price = price
        self.frame = tk.Frame(frame)
        self.quantity = quantity
        self.draw(self.frame)
        self.Add.configure(command=self.add)
        self.Remove.configure(command=self.remove)



    def draw(self, frame):
        self.namelabel = tk.Label(frame, text=self.name)
        self.Add = tk.Button(frame, text=" + ")
        self.Remove = tk.Button(frame, text=" - ")
        self.priceLabel = tk.Label(frame, text=str(self.price) + "kr")
        self.quantityLabel = tk.Label(frame, text=str(self.quantity))

        self.namelabel.pack(side = tk.LEFT, padx = 10)
        self.Add.pack(side = tk.LEFT, padx = 2)
        self.Remove.pack(side = tk.LEFT, padx = 2)
        self.priceLabel.pack(side = tk.LEFT)
        self.quantityLabel.pack(side = tk.LEFT)

        self.frame.pack()

    def add(self):
        self.quantity += 1
        self.quantityLabel.configure(text=str(self.quantity))

    def remove(self):
        self.quantity -= 1
        if self.quantity < 0:
            self.quantity = 0
        self.quantityLabel.configure(text=str(self.quantity))

    def getItemtotal(self):
        return self.quantity * self.price


           



#frame1 = tk.Frame(app)
#frame1.pack(side = tk.TOP)


#frame2 = tk.Frame(app)
#frame2.pack(side=tk.TOP)


frame1 = Frame(app)
frame2= Frame(app)
frame3 = Frame(app)

frame1.pack(side=LEFT)
frame2.pack(side=LEFT)
frame3.pack(side=LEFT)

Beer = orderableItem("Öl", 95, frame1)
Water = orderableItem("Vatten", 45, frame1)
Wine = orderableItem("Vin", 100, frame1)
CocaCola = orderableItem("CocaCola", 55, frame1)

Pizza = orderableItem("Pizza", 75, frame2)
VBiff = orderableItem("Fake-biff", 100, frame2)
Soup = orderableItem("Soppa", 60, frame2)
Biff = orderableItem("Biff", 165, frame2)

Paj = orderableItem("Paj", 65, frame3)
Icecream = orderableItem("Glass", 55, frame3)
Chocolate = orderableItem("Choklad", 30, frame3)
Cake = orderableItem("Tårta", 65, frame3)

def getTotal():
    total = 0
    total += Beer.getItemtotal()
    total += Water.getItemtotal()
    total += Wine.getItemtotal()
    total += CocaCola.getItemtotal()
    total += Pizza.getItemtotal()
    total += VBiff.getItemtotal()
    total += Soup.getItemtotal()
    total += Biff.getItemtotal()
    total += Paj.getItemtotal()
    total += Icecream.getItemtotal()
    total += Chocolate.getItemtotal()
    total += Cake.getItemtotal()
    print(total)

Order = tk.Button(frame1, text="Order", command=getTotal)
Order.pack(side = tk.BOTTOM)

app.mainloop()