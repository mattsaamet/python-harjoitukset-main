print("-------TERVETULOA LASKINOHJELMAAN-------")

while True:
    print("Valitse mitä toimintoa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q= Lopeta ohjelma")
    valinta = input("Anna valintasi: ").upper()

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break

    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        tulos = a + b
        print(f"Yhteenlaskun tulos on: {tulos}")
        break
    elif valinta == "B":
        tulos = a - b
        print(f"Vähennyslaskun tulos on: {tulos}")
        break
    elif valinta == "C":
        tulos = a * b
        print(f"Kertolaskun tulos on: {tulos}")
        break
    elif valinta == "D":
        tulos = a / b
        print(f"Jakolaskun tulos on: {tulos}")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
print ("Ohjelma päättynyt")