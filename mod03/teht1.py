pituus = float(input("Anna kuhan pituus senttimetreinä: "))

ALAMITTA = 37

if pituus < ALAMITTA:
    puuttuvat_sentit = ALAMITTA - pituus
    print("Laske kuha takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuvat_sentit:.1f} senttimetriä.")
else:
    print("Kuha on riittävän pitkä, voit ottaa sen mukaasi.")