while True:
    price = float(input("Price per kg: "))
    protein_in_100g = float(input("Protein in 100g: "))

    protein_in_100g /= 100
    price /= 10 #per 100g hinta
    protein_price_per_100g = price / protein_in_100g

    print()
    print(f"Protein price per 100g: {protein_price_per_100g:.2f}")
    print()

    again = input("Again? y/n ")
    
    if again == "n":
        break