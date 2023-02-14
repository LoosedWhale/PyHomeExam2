from tkinter import *
from tkinter import messagebox


appSize = "340x465"
bgc = "#292929"
fgc = "gainsboro"
app = Tk()
app.title("Order Food")
app.geometry(appSize)
app.resizable(False, False)
app.configure(background=bgc)

class orderItem:
    def __init__(self, name, price, frame, quantity = 0):
        self.name = name
        self.price = price
        self.frame = Frame(frame)
        self.quantity = quantity
        self.draw(self.frame)
        self.Add.configure(command=self.add)
        self.Remove.configure(command=self.remove)

    def draw(self, frame):
        self.nameLabel = Label(frame, text=self.name, bg=bgc, fg=fgc)
        self.Add = Button(frame, text="  +  ", bg=bgc, fg="Green", activeforeground=bgc, activebackground="Green")
        self.Remove = Button(frame, text="   -   ", bg=bgc, fg="Red", activeforeground=bgc, activebackground="Red")
        self.priceLabel = Label(frame, text=f"{self.price} kr", bg=bgc, fg=fgc)
        self.quantityLabel = Label(frame, text=f"{self.quantity}", bg=bgc, fg=fgc)
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
        self.quantityLabel.configure(text=f"{self.quantity}")

    def remove(self):
        self.quantity -= 1
        if self.quantity < 0:
            self.quantity = 0
        self.quantityLabel.configure(text=f"{self.quantity}")

    def getTotalPrice(self):
        return self.quantity * self.price
    
    def getName(self):
        return self.name


def getTotal():
    totalPrice = 0
    itemNames = ""
    orderedItems = [Pizza, VBiff, Soup, Biff, Water, CocaCola, Beer, Wine, Pie, IceCream, Chocolate, Cake]

    for item in orderedItems:
        totalPrice += item.getTotalPrice()
        if item.quantity > 0:
            itemNames += item.getName() + " \n"
            if Beer.quantity == 69 :
                messagebox.askyesno(title="Warning", message="Kör försiktigt!")

    formatTotal = "Total: " + str(totalPrice) + " kr"  "\n"+  str(itemNames)
    
    if totalPrice == 0:
        OrderTextBox.configure(state='normal')
        OrderTextBox.delete(0.0, END)
        OrderTextBox.insert(0.0 , "Total: \nEmpty order")
        OrderTextBox.configure(state='disabled')
    else:
        OrderTextBox.configure(state='normal')
        OrderTextBox.delete(0.0, END)
        OrderTextBox.insert(0.0 , formatTotal)
        OrderTextBox.configure(state='disabled')



frameOne = Frame(app, bg=bgc)
frameTwo= Frame(app,  bg=bgc)
frameThree = Frame(app, bg=bgc) 
frameFour = Frame(app, bg=bgc)

frameOne.pack(side=LEFT, anchor=W)
frameTwo.pack(side=LEFT, anchor=W)
frameThree.pack(side=LEFT, anchor=W)
frameFour.pack(side=LEFT, anchor=W)


MainDishLabel = Label(frameOne, text="Main Dish", bg=bgc, fg="sandy brown", font=(None, 10, "bold"))
DrinkLabel = Label(frameTwo, text="Drink", bg=bgc, fg="CadetBlue2", font=(None, 10, "bold"))
DessertLabel = Label(frameThree, text="Dessert", bg=bgc, fg="salmon", font=(None, 10, "bold"))
OrderLabel = Label(frameFour, text="Order!", bg=bgc, fg="Gold", font=(None, 13, "bold"))

MainDishLabel.pack(fill=X)
DrinkLabel.pack(fill=X)
DessertLabel.pack(fill=X)
OrderLabel.pack(fill=X)


Pizza = orderItem("Pizza", 75, frameOne)
VBiff = orderItem("V.Biff", 100, frameOne)
Soup = orderItem("Soppa", 60, frameOne)
Biff = orderItem("Biff", 165, frameOne)

Water = orderItem("Vatten", 45, frameTwo)
CocaCola = orderItem("Cola", 55, frameTwo)
Beer = orderItem("Öl", 95, frameTwo)
Wine = orderItem("Vin", 100, frameTwo)

Pie = orderItem("Paj", 65, frameThree)
IceCream = orderItem("Glass", 55, frameThree)
Chocolate = orderItem("Choklad", 30, frameThree)
Cake = orderItem("Tårta", 65, frameThree)

Order = Button(frameFour, text="Order", command=getTotal, bg=bgc, fg="Gold", activeforeground=bgc, activebackground="Gold", font = (None, 10, "bold"))
OrderTextBox = Text(frameFour, height=26, width=20, bg=bgc, fg="Snow2") 
OrderTextBox.insert(END, "Total: ")
OrderTextBox.configure(state='disabled')

Order.pack(side=BOTTOM, fill=X)
OrderTextBox.pack(side=BOTTOM)

app.mainloop()