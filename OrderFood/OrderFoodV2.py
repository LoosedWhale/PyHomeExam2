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






#frame1 = tk.Frame(app)
#frame1.pack(side = tk.TOP)


#frame2 = tk.Frame(app)
#frame2.pack(side=tk.TOP)


frame1 = Frame(app)
frame2= Frame(app)

#knapp1 = Button(frame1, text="Knapp1")
#knapp2= Button(frame1, text="Knapp2")

#knapp3 = Button(frame2, text="Knapp3")
#knapp4= Button(frame2, text="Knapp4")

#knapp1.pack()
#knapp2.pack()
#knapp3.pack()
#knapp4.pack()

frame1.pack(side=LEFT)
frame2.pack(side=RIGHT)

Öl = orderableItem("Öl", 50, frame1)
Vatten = orderableItem("Vatten", 45, frame1)
Kaffe = orderableItem("Vin", 30, app)
CocaCola = orderableItem("CocaCola", 25, app)



app.mainloop()