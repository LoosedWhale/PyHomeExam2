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


foods = [Food("Hamburger", 50),
         Food("Pizza", 110),
         Food("Sushi", 150),
         Food("Tacos", 70)]

drinks = [Drink("Soda", 10),
          Drink("Water", 5),
          Drink("Juice", 8),
          Drink("Coffee", 20)]

desserts = [Dessert("Ice Cream", 25),
            Dessert("Cake", 30),
            Dessert("Fruit Salad", 15),
            Dessert("Chocolate", 10)]

class CTkOptionMenu(tkinter.OptionMenu):
    def __init__(self, master, values, command):
        self._var = tkinter.StringVar()
        self._var.set(values[0])
        super().__init__(master, self._var, *values, command=command)

    def get(self):
        return self._var.get()

    def _button_callback(self, value):
        self._command(value[0,1])
        print(f"Namn: {value[0]}, Pris: {value[1]}")
        self._dropdown_callback(self._current_value)


    

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

app = App()
app.mainloop()