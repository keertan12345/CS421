#Defining a class for Pens
class Pens: 
    
    def __init__(self, company, model, color, price):
        self.company = company
        self.model = model
        self.color = color
        self.price = price
        
    def getDetails(self):
        print("Company: " + self.company)
        print("Model: " + self.model)
        print("Color " + self.color)
        print("Price: " + self.price)
        print("\n")

#Creating a few instaces
Sharpie = Pens("Sharpie", "S-gel pen", "Black", "$11.99")
Paper_mate = Pens("Paper Mate", "Ballpoint pen", "Black, red, blue",
"$5.79")
BIC = Pens("BIC", "Xtra Life Ballpoint Pen", "Blue", "$6.48")
Pilot = Pens("Pilot G2", "Retractable Rolling Ball Gel Pens", "Blue",
"$16.70")

Sharpie.getDetails()
Paper_mate.getDetails()
