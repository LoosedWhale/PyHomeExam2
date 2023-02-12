#(venv) PS C:\Users\theod\HomeExamPCVersion\PyHomeExam2\OrderFood> python .\OrderFood.py 

import tkinter
import customtkinter 


class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Dessert:
    def __init__(self, name, price):
        self.name = name
        self.price = price


foods = [Food("Pizza", 75),
         Food("Fake-biff", 100),
         Food("Soppa", 60),
         Food("Biff", 165)]

drinks = [Drink("Vatten", 45),
          Drink("Coca-cola", 55),
          Drink("Öl", 95),
          Drink("Vin", 100)]

desserts = [Dessert("Paj", 65),
            Dessert("Glass", 55),
            Dessert("Choklad", 30),
            Dessert("Tårta", 65)]

class CTkOptionMenu(tkinter.OptionMenu):
    def __init__(self, master, values, command):
        self._var = tkinter.StringVar()
        self._var.set(values[0][0])
        super().__init__(master, self._var, *values, command=lambda x: command(self._var.get()))

    def get(self):
        return self._var.get()


""" 

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x400")
        self.title("Order Food")
        self.maxsize(480, 400)
        self.minsize(480, 400)

        self.FoodL = customtkinter.CTkLabel(master=self, text="Food:", font= (None, 18), width = 10)
        self.FoodL.grid(row=0, column=0, padx = 20, pady = 10, sticky="nsew")

        foodNames = [food.name for food in foods]
        self.FoodOM = customtkinter.CTkOptionMenu(self, values=foodNames, command=self.optionmenuCallback)
        self.FoodOM.grid(row=1, column=0, padx=10, pady = 10, sticky="n")
    

        self.DrinkL = customtkinter.CTkLabel(master=self, text="Drink:", font= (None, 18), width = 10)
        self.DrinkL.grid(row=0, column=1, padx = 20, pady = 10, sticky="nsew")
        
        drinkNames = [drink.name for drink in drinks]
        self.DrinkOM = customtkinter.CTkOptionMenu(self, values=drinkNames, command=self.optionmenuCallback)
        self.DrinkOM.grid(row=1, column=1, padx=10, pady = 10, sticky="n")


        self.DessertL = customtkinter.CTkLabel(master=self, text="Dessert:", font= (None, 18), width = 10)
        self.DessertL.grid(row=0, column=2, padx = 20, pady = 10, sticky="nsew")

        dessertNames = [dessert.name for dessert in desserts]
        self.DessertOM = customtkinter.CTkOptionMenu(self, values=dessertNames, command=self.optionmenuCallback)
        self.DessertOM.grid(row=1, column=2, padx=10, pady = 10, sticky="n")

    # add methods to app
    def buttonClick(self):
        print("button click")

    def optionmenuCallback(self, choice):
        print("You have picked:", choice)



"""

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("480x400")
        self.title("Order Food")
        self.maxsize(480, 400)
        self.minsize(480, 400)

        self.FoodL = customtkinter.CTkLabel(master=self, text="Food:", font= (None, 18), width = 10)
        self.FoodL.grid(row=0, column=0, padx = 20, pady = 10, sticky="nsew")

        foodOptions = [(food.name, food.price) for food in foods]
        self.FoodOM = CTkOptionMenu(self, values=foodOptions, command=lambda x: self.optionmenuCallback(x, 'food'))
        self.FoodOM.grid(row=1, column=0, padx=10, pady = 10, sticky="n")
    

        self.DrinkL = customtkinter.CTkLabel(master=self, text="Drink:", font= (None, 18), width = 10)
        self.DrinkL.grid(row=0, column=1, padx = 20, pady = 10, sticky="nsew")
        
        drinkOptions = [(drink.name, drink.price) for drink in drinks]
        self.DrinkOM = CTkOptionMenu(self, values=drinkOptions, command=lambda x: self.optionmenuCallback(x, 'drink'))
        self.DrinkOM.grid(row=1, column=1, padx=10, pady = 10, sticky="n")

        self.DessertL = customtkinter.CTkLabel(master=self, text="Dessert:", font= (None, 18), width = 10)
        self.DessertL.grid(row=0, column=2, padx = 20, pady = 10, sticky="nsew")

        dessertOptions = [(dessert.name, dessert.price) for dessert in desserts]
        self.DessertOM = CTkOptionMenu(self, values=dessertOptions, command=lambda x: self.optionmenuCallback(x, 'dessert'))
        self.DessertOM.grid(row=1, column=2, padx=10, pady = 10, sticky="n")

        self.stringvar = tkinter.StringVar()

        self.textbox = customtkinter.CTkTextbox(master=self, width=30, height=100, corner_radius=5)
        self.textbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.textbox.insert("0.0", self.optionmenuCallback)
        
    # add methods to app
    def buttonClick(self):
        print("button click")

 
    def optionmenuCallback(self, choice, item_type):
        if item_type == 'food':
            items = foods
        elif item_type == 'drink':
            items = drinks
        elif item_type == 'dessert':
            items = desserts

        for item in items:
            if item.name == choice:
                self.textbox.insert("end", f"{item.name} {item.price}kr ")
        return self.textbox.insert("end", f"{item.name} {item.price}kr ")
        print("You have picked:", choice)


app = App()
app.mainloop()