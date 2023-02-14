from tkinter import *
import tkinter as tk

size = "340x465"
bgc = "#292929"
fgc = "Gold"
app = tk.Tk()
app.title("Order Food")
app.geometry(size)
app.resizable(False, False)
app.configure(background=bgc)
class orderItem:
    def __init__(self, name, price, frame, quantity = 0):
        self.name = name
        self.price = price
        self.frame = tk.Frame(frame)
        self.quantity = quantity
        self.draw(self.frame)
        self.Add.configure(command=self.add)
        self.Remove.configure(command=self.remove)

    def draw(self, frame):
        self.nameLabel = Label(frame, text=self.name, bg=bgc, fg=fgc)
        self.Add = Button(frame, text="  +  ", bg=bgc, fg="Green", activeforeground=bgc, activebackground="Green")
        self.Remove = Button(frame, text="   -   ", bg=bgc, fg="Red", activeforeground=bgc, activebackground="Red")
        self.priceLabel = Label(frame, text=str(self.price) + "kr", bg=bgc, fg=fgc)
        self.quantityLabel = Label(frame, text=str(self.quantity), bg=bgc, fg=fgc)
        self.Line = Label(frame, text="___________", bg=bgc, fg=fgc)

        self.Line.pack(side = TOP, fill=X)
        self.nameLabel.pack(side = TOP, fill=X)
        self.priceLabel.pack(side = TOP, fill=X)
        self.quantityLabel.pack(side = BOTTOM, fill=X)
        self.Add.pack(side = LEFT, fill=X)
        self.Remove.pack(side = LEFT, fill=X)
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
    total += Pie.getPriceTotal()
    total += IceCream.getPriceTotal()
    total += Chocolate.getPriceTotal()
    total += Cake.getPriceTotal()

    if Beer.quantity > 0:
        foodNames += Beer.getName() + " \n"
    if Water.quantity > 0:
        foodNames += Water.getName() + " \n"
    if Wine.quantity > 0:
        foodNames += Wine.getName() + " \n"
    if CocaCola.quantity > 0:
        foodNames += CocaCola.getName() + " \n"
    if Pizza.quantity > 0:
        foodNames += Pizza.getName() + " \n"
    if VBiff.quantity > 0:
        foodNames += VBiff.getName() + " \n"
    if Soup.quantity > 0:
        foodNames += Soup.getName() + " \n"
    if Biff.quantity > 0:
        foodNames += Biff.getName() + " \n"
    if Pie.quantity > 0:
        foodNames += Pie.getName() + " \n"
    if IceCream.quantity > 0:
        foodNames += IceCream.getName() + " \n"
    if Chocolate.quantity > 0:
        foodNames += Chocolate.getName() + " \n"
    if Cake.quantity > 0:
        foodNames += Cake.getName() + " \n"

    formatTotal = "Total: " + str(total) + " kr"  "\n"+  str(foodNames + " ")
    if total == 0:
        OrderText.delete(0.0, END)
        OrderText.insert(0.0 , "Total: \nEmpty order")
    else:
        OrderText.delete(0.0, END)
        OrderText.insert(0.0 , formatTotal)



f1 = Frame(app, bg=bgc)
f2= Frame(app,  bg=bgc)
f3 = Frame(app, bg=bgc) 
f4 = Frame(app, bg=bgc)

f1.pack(side=LEFT, anchor=W)
f2.pack(side=LEFT, anchor=W)
f3.pack(side=LEFT, anchor=W)
f4.pack(side=LEFT, anchor=W)


MainDishL = Label(f1, text="Main Dish >", bg=bgc, fg="CadetBlue4")
DrinkL = Label(f2, text="Drink >>", bg=bgc, fg="CadetBlue3")
DessertL = Label(f3, text="Dessert >>>", bg=bgc, fg="CadetBlue2")
OrderL = Label(f4, text="Order!", bg=bgc, fg="CadetBlue1")

MainDishL.pack()
DrinkL.pack()
DessertL.pack()
OrderL.pack()


Beer = orderItem("Öl ", 95, f1)
Water = orderItem("Vatten", 45, f1)
Wine = orderItem("Vin", 100, f1)
CocaCola = orderItem("Cola", 55, f1)

Pizza = orderItem("Pizza", 75, f2)
VBiff = orderItem("V.biff", 100, f2)
Soup = orderItem("Soppa", 60, f2)
Biff = orderItem("Biff", 165, f2)

Pie = orderItem("Paj ", 65, f3)
IceCream = orderItem("Glass", 55, f3)
Chocolate = orderItem("Choklad", 30, f3)
Cake = orderItem("Tårta", 65, f3)

Order = Button(f4, text="Order", command=getTotal, bg=bgc, fg=fgc, activeforeground=bgc, activebackground=fgc)
Order.pack(side=BOTTOM)

OrderText = Text(f4, height=26, width=20, bg=bgc, fg="Snow2") 
OrderText.pack(side=BOTTOM)
OrderText.insert(END, "Total: ")

app.mainloop()