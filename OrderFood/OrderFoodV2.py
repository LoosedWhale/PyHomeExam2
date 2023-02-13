from tkinter import *
import tkinter as tk

size = "400x400"
app = tk.Tk()
app.title("Order Food")
app.geometry()




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

    def getPriceTotal(self):
        return self.quantity * self.price
    
    def getName(self):
        return self.name


           


frame1 = Frame(app)
frame2= Frame(app)
frame3 = Frame(app) 
frame4 = Frame(app)

frame1.pack(side=LEFT)
frame2.pack(side=LEFT)
frame3.pack(side=LEFT)
frame4.pack(side=RIGHT)

Beer = orderableItem("Öl", 95, frame1)
Water = orderableItem("Vatten", 45, frame1)
Wine = orderableItem("Vin", 100, frame1)
CocaCola = orderableItem("CocaCola", 55, frame1)

Pizza = orderableItem("Pizza", 75, frame2)
VBiff = orderableItem("Fake-biff", 100, frame2)
Soup = orderableItem("Soppa", 60, frame2)
Biff = orderableItem("Biff", 165, frame2)

Paj = orderableItem("Paj", 65, frame3)
IceCream = orderableItem("Glass", 55, frame3)
Chocolate = orderableItem("Choklad", 30, frame3)
Cake = orderableItem("Tårta", 65, frame3)

def getTotal():
    total = 0
    foodNames = ""
    total += Beer.getPriceTotal()
    total += Water.getPriceTotal()
    total += Wine.getPriceTotal()
    total += CocaCola.getPriceTotal()
    total += Pizza.getPriceTotal()
    total += VBiff.getPriceTotal()
    total += Soup.getPriceTotal()
    total += Biff.getPriceTotal()
    total += Paj.getPriceTotal()
    total += IceCream.getPriceTotal()
    total += Chocolate.getPriceTotal()
    total += Cake.getPriceTotal()

    if Beer.quantity > 0:
        foodNames += Beer.getName() + " "
    if Water.quantity > 0:
        foodNames += Water.getName() + " "
    if Wine.quantity > 0:
        foodNames += Wine.getName() + " "
    if CocaCola.quantity > 0:
        foodNames += CocaCola.getName() + " "
    if Pizza.quantity > 0:
        foodNames += Pizza.getName() + " "
    if VBiff.quantity > 0:
        foodNames += VBiff.getName() + " "
    if Soup.quantity > 0:
        foodNames += Soup.getName() + " "
    if Biff.quantity > 0:
        foodNames += Biff.getName() + " "
    if Paj.quantity > 0:
        foodNames += Paj.getName() + " "
    if IceCream.quantity > 0:
        foodNames += IceCream.getName() + " "
    if Chocolate.quantity > 0:
        foodNames += Chocolate.getName() + " "
    if Cake.quantity > 0:
        foodNames += Cake.getName() + " "
        

    formatTotal = "Total: " + str(total) + " kr"  "\n"+  str(foodNames + " ")
    if total == 0:
        print("Empty order")
        OrderText.delete(0.0, END)
        OrderText.insert(0.0 , "Empty order")
    else:
        print(formatTotal)
        OrderText.delete(0.0, END)
        OrderText.insert(0.0 , formatTotal)

Order = Button(frame4, text="Order", command=getTotal)
Order.pack(side=BOTTOM)

OrderText = Text(frame4, height=10, width=30)
OrderText.pack()
OrderText.insert(END, "Order: ")

app.mainloop()