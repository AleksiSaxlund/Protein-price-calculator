class Calculator:
    #Converts values into floats. Asks new values until floats are given
    def valuechecker(self, value, text: str):
        try:
            value = float(value)
        except ValueError:
            print()
            print("Please input whole- or decimal numbers using dots.")
            value = input(text)
            value = self.valuechecker(value, text)
        return value

    #do calculations and run valuechecker
    def calculate(self, price_per_kg: str, protein_in_100g: str):
        price_per_kg = self.valuechecker(price_per_kg, "price per kg: ")
        protein_in_100g = self.valuechecker(protein_in_100g, "Protein in 100g: ")
        protein_in_100g /= 100
        price_per_kg /= 10
        protein_price_per_100g = price_per_kg / protein_in_100g

        return protein_price_per_100g

class ProteinCalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

    #return True for new loop, False to stop running
    def again(self):
        while True:
            print("Again? y/n")
            again = input()
            if again == "n":
                return True
            elif again == "y":
                return False      

    #take inputs, call calculate and print the results
    def inputs(self):
        input1 = input("Price per kg: ")
        input2 = input("Protein in 100g: ")
        price_of_100g_protein = self.calculator.calculate(input1, input2)

        print()
        print(f"Protein price per 100g: {price_of_100g_protein:.2f}")

    def run(self):
        while True:
            self.inputs()
            if self.again():
                break

ProteinCalculatorApp().run()