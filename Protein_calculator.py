while True:
    try:
        price = float(input("Price per kg: "))
        protein_in_100g = float(input("Protein in 100g: "))
        
        protein_in_100g /= 100
        price /= 10 #per 100g hinta
        protein_price_per_100g = price / protein_in_100g

    except ValueError:
        print()
        print("Please input whole- or decimal numbers using dots.")
        print()
        continue

    print()
    print(f"Protein price per 100g: {protein_price_per_100g:.2f}")
    print()

    print("Again? y/n ")
    again = input()

    if again == "n":
        break

    print()