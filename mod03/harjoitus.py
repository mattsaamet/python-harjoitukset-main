nimi = input("Mikä sinun nimesi on? ")
if nimi == "Matti":
    print("Seuraava,kiitos!")
else:
    annos = int(input("Montako keittoannosta?"))
    hinta = annos * 5.9
    print(f"Keittoannoksen hinta on {hinta:.2f} euroa")
    print("Seuraava,kiitos!")
